
def isClean(sentence):
    if "RT @" in sentence or "ポストに到達しました！" in sentence:
        return False
    else:
        return True


with open("ujimaru_markov_model/uzimaru0000.txt") as f:
    texts = f.readlines()

texts = filter(lambda x: isClean(x), texts)

with open("ujimaru_markov_model/clean.txt", "w") as f:
    f.write("".join(texts))
