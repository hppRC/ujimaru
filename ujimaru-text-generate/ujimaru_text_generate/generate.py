# %%

import gin
import os
import jax
import trax
from trax.supervised import inputs

import numpy as onp
import jax.numpy as np

from scipy.special import softmax

from sentencepiece import SentencePieceProcessor

import subprocess


# %%
# print(subprocess.run("tree"))

# %%
TOKENIZER = SentencePieceProcessor()
TOKENIZER.load('ujimaru_text_generate/sentencepiece/wiki-daimyo.model')


# %%
# IDS = TOKENIZER.EncodeAsIds(text)
# IDS = onp.asarray(IDS, dtype=onp.int32)
# print("Number of tokens:", IDS.shape[0])


# %%
# Configure hyperparameters.
gin.parse_config("""
import trax.layers
import trax.models
import trax.optimizers
import trax.supervised.inputs
import trax.supervised.trainer_lib

# Parameters that will vary between experiments:
# ==============================================================================
train.model = @trax.models.ReformerLM
# Our model will have 6 layers, alternating between the LSH attention proposed
# in the Reformer paper and local attention within a certain context window.
n_layers = 6
attn_type = [
  @TimeBinCausalAttention,
  @LSHCausalAttention,  
  @TimeBinCausalAttention,
  @LSHCausalAttention,
  @TimeBinCausalAttention,
  @LSHCausalAttention,
  ]
share_qk = False  # LSHCausalAttention ignores this flag and always shares q & k
n_heads = 2
attn_kv = 64
dropout = 0.05
n_tokens = 524288

# Parameters for MultifactorSchedule:
# ==============================================================================
MultifactorSchedule.constant = 0.01
MultifactorSchedule.factors = 'constant * linear_warmup * cosine_decay'
MultifactorSchedule.warmup_steps = 100
MultifactorSchedule.steps_per_cycle = 900

# Parameters for Adam:
# ==============================================================================
Adam.weight_decay_rate=0.0
Adam.b1 = 0.86
Adam.b2 = 0.92
Adam.eps = 1e-9

# Parameters for TimeBinCausalAttention:
# ==============================================================================
TimeBinCausalAttention.bin_length = 64
TimeBinCausalAttention.dropout = 0.05
TimeBinCausalAttention.n_bins = None
TimeBinCausalAttention.share_qk = %share_qk

# Parameters for LSHCausalAttention:
# ==============================================================================
LSHCausalAttention.allow_duplicate_attention = False
LSHCausalAttention.attend_across_buckets = True
LSHCausalAttention.rehash_each_round = True
LSHCausalAttention.data_rotation = False
LSHCausalAttention.n_bins = 4096
LSHCausalAttention.n_buckets = 8192
LSHCausalAttention.factorize_hash = [64, 128]
LSHCausalAttention.n_hashes = 1
LSHCausalAttention.one_rng = False
LSHCausalAttention.hard_k = 0
LSHCausalAttention.dropout = 0.0
LSHCausalAttention.drop_for_hash_rate = 0.0
LSHCausalAttention.max_len_for_inference = 2048
LSHCausalAttention.bucket_capacity_for_inference = 64

# Parameters for ReformerLM:
# ==============================================================================
ReformerLM.attention_type = %attn_type
ReformerLM.d_attention_key = %attn_kv
ReformerLM.d_attention_value = %attn_kv
ReformerLM.d_model = 256
ReformerLM.d_ff = 512
ReformerLM.dropout = %dropout
ReformerLM.ff_activation = @trax.layers.Relu
ReformerLM.max_len = %n_tokens
ReformerLM.mode = 'train'
ReformerLM.n_heads = %n_heads
ReformerLM.n_layers = %n_layers
ReformerLM.vocab_size = 320
ReformerLM.share_qk = %share_qk
ReformerLM.axial_pos_shape = (512, 1024)
ReformerLM.d_axial_pos_embs= (64, 192)
""")
# %%
output_dir = os.path.expanduser('ujimaru_text_generate/reformer')


# %%

# trainer = trax.supervised.Trainer(
#     model=trax.models.ReformerLM,
#     loss_fn=trax.layers.CrossEntropyLoss,
#     optimizer=trax.optimizers.Adam,
#     lr_schedule=trax.lr.MultifactorSchedule,
#     inputs=trax.supervised.inputs.Inputs(my_inputs),
#     output_dir=output_dir,
#     has_weights=True)


# %%

# As we report in the Reformer paper, increasing the number of hashing rounds
# helps with quality. We can even increase the number of hashing rounds at
# evaluation time only.
# gin.parse_config("""LSHCausalAttention.n_hashes = 4""")
# model_infer = trax.models.ReformerLM(mode='predict')

# %%

# Initialize model for inference.
# gin.parse_config("""LSHCausalAttention.n_hashes = 4""")
model_infer = trax.models.ReformerLM(mode='predict')
print(model_infer)


# %%


# Set up the initial state for sampling.
initial_state = model_infer.new_weights_and_state(
    trax.supervised.trainer_lib.ShapeDtype((1, 1), dtype=np.int32))[1]
print(initial_state)


# %%

# load pretrained weight
model_infer.init_from_file("ujimaru_text_generate/reformer/model.pkl")


# %%
