def detect_red_flags(patient):

    warnings = []

    visit_reason = patient["visit_reason"].lower()

    # Stroke indicators
    if "weakness" in visit_reason or "slurred speech" in visit_reason:
        warnings.append("Possible Stroke Symptoms Detected")

    # Meningitis indicators
    if "fever" in visit_reason and "neck stiffness" in visit_reason:
        warnings.append("Possible Meningitis Symptoms Detected")

    # Severe headache red flag
    if "worst headache" in visit_reason:
        warnings.append("Possible Subarachnoid Hemorrhage")

    return warnings

