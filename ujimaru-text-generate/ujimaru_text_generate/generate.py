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
sentencepice_dir = os.path.expanduser('ujimaru_text_generate/sentencepiece')
reformer_dir = os.path.expanduser('ujimaru_text_generate/reformer')

with open(os.path.join(sentencepice_dir, "wiki-daimyo.txt")) as f:
    text = f.read().strip()

# %%
TOKENIZER = SentencePieceProcessor()
TOKENIZER.load(os.path.join(sentencepice_dir, 'wiki-daimyo.model'))

# %%
IDS = TOKENIZER.EncodeAsIds(text)
IDS = onp.asarray(IDS, dtype=onp.int32)
print("Number of tokens:", IDS.shape[0])

# Configure hyperparameters.
gin.parse_config_file('ujimaru_text_generate/config.gin')

# %%

# As we report in the Reformer paper, increasing the number of hashing rounds
# helps with quality. We can even increase the number of hashing rounds at
# evaluation time only.
gin.parse_config("""LSHCausalAttention.n_hashes = 4""")
model_infer = trax.models.ReformerLM(mode='predict')

# Set up the initial state for sampling.
initial_state = model_infer.new_weights_and_state(
    trax.supervised.trainer_lib.ShapeDtype((1, 1), dtype=np.int32))[1]

# load pretrained weight
model_infer.init_from_file(os.path.join(
    reformer_dir, "model.pkl"), weights_only=True)

print(trax.math.device_count())


def prediction(length=2048, prompt=None,):
    """Sample from the ReformerLM model"""
    # Token id 0 is the equivalent of a "start" token
    model_infer.state = initial_state             # stateの初期化
    cur_inputs = np.zeros((1, 1), dtype=np.int32)  # 初期値=0の挿入
    all_samples = []
    if prompt is not None:
        prompt = np.asarray(TOKENIZER.EncodeAsIds(prompt))

    for iteration in range(length):
        logits = model_infer(cur_inputs)

        if prompt is not None and iteration < prompt.shape[0]:
            cur_samples = onp.array(prompt[iteration], dtype=int)
        else:
            logits = onp.array(logits)[0, 0, :]
            probs = onp.exp(logits)
            cur_samples = onp.random.choice(probs.shape[-1], p=probs[:])
            cur_samples = onp.array(cur_samples, dtype=int)

        all_samples.append(cur_samples)
        cur_inputs = np.array(cur_samples[None, None])

    all_samples = onp.stack(all_samples, -1)

    return all_samples


prefix = [5, 3, 5, 2, 1, 6]
pred = prediction(10, "家康は")

print(TOKENIZER.DecodeIds(pred.tolist()))
