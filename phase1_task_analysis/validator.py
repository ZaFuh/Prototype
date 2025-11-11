#Simple rule-based validation (LLM-based validator can be stubbed later...

def validate_grammar(grammar):
    # simple checks
    if "Hand" not in grammar["N"]:
        return False, "Missing 'Hand' non-terminal."
    return True, "Grammar structurally valid."
