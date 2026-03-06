import os

def find_radiology_file(patient_id):
    """
    Searches radiology folder for any imaging report matching
    CT, MRI, Xray, or other modality patterns for the patient.
    """
    radiology_folder = "radiology"

    candidates = []
    for file in os.listdir(radiology_folder):
        # common radiology prefixes
        if file.startswith(patient_id + "_"):
            candidates.append(file)

    # sort deterministically so CT > MRI > Xray
    candidates.sort()
    return candidates[0] if candidates else None


def load_radiology(patient_id):

    file = find_radiology_file(patient_id)

    if not file:
        return f"No radiology report found for {patient_id}"

    path = os.path.join("radiology", file)

    with open(path) as f:
        return f.read()


def find_lab_file(patient_id):
    """
    Searches labs folder for any matching pattern (e.g. patient_1, patient_1_blood, etc.)
    """
    labs_folder = "labs"
    candidates = []
    for file in os.listdir(labs_folder):
        if file.startswith(patient_id + "_"):
            candidates.append(file)
    candidates.sort()
    return candidates[0] if candidates else None


def load_labs(patient_id):

    file = find_lab_file(patient_id)

    if not file:
        return f"No lab results found for {patient_id}"

    path = os.path.join("labs", file)

    with open(path) as f:
        return f.read()

