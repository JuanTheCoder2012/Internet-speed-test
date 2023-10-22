import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class InternetSpeedTester(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Internet Speed Tester')
        self.setGeometry(200, 200, 400, 200)

        self.download_label = QLabel('Download Speed: ')
        self.upload_label = QLabel('Upload Speed: ')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.download_label)
        self.layout.addWidget(self.upload_label)

        self.start_button = QPushButton('Start Test', self)
        self.start_button.clicked.connect(self.startTest)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def startTest(self):
        self.start_button.setEnabled(False)
        self.download_label.setText('Download Speed: Calculating...')
        self.upload_label.setText('Upload Speed: Calculating...')
        subprocess.Popen(["speedtest-cli", "--simple"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate(input=None)
        self.updateSpeeds()

    def updateSpeeds(self):
        try:
            result = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
            output = result.stdout.splitlines()

            if len(output) >= 2 and output[0].startswith("Download") and output[1].startswith("Upload"):
                download_speed = float(output[0].split()[1]) / 1_000_000  # Convert to Mbps
                upload_speed = float(output[1].split()[1]) / 1_000_000  # Convert to Mbps

                self.download_label.setText(f'Download Speed: {download_speed:.2f} Mbps')
                self.upload_label.setText(f'Upload Speed: {upload_speed:.2f} Mbps')
            else:
                raise Exception("Unexpected output format", output)

        except Exception as e:
            print(f"Error: {e}")
            self.download_label.setText('Download Speed: Error')
            self.upload_label.setText('Upload Speed: Error')
        
        self.start_button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InternetSpeedTester()
    window.show()
    sys.exit(app.exec_())
