# 🎙️ Jarvis – Your Personal Voice Assistant  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red)]()  

A lightweight **AI-powered voice assistant** built with Python that listens to your voice commands, talks back, and helps you with everyday tasks like opening apps, browsing websites, searching Wikipedia, and more! 🚀  

---

## ✨ Features  

✅ **Text-to-Speech (TTS)** – Speaks with natural voices using `pyttsx3`  
✅ **Speech Recognition** – Understands your commands via Google Speech Recognition  
✅ **Wikipedia Search** – Gives you quick 2-sentence summaries  
✅ **Web Shortcuts** – Opens Google, YouTube, Stack Overflow in your default browser  
✅ **App Launcher** – Open VS Code, WhatsApp, Edge (customizable)  
✅ **Time Updates** – Tells you the current time  
✅ **Smart Greetings** – Greets you according to the time of day  

---

## 📸 Demo  

Here’s a quick look at Jarvis in action:  

![Jarvis Demo](assets/demo.gif)  

*(To add this GIF: record your screen → convert to GIF → save it in `/assets/demo.gif` → commit and push.)*  

---

## 🛠️ Installation  

1️⃣ Clone the repo:  

```bash
git clone https://github.com/your-username/jarvis-assistant.git
cd jarvis-assistant
```

2️⃣ Install dependencies:  

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyaudio
```

⚠️ On Windows, if `pyaudio` fails:  

```bash
pip install pipwin
pipwin install pyaudio
```

3️⃣ Run the assistant:  

```bash
python jarvis.py
```

---

## 🎤 Voice Commands  

Here are some things you can say:  

- 🔍 **Wikipedia** → “Search Wikipedia for Python programming”  
- 🌐 **Websites** → “Open YouTube”, “Open Google”, “Open Stack Overflow”  
- 🕒 **Time** → “Tell me the time”  
- 🖥️ **Apps** → “Open WhatsApp”, “Open Code”, “Open Browser”  

---

## ⚙️ Customization  

- **Change Voice (male/female)**  
  ```python
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)  # try changing index
  ```

- **Change App Paths**  
  Update this in `jarvis.py`:  
  ```python
  codePath = "C:\\Users\\YourName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
  ```

---

## 🚀 Future Plans  

- Add GUI with Tkinter 🎨  
- Weather updates 🌦️  
- Send emails 📧  
- Play music 🎶  
- AI chatbot integration 🤖  

---

## 👩‍💻 Author  

**Ipshita Srivastava**  
💻 CSE Student | 🌐 Frontend Developer | 🤖 AI/ML Enthusiast  

📌 [LinkedIn](https://www.linkedin.com/in/ipshita-srivastvava) | [GitHub](https://github.com/Ipshita0101)  

---

✨ *If you like this project, don’t forget to ⭐ the repo!* ✨  
