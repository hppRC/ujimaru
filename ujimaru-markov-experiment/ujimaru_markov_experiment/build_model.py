from pyknp import Juman
import markovify
import MeCab
from pyknp import Juman
import json


jumanpp = Juman()


def wakati(sentence: str) -> str:
    try:
        return " ".join(token.midasi for token in jumanpp.analysis(sentence.strip()))
    except:
        return ""


def parse_text(filepath):
    with open(filepath) as f:
        corpus = f.readlines()

    return "\n".join(wakati(line) for line in corpus)


def build_model(parsed_text, state_size=2):
    return markovify.NewlineText(parsed_text, state_size)


filepath = "../shared/uzimaru0000.txt"

parsed_text = parse_text(filepath)

model = build_model(parsed_text, state_size=3)

with open("models/trimodel-uzimaru0000-big.json", "w") as f:
    json.dump(model.to_json(), f)
