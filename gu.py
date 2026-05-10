import tkinter as tk
import threading

class JarvisGUI:
    def __init__(self, root, start_callback, stop_callback):
        self.root = root
        self.root.title("Jarvis - Voice Assistant")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.status_var = tk.StringVar(value="Status: Idle")

        tk.Label(root, text="Heard:", font=("Arial", 12)).pack(pady=5)
        self.transcription_box = tk.Text(root, height=5, width=45)
        self.transcription_box.pack(pady=5)

        tk.Label(root, text="Jarvis says:", font=("Arial", 12)).pack(pady=5)
        self.response_box = tk.Label(root, text="", wraplength=350, font=("Arial", 10), justify="left")
        self.response_box.pack(pady=5)

        tk.Label(root, textvariable=self.status_var).pack(pady=5)

        tk.Button(root, text="Start Listening", command=lambda: threading.Thread(target=start_callback, daemon=True).start()).pack(pady=10)
        tk.Button(root, text="Stop Listening", command=stop_callback).pack(pady=5)

    def update_transcription(self, text):
        self.transcription_box.delete(1.0, tk.END)
        self.transcription_box.insert(tk.END, text)

    def update_jarvis_response(self, text):
        self.response_box.config(text=text)

    def set_status(self, text):
        self.status_var.set(text)
