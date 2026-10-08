# Keyboard Sound Effects

Lightweight Python application that play gunshots or typewriter sound effects with every click on the keyboard.
It is very good for annoying someone or playing it in a cafe.

---

## Features

- **Real-time Audio Feedback:** Zero-latency sound response using `pynput` and `pygame.mixer`
- **Multiple Sound Modes:"** Switch between different themes
  - **Gunshot Mode:** (`CTRL + 2`) - Gunshot sound with reload sound on `Enter`
  - **Typewriter Mode:** (`CTRL + 3`) - Classic mechanical typewriter  with bell chime on `Enter`
- **Toggle Mute Key:** Instant mute/unmute audio with `CTRL + 1`
- **Smart Key Handling:** No sound while key combination with `CTRL`

--- 

## Requirements


- Python 3.8 or higher
- pynput
- pygame

---

## Installation(Cross-Platform)

### 1. Clone the Repository

```bash
git clone https://github.com/soskoski/Keyboard-Sound.git
```

```bash
cd keyboard-sound
```

### 2. Set Up Virtual Environment

**Windows:**
```DOS
python -m venv venv
venv\Scripts\activate
```
**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Two options:

```bash
pip install pynput pygame
```
or

```bash
pip install -r requirements.txt
```

### 4. Run the Application and enjoy

```bash
python keyboard.py
```

