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
        
        