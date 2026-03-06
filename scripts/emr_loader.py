import json
import os


def load_patients():

    patients = []

    emr_folder = "emr"

    files = sorted(os.listdir(emr_folder))

    for file in files:

        if file.endswith(".json"):

            path = os.path.join(emr_folder, file)

            with open(path) as f:
                patient = json.load(f)

                patient["file_id"] = file.replace(".json","")

                patients.append(patient)

    return patients


def build_patient_summary(patient):

    summary = f"""
Patient: {patient['name']}
Age: {patient['age']}
Sex: {patient['sex']}

Conditions:
{", ".join(patient['conditions'])}

Medications:
{", ".join(patient['medications'])}

Current Visit Reason:
{patient['visit_reason']}
"""

    # Add visit history if present
    if "visit_history" in patient:

        summary += "\nPrevious Clinical Visits:\n"

        for visit in patient["visit_history"]:

            summary += f"""
Date: {visit['date']}
Chief Complaint: {visit['chief_complaint']}
Physician Notes: {visit['physician_notes']}
"""

    return summary


