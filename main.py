from phase1_task_analysis.llm_task_analysis import generate_functional_json
from phase1_task_analysis.grammar_hand_design import generate_grammar
from phase1_task_analysis.validator import validate_grammar
from phase2_geometry_parameterization.parameter_generator import generate_parameters
from phase2_geometry_parameterization.open_parametric_interface import generate_stl
from phase3_morphology_filter.constraint_checker import check_constraints
from phase4_diversity.variant_generator import generate_variants
from phase5_ranking.evaluator import evaluate

def main():
    print("---- Prosthetic Hand Design Pipeline ----")
    prompt = "Design a prosthetic hand for fine manipulation of small, fragile objects."
    
    req = generate_functional_json(prompt)
    grammar = generate_grammar(req)
    valid, msg = validate_grammar(grammar)
    print(f"Grammar validation: {msg}")
    
    if not valid: return

    params = generate_parameters(grammar, req)
    ok, msg = check_constraints(params)
    print(msg)
    if not ok: return

    variants = generate_variants(params, 3)

    print("\nGenerated Variants and Scores:")
    for i, v in enumerate(variants):
        score = evaluate(v)
        print(f"Variant {i+1}:", v, "→", score)
        generate_stl(v, f"variant_{i+1}.stl")

if __name__ == "__main__":
    main()
