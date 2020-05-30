import markovify
import json


def clean_text(sentence: str) -> str:
    if sentence:
        sentence = sentence.replace(" ", "")
        return sentence + "\n"
    else:
        return ""


models = []

model_paths = [
    "models/trimodel-d0ra1998.json",
    "models/trimodel-hpp_ricecake.json",
    "models/trimodel-nasa_desu.json",
    "models/trimodel-p1ass.json",
    "models/trimodel-saitoeku3.json",
    "models/trimodel-schktjm.json",
    "models/trimodel-takanakahiko.json",
    "models/trimodel-uzimaru0000.json",
    "models/trimodel-yt8492.json",
]

for path in model_paths:
    with open(path) as f:
        model_json = json.load(f)
    models.append(markovify.Text.from_json(model_json))

with open("models/trimodel-uzimaru0000-big.json") as f:
    big_model_json = json.load(f)
    models.append(markovify.Text.from_json(big_model_json))

weights = [0.1] * (len(models) - 1)
weights.append(3.1)

model = markovify.combine(models, weights)

with open("../shared/markov-generated/tri-generated-all-3.txt", "w") as f:
    for _ in range(1000):
        sentence = clean_text(model.make_sentence())
        f.write(sentence)

with open("models/ujimaru.json", "w") as f:
    json.dump(model.to_json(), f)
