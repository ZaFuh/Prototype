# LLM-Driven Prosthetic Hand Design Pipeline

An end-to-end automated pipeline for generating task-specific, 3D-printable prosthetic hand designs using Large Language Models and formal grammar systems.

## Overview

This project implements a multi-phase pipeline that transforms high-level task descriptions into validated, printable prosthetic hand designs. By combining LLM semantic understanding with formal design grammars and morphological constraints, the system generates diverse, functional hand designs optimized for specific manipulation tasks.

## Pipeline Architecture

### Phase 1: Dual-Level Task Analysis

**1.1 Task Analysis via LLM**

- Generates structured JSON with functional requirements through semantic understanding
- Analyzes three key dimensions:
  - **Task Understanding**: Primary goal, object manipulation, force and precision requirements
  - **Object Properties**: Size, material, fragility, surface friction
  - **Grasp Classification**: Force-based, fine manipulation, or tool-based grasps

**1.2 Grammar-Based Hand Design**

- Implements formal context-free grammar: `Ghand = (N, T, A, R, S)`
  - `N`: Non-terminal components
  - `T`: Terminal components
  - `A`: Component alphabet
  - `R`: Production rules
  - `S`: Start symbol
- Maps functional requirements to grammar through LLM-guided generation

**1.3 Validation & Revision Loop**

- **Rule-Based Validator**: Programmatic checks for deterministic structural constraints with severity annotations
- **LLM Structural Assessment**: Question-answering task for structural completeness and feasibility scoring
- **Iterative Refinement**: Combined validation scores determine pass/fail; failures trigger re-prompting with diagnostic feedback

### Phase 2: Geometry Parameterization

Uses Open Parametric Hand (OPH) framework to generate structured parameter dictionaries:

- `Θ = fLLM(S, f)` where `S` is grammar and `f` is semantic requirements
- Grasp-type-influenced parameter selection
- Subset utilization of OPH template parameters

### Phase 3: Morphological Constraint Filtering

Enforces design rules from OPH framework and 3D printing best practices:

- Finger count validation (anthropomorphic and underactuated designs)
- Joint and link dimension checks
- Slenderness ratio analysis
- Overall finger length constraints
- Initial orientation validation
- Fabrication footprint optimization

### Phase 4: Diversity Strategy

Ensures meaningful design variation through:

- Variant-specific design rule prompting
- Deterministic bias injection (vs. stochastic sampling)
- Generation of multiple candidate designs

### Phase 5: LLM-Guided Ranking and Selection

**5.1 Evaluation and Ranking**

- **Semantic Alignment** (0-10): Language-driven task-design fit assessment
- **Size Compatibility** (0-10): Dimensional appropriateness scoring
- Composite ranking of all candidate designs

**5.2 Refinement Loop**

- Feedback-driven improvement of top-rated designs
- Prompt-level optimization with phase-specific backpropagation

## Project Structure

```
prosthetic_hand_pipeline/
│
├── main.py                          # Main entry point
│
├── phase1_task_analysis/
│   ├── llm_task_analysis.py         # LLM → functional JSON
│   ├── grammar_hand_design.py       # Grammar generation
│   └── validator.py                 # Combined validation
│
├── phase2_geometry_parameterization/
│   ├── parameter_generator.py       # Grammar + semantic → Θ
│   └── open_parametric_interface.py # OpenSCAD interface
│
├── phase3_morphology_filter/
│   └── constraint_checker.py        # Printability checks
│
├── phase4_diversity/
│   └── variant_generator.py         # Design diversity
│
├── phase5_ranking/
│   └── evaluator.py                 # Scoring and ranking
│
├── OpenSCAD/                        # OPH repository
│   ├── parameters.scad
│   ├── STLs/
│   └── ...
│
├── outputs/
│   ├── json/
│   ├── grammar/
│   ├── params/
│   └── stl/
│
├── requirements.txt
└── README.md
```

## Implementation Stack

| Phase                   | Technology                                     |
| ----------------------- | ---------------------------------------------- |
| LLM Task Analysis       | Python + OpenAI API (JSON mode)                |
| Grammar Design          | `lark` or custom rule dictionaries             |
| Validation              | Regex + heuristic rules                        |
| Parameterization        | OpenSCAD variable generation                   |
| Morphological Filtering | Python numeric thresholds                      |
| OpenSCAD Rendering      | Subprocess calls                               |
| Visualization           | `matplotlib` 3D / STL export (MeshLab/Blender) |
