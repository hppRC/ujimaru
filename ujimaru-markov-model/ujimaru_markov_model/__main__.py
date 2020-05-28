import markovify
import json


def clean_text(sentence: str) -> str:
    if sentence:
        sentence = sentence.replace(" ", "")
        return sentence + "\n"
    else:
        return ""


models = []

for name in ["ujimaru_markov_model/trimodel.json", "ujimaru_markov_model/hpp-trimodel.json", "ujimaru_markov_model/nasa-trimodel.json"]:
    with open(name) as f:
        model_json = json.load(f)
    models.append(markovify.Text.from_json(model_json))

model = markovify.combine(models, [1, 1, 1])

with open("ujimaru_markov_model/tri-generated-some.txt", "w") as f:
    for _ in range(200):
        sentence = clean_text(model.make_sentence())
        print(sentence, end="")
        f.write(sentence)
