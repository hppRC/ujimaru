import markovify
import json
import os

class Ujimaru(object):
    def __init__(self):
        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, "data", "ujimaru.json")
        with open(DATA_PATH) as f:
            big_model_json = json.load(f)
        self.model = markovify.Text.from_json(big_model_json)

    @staticmethod
    def clean_text(sentence: str) -> str:
        if sentence:
            sentence = sentence.replace(" ", "")
            return sentence.strip()
        else:
            return ""

    def make_sentence(self):
        while not (sentence := Ujimaru.clean_text(self.model.make_sentence())):
            continue
        return sentence

    def make_tweet(self):
        while not (sentence := Ujimaru.clean_text(self.model.make_short_sentence(140))):
            continue
        return sentence


if __name__ == "__main__":
    ujimaru = Ujimaru()
    print(ujimaru.make_sentence())
    print(ujimaru.make_tweet())
