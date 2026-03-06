import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QLabel,
    QComboBox
)

from scripts.emr_loader import load_patients, build_patient_summary
from scripts.clinical_data_loader import load_radiology, load_labs
from scripts.rag_engine import retrieve
from scripts.clinical_prompt import build_prompt
from scripts.llm_engine import generate


class AssistantUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Physician Assistant")
        self.resize(800,600)

        self.patients = load_patients()

        self.selector = QComboBox()

        for p in self.patients:
            self.selector.addItem(p["name"])

        self.summary_label = QLabel("Patient Summary")

        self.summary_box = QTextEdit()
        self.summary_box.setReadOnly(True)

        self.result_label = QLabel("AI Recommendation")

        self.result_box = QTextEdit()

        self.btn = QPushButton("Generate Clinical Recommendation")

        self.btn.clicked.connect(self.run_ai)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Select Patient"))
        layout.addWidget(self.selector)

        layout.addWidget(self.summary_label)
        layout.addWidget(self.summary_box)

        layout.addWidget(self.btn)

        layout.addWidget(self.result_label)
        layout.addWidget(self.result_box)

        self.setLayout(layout)


    def run_ai(self):

        patient = self.patients[self.selector.currentIndex()]

        summary = build_patient_summary(patient)

        patient_id = patient["file_id"]


        labs = load_labs(patient_id)
        radiology = load_radiology(patient_id)


        guideline_context = retrieve(summary)

        prompt = build_prompt(summary, labs, radiology, guideline_context)

        result = generate(prompt)

        self.summary_box.setText(summary)

        self.result_box.setText(result)


app = QApplication(sys.argv)

window = AssistantUI()

window.show()

sys.exit(app.exec())

