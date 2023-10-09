import threading
import tkinter as tk
from tkinter import ttk
import speedtest

class InternetSpeedTester(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Internet Speed Tester")
        self.geometry("400x200")
        self.speedtester = speedtest.Speedtest()

        self.download_label = ttk.Label(self, text="Download Speed: ")
        self.download_label.pack(pady=10)

        self.upload_label = ttk.Label(self, text="Upload Speed: ")
        self.upload_label.pack(pady=10)

        self.start_button = ttk.Button(self, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=20)

    def start_test(self):
        self.start_button.config(state="disabled")
        self.download_label.config(text="Download Speed: Calculating...")
        self.upload_label.config(text="Upload Speed: Calculating...")

        # Start the speed test in a separate thread
        thread = threading.Thread(target=self.run_speed_test)
        thread.start()

    def run_speed_test(self):
        download_speed = self.speedtester.download() / 1_000_000  # Convert to Mbps
        upload_speed = self.speedtester.upload() / 1_000_000  # Convert to Mbps

        # Update UI with results
        self.download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        self.upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
        
        # Enable the start button after the test is completed
        self.start_button.config(state="normal")


if __name__ == "__main__":
    app = InternetSpeedTester()
    app.mainloop()
