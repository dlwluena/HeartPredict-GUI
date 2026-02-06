import sys
import numpy as np
import pickle
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLineEdit, QPushButton, QLabel, QMessageBox, QFrame, QScrollArea)
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt
from tensorflow.keras.models import load_model

# MODERN MEDICAL THEME (QSS)
STYLE_SHEET = """
QWidget {
    background-color: #f0f2f5;
    font-family: 'Segoe UI', Arial;
}
QFrame#InputCard {
    background-color: white;
    border-radius: 15px;
    border: 1px solid #dcdfe6;
    padding: 10px;
}
QLineEdit {
    background-color: #f4f7f9;
    border: 1px solid #ced4da;
    border-radius: 8px;
    padding: 10px;
    font-size: 14px;
    color: #333;
}
QLineEdit:focus {
    border: 2px solid #4a90e2;
}
QPushButton#DiagnoseBtn {
    background-color: #4a90e2;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 15px;
    margin-top: 10px;
}
QPushButton#DiagnoseBtn:hover {
    background-color: #357abd;
}
QLabel#TitleLabel {
    color: #2c3e50;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
QLabel#RangeLabel {
    font-size: 11px;
    color: #7f8c8d;
}
"""

class SweetHeartApp(QWidget):
    def __init__(self):
        super().__init__()
        # Load assets
        self.model = load_model('heart_model.keras')
        with open('scaler.pkl', 'rb') as f:
            self.scaler = pickle.load(f)
        self.initUI()

    def create_input_card(self, label_text, range_text):
        card = QFrame()
        card.setObjectName("InputCard")
        layout = QVBoxLayout(card)
        
        header = QHBoxLayout()
        title = QLabel(label_text)
        title.setStyleSheet("font-weight: 600; color: #34495e;")
        info = QLabel(range_text)
        info.setObjectName("RangeLabel")
        header.addWidget(title)
        header.addStretch()
        header.addWidget(info)
        
        entry = QLineEdit()
        layout.addLayout(header)
        layout.addWidget(entry)
        return card, entry

    def initUI(self):
        self.setStyleSheet(STYLE_SHEET)
        self.setWindowTitle('HeartExpert AI Dashboard')
        self.setFixedSize(480, 750)
        
        main_layout = QVBoxLayout(self)
        
        # Header Section
        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)
        title = QLabel("HeartHealth Predictor")
        title.setObjectName("TitleLabel")
        title.setAlignment(Qt.AlignCenter)
        subtitle = QLabel("AI-Powered Cardiovascular Risk Assessment")
        subtitle.setStyleSheet("color: #95a5a6; font-size: 12px;")
        subtitle.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        main_layout.addWidget(header_frame)

        # Scrollable Inputs
        scroll = QScrollArea()
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(12)
        
        self.inputs = {}
        features = [
            ('Age', 'age', '29-77'), ('Sex', 'sex', '1:M, 0:F'), ('Chest Pain', 'cp', '1-4'),
            ('Rest Blood Pressure', 'trestbps', '94-200'), ('Cholestoral', 'chol', '126-564'),
            ('Fasting Blood Sugar', 'fbs', '1:Y, 0:N'), ('Rest ECG', 'restecg', '0-2'),
            ('Max Heart Rate', 'thalach', '71-202'), ('Exercise Angina', 'exang', '1:Y, 0:N'),
            ('Oldpeak', 'oldpeak', '0.0-6.2'), ('ST Slope', 'slope', '1-3'),
            ('Vessels (CA)', 'ca', '0-3'), ('Thal Result', 'thal', '3, 6, 7')
        ]

        for label, key, r_text in features:
            card, entry = self.create_input_card(label, r_text)
            self.inputs[key] = entry
            scroll_layout.addWidget(card)

        scroll.setWidget(scroll_content)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        main_layout.addWidget(scroll)

        # Action Button
        self.btn = QPushButton('ANALYZE PATIENT')
        self.btn.setObjectName("DiagnoseBtn")
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.run_prediction)
        main_layout.addWidget(self.btn)

        self.result_display = QLabel("Waiting for input...")
        self.result_display.setAlignment(Qt.AlignCenter)
        self.result_display.setStyleSheet("font-size: 16px; padding: 15px; border-radius: 10px; background: white; border: 1px solid #dcdfe6;")
        main_layout.addWidget(self.result_display)

    def run_prediction(self):
        try:
            # All inputs must be numbers
            data = [float(self.inputs[k].text()) for k in ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
            scaled = self.scaler.transform([data])
            prob = self.model.predict(scaled, verbose=0)[0][0]

            if prob > 0.5:
                self.result_display.setText(f"RISK DETECTED: {prob*100:.1f}%")
                self.result_display.setStyleSheet("background: #f8d7da; color: #721c24; font-weight: bold; border: 1px solid #f5c6cb;")
            else:
                self.result_display.setText(f"CONDITION NORMAL: {prob*100:.1f}%")
                self.result_display.setStyleSheet("background: #d4edda; color: #155724; font-weight: bold; border: 1px solid #c3e6cb;")
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please ensure all fields are filled with numbers.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SweetHeartApp()
    ex.show()
    sys.exit(app.exec())