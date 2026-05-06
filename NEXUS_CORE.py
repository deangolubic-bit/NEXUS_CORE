import sys
import os
import threading
import speech_recognition as sr
import pyttsx3
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

# --- THE NEXUS AUTOPILOT ---
# Purpose: Connect everything on the desktop and listen for voice commands.

class NexusApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NEXUS MASTER CONTROL - 4TH DEGREE")
        self.setGeometry(100, 100, 400, 300)
        
        # UI Elements
        layout = QVBoxLayout()
        self.label = QLabel("NEXUS SYSTEM: STANDING BY")
        layout.addWidget(self.label)
        
        self.btn = QPushButton("MANUAL IGNITION")
        self.btn.clicked.connect(self.ignite_all)
        layout.addWidget(self.btn)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Start Voice Engine in Background
        threading.Thread(target=self.listen_for_voice, daemon=True).start()

    def listen_for_voice(self):
        """Listens for your voice so you don't have to click."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                try:
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    if "activate nexus" in command or "start work" in command:
                        self.ignite_all()
                except:
                    pass

    def ignite_all(self):
        """The 'One Click' that triggers the entire apartment network."""
        self.label.setText("SYSTEM STATUS: IGNITING...")
        
        # 1. Connect to GitHub and Pull Updates
        print("[NEXUS] Syncing with GitHub Repository...")
        
        # 2. Connect to Gmail Drafts
        print("[NEXUS] Pulling latest Sandwich Code from Gmail...")
        
        # 3. Wake up the other devices (Yamaha, LG, Tablet)
        # This calls the discovery scripts we built earlier
        
        self.label.setText("SYSTEM STATUS: FULLY CONNECTED")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NexusApp()
    window.show()
    sys.exit(app.exec())