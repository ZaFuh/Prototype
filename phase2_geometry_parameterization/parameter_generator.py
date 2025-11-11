#Maps grammar + semantics to numerical design params.
# converts grammar + semantic data → Θ dictionary


def generate_parameters(grammar, requirements):
    grasp = requirements.get("grasp_type", "fine")
    if grasp == "force":
        return {"finger_length": 55, "joint_diameter": 12, "palm_width": 85}
    elif grasp == "tool":
        return {"finger_length": 65, "joint_diameter": 10, "palm_width": 90}
    else:
        return {"finger_length": 45, "joint_diameter": 8, "palm_width": 70}
