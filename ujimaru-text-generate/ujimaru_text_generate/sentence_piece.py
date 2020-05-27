# %%
import sentencepiece as spm
from bs4 import BeautifulSoup

with open("ujimaru_text_generate/sentencepiece/tweets-uzimaru0000.txt") as f:
    corpus = [s.strip() for s in f.readlines()]

# %%
spm.SentencePieceTrainer.Train(
    '--input=ujimaru_text_generate/sentencepiece/tweets-uzimaru0000.txt, --model_prefix=ujimaru_text_generate/sentencepiece/uzimaru0000 --character_coverage=0.9995 --vocab_size=7000 --pad_id=3'
)

# %%
sp = spm.SentencePieceProcessor()
sp.Load("ujimaru_text_generate/sentencepiece/uzimaru0000.model")

# %%
print(sp.EncodeAsPieces(corpus[70]))

# %%
print(sp.EncodeAsIds(corpus[70]))
# [16, 111, 17, 211, 28, 4, 4228, 67, 2268, 10, 1564, 20, 4, 6106, 3832, 81, 15, 2268, 124, 55, 2311, 23, 2268, 157, 12, 4909, 366, 476, 1050, 61, 15, 113, 7923, 242, 13, 7, 4, 3870, 15, 98, 1010, 13, 6069, 4, 6106, 653, 2377, 6, 52, 4, 3030, 997, 1144, 10, 6024, 18, 2738, 1537, 20, 4, 93, 1413, 5, 3947, 39, 10, 1564, 12, 654, 101, 2634, 63, 70, 7974, 232, 15, 4582, 55, 1195, 56, 4, 793, 2180, 12, 4388, 51, 958, 736, 529, 9, 4287, 10, 4, 76, 17, 5, 2015, 18, 229, 12, 2635, 7, 2738, 1537, 20, 4, 7784, 285, 7, 3539, 6]

# %%
tokens = ["コミット", "と", "迷った", "けど", "RT", "は", "デプロイ",
          "って", "感じ", "が", "した", "ので", "CD", "って", "言い", "ました"]
print("sp.DecodePieces(tokens)", sp.DecodePieces(tokens))

# %%
ids = sp.EncodeAsIds(corpus[70])
print("sp.EncodeAsIds(corpus[70])", ids)
print("sp.DecodeIds(ids)", sp.DecodeIds(ids))

# %%
print("sp.GetPieceSize()", sp.GetPieceSize())
# 8000

# %%
print(sp.PieceToId('</s>'))
print(sp["</s>"])
print("-" * 10)
# %%
print("CDされるから...")
for i in sp.EncodeAsIds("CDされるから..."):
    print(i, sp.IdToPiece(i))
print("-" * 10)

# %%
print("最近ツイート数がおおい気がする")
for i in sp.EncodeAsIds("最近ツイート数がおおい気がする"):
    print(i, sp.IdToPiece(i))
print("-" * 10)
# %%
print("ひさびさに寝過ぎた")
for i in sp.EncodeAsIds("ひさびさに寝過ぎた"):
    print(i, sp.IdToPiece(i),)
