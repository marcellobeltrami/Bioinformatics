import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog, QMessageBox
import main 

class CustomGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bioinformatics App")
        self.setGeometry(100, 100, 400, 300)

        self.file_path = None

        self.upload_button = QPushButton("Upload File", self)
        self.upload_button.clicked.connect(self.upload_file)
        self.upload_button.setGeometry(50, 50, 120, 30)

        self.confirm_button = QPushButton("Confirm Input", self)
        self.confirm_button.clicked.connect(self.confirm_input)
        self.confirm_button.setGeometry(200, 50, 120, 30)
        self.confirm_button.setEnabled(False)

        self.output_text = QTextEdit(self)
        self.output_text.setGeometry(50, 100, 300, 100)

        self.download_button = QPushButton("Download File", self)
        self.download_button.clicked.connect(self.download_file)
        self.download_button.setGeometry(150, 220, 120, 30)
        self.download_button.setEnabled(False)

    def upload_file(self):
        file_dialog = QFileDialog()
        self.file_path, _ = file_dialog.getOpenFileName(self, "Upload File", "", "Text files (*.txt);;All files (*.*)")

        if self.file_path:
            self.confirm_button.setEnabled(True)
            QMessageBox.information(self, "Upload Successful", "File uploaded successfully!")
        else:
            QMessageBox.warning(self, "Upload Failed", "No file selected.")

    def confirm_input(self):
        QMessageBox.information(self, "Input Confirmed", "Input confirmed and processing started!")
        self.process_input()

#add processes from main here 
    def process_input(self):
        try:
            with open(self.file_path, "r") as file:
                content = file.read()
                self.output_text.setText(content)
            self.download_button.setEnabled(True)
        
        except Exception as e:
            QMessageBox.critical(self, "Processing Error", f"An error occurred during processing:\n{str(e)}")

    def download_file(self):
        save_dialog = QFileDialog()
        save_path, _ = save_dialog.getSaveFileName(self, "Save File", "", "Text files (*.txt);;All files (*.*)")

        if save_path:
            try:
                # Implement your file download logic here
                # Use self.file_path to access the processed data and save it to the desired location
                QMessageBox.information(self, "Download Complete", "File downloaded successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Download Failed", f"An error occurred during download:\n{str(e)}")
        else:
            QMessageBox.warning(self, "Download Failed", "No save location selected.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomGUI()
    window.show()
    sys.exit(app.exec_())
