def build_prompt(summary, labs, radiology, guideline_context):

    prompt = f"""
You are an AI physician assistant.

PATIENT SUMMARY
---------------
{summary}

LAB RESULTS
-----------
{labs}

RADIOLOGY REPORT
----------------
{radiology}

GUIDELINE EVIDENCE
------------------
{guideline_context}

TASK
----
Analyze the patient's condition.

Consider:

1. Current symptoms
2. Historical visit patterns
3. Lab abnormalities
4. Imaging results
5. Guideline recommendations

Provide:

1. Clinical Summary
2. Possible Diagnosis
3. Recommended Next Steps
4. Guideline Evidence Used

Be concise and clinically accurate.
"""

    return prompt
