# 🔔 Reminder Remix

> **A customizable reminder app with live countdowns, video backgrounds, and audio alerts — all in one desktop experience.**

---

## 📌 Overview

**Reminder Remix** is a feature-rich desktop reminder application built with Python. It combines a clean **Tkinter UI** with real-time countdown logic, **OpenCV-powered video backgrounds**, and **Pygame audio alerts** to deliver reminders that are hard to miss and easy to set up.

Whether you need a quick timer or a fully personalized reminder experience, Reminder Remix gives you full control over time, visuals, and sound.

---

## ✨ Features

- ⏱️ **Flexible Time Input** — Set reminders using HH:MM:SS format for precise countdown control
- 🔢 **Real-Time Countdown** — Live countdown logic that updates every second until the alert triggers
- 🎬 **OpenCV Video Backgrounds** — Dynamic video backgrounds rendered using OpenCV for a rich visual experience
- 🔊 **Custom Audio Alerts** — Personalized sound notifications powered by Pygame
- 🖥️ **Clean Tkinter UI** — Simple, intuitive desktop interface with smooth media playback integration
- 🎨 **Fully Customizable** — Bring your own video and audio files to personalize every reminder

---

## 🛠️ Tech Stack

| Layer        | Technology                      |
|--------------|---------------------------------|
| UI           | Python, Tkinter                 |
| Video        | OpenCV (cv2)                    |
| Audio        | Pygame                          |
| Logic        | Python datetime / threading     |

---

## 📁 Project Structure

```
Reminder-Remix/
├── main.py                 # Application entry point
├── countdown.py            # Countdown timer logic
├── media/
│   ├── background.mp4      # Video background file
│   └── alert.mp3           # Custom audio alert
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/rahulachari/Reminder-Remix.git
cd Reminder-Remix
```

**2. Create and activate a virtual environment** *(recommended)*

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your media files**

Place your video file and audio alert inside the `media/` directory.

**5. Run the app**

```bash
python main.py
```

---

## 🎮 How to Use

1. Launch the app with `python main.py`
2. Enter your desired time in **HH:MM:SS** format
3. Hit **Start** — the countdown begins with your video background playing
4. When the timer hits zero, your custom audio alert fires automatically

---

## 🔧 Dependencies

Install all dependencies with:

```bash
pip install -r requirements.txt
```

| Package          | Purpose                        |
|------------------|--------------------------------|
| opencv-python    | Video background rendering     |
| pygame           | Audio alert playback           |
| tkinter          | Desktop UI (built into Python) |

---

## 🔮 Roadmap

- [ ] Multiple simultaneous reminders
- [ ] System tray support
- [ ] Recurring reminder schedules
- [ ] Reminder history log
- [ ] Executable (.exe) build for Windows

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Rahul Achari**  
GitHub: [github.com/rahulachari](https://github.com/rahulachari)

---

> *"Never miss a moment — Reminder Remix keeps you on track."*
