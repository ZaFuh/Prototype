# checks 3D printability + OPH constraints

def check_constraints(params):
    if not (3 <= params["joint_diameter"] <= 15):
        return False, "Joint diameter out of range."
    if not (30 <= params["finger_length"] <= 80):
        return False, "Finger length out of range."
    return True, "Parameters acceptable."
