from build_model import build_model, parse_text
import json

users = ["uzimaru0000",
         "p1ass",
         "hpp_ricecake",
         "yt8492",
         "takanakahiko",
         "nasa_desu",
         "saitoeku3",
         "d0ra1998",
         "schktjm"]

for name in users:
    filepath = f"../shared/users/tweets-{name}.txt"
    parsed_text = parse_text(filepath)

    model = build_model(parsed_text, state_size=3)
    with open(f"models/trimodel-{name}.json", "w") as f:
        json.dump(model.to_json(), f)
