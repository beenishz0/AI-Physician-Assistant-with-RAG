# AI-Physician-Assistant-with-RAG
An AI system that integrates electronic medical records (EMR) with local large language models (LLMs) to provide clinical decision support. The system processes patient historical charts, lab results, and multi-modal radiology reports (CT, MRI, X-ray) to generate evidence-based recommendations.
Leveraging a retrieval-augmented generation (RAG) framework, the AI retrieves relevant guideline information, combines it with patient-specific data, and outputs recommendations via a desktop interface using PyQt6. The PoC demonstrates offline capability on an desktop Linux PC system, achieving a realistic simulation of EMR-assisted clinical reasoning. Results indicate that the system can summarize patient histories, interpret multiple data types, and provide guideline-aligned recommendations, highlighting the potential for localized AI-based clinical support.

# Folder Structure Example:
    physician_assistant_rag/
    ├── emr/                # Patient JSON files
    ├── labs/               # Lab results
    ├── radiology/          # CT, MRI, X-ray reports
    ├── knowledge_base/     # Guidelines
    ├── vectordb/           # FAISS vector index
    ├── scripts/            # Data loaders, RAG, LLM interface
    └── ui/                 # PyQt6 GUI

# Example Output – Patient “Buzz Lightyear”
Patient Summary:
Patient: Buzz Lightyear
Age: 30
Sex: Female

Conditions:
None

Medications:
Vitamins

Current Visit Reason:
Severe headache on left side near temporal region

Previous Clinical Visits:

Date: 2019-01-28
Chief Complaint: Severe one sided headache
Physician Notes: Patient reports right after a flu started having severe headache on left side of the head. Occurs randomly throughout the day, with many episodes each lasting 2-3 minutes. Level 9 pain. No vision changes, no family history of migraine. Advised likely cluster headaches, recommended pure oxygen which helped and use of rizatriptan.

Date: 2023-05-20
Chief Complaint: Headache
Physician Notes: Severe one sided headaches on left side. Previous CT was normal. Recommended continue using pure oxygen and rizatriptan as it helped. Ordered labs and MRI.
AI Recommendation:
CLINICAL SUMMARY
----------------
Patient Buzz Lightyear is a 30-year-old female with no significant medical history who presents with severe, one-sided headaches on the left side near the temporal region. The pain is described as pulsating or throbbing in quality and has a moderate to severe intensity. The headaches worsen with routine physical activity and last between 4 and 72 hours.

The patient previously experienced similar symptoms following a flu episode, which were diagnosed as likely cluster headaches. She was advised to use pure oxygen and rizatriptan for symptomatic relief. A recent MRI brain scan showed no evidence of acute infarct, intracranial hemorrhage, or mass effect. Mucous retention cysts were noted in the left maxillary and sphenoid sinuses.

POSSIBLE DIAGNOSIS
------------------
Based on the patient's symptoms and imaging results, it is most likely that she continues to experience cluster headaches. However, given the persistence of her symptoms despite treatment, alternative diagnoses such as migraine or tension-type headache should be considered. Further evaluation by a neurologist may be necessary for definitive diagnosis.

RECOMMENDED NEXT STEPS
----------------------
1. Neurology consultation for further evaluation and potential alternative treatment options.
2. Continue use of pure oxygen and rizatriptan as needed for symptomatic relief.
3. Consider trial of other migraine preventative medications, such as propranolol or topiramate.
4. Monitor for any new symptoms or changes in headache pattern.

GUIDELINE EVIDENCE
