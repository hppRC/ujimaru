from pyknp import Juman
import markovify
import MeCab
from pyknp import Juman


jumanpp = Juman()


def wakati(sentence: str) -> str:
    return " ".join(token.midasi for token in jumanpp.analysis(sentence.strip()))


def parse_text(filepath):
    with open(filepath) as f:
        corpus = f.readlines()

    return "\n".join(wakati(line) for line in corpus)


def build_model(parsed_text, state_size=2):
    return markovify.NewlineText(parsed_text, state_size)


def clean_text(sentence: str) -> str:
    if sentence:
        sentence = sentence.replace(" ", "")
        return sentence + "\n"
    else:
        return ""


filepath = "ujimaru_markov_model/tweets-uzimaru0000.txt"

parsed_text = parse_text(filepath)

model = build_model(parsed_text, state_size=2)


with open("ujimaru_markov_model/generated.txt", "w") as f:
    for _ in range(100):
        sentence = clean_text(model.make_sentence())
        print(sentence, end="")
        f.write(sentence)
    for _ in range(100):
        sentence = clean_text(model.make_sentence_with_start("えっち"))
        print(sentence, end="")
        f.write(sentence)
