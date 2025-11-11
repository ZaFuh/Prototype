#Bias LLM or tweak parameters for diversity.

import random

def generate_variants(base_params, count=3):
    variants = []
    for _ in range(count):
        v = base_params.copy()
        v["finger_length"] += random.randint(-5, 5)
        v["joint_diameter"] += random.randint(-1, 1)
        variants.append(v)
    return variants
