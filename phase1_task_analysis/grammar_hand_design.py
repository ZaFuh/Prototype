def generate_grammar(requirements_json):
    grammar = {
        "N": ["Hand", "Finger", "Joint", "Palm"],
        "T": ["Material", "ForceType", "PrecisionLevel"],
        "A": ["H", "F", "J", "P"],
        "R": [
            "Hand -> Palm + Finger*5",
            "Finger -> Joint*3 + Tip",
            "Joint -> (hinge | ball)"
        ],
        "S": "Hand"
    }
    return grammar
