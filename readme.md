# Fun Python Projects

This repository contains two fun Python projects: `monkeytype-automate` and `auto-insta-scroller`.

## monkeytype-automate

This project automates the typing of text extracted from a screenshot using OCR (Optical Character Recognition).

### Requirements

- Python 3.x
- `pyautogui` library
- `pytesseract` library
- `opencv-python` library
- Tesseract OCR installed on your system

### Installation

1. Install the required Python libraries:
    ```bash
    pip install pyautogui pytesseract opencv-python
    ```

2. Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

### Usage

1. Run the script:
    ```bash
    python monkeytype.py
    ```

2. The script will take a screenshot of a specific region, extract text using OCR, and type it out automatically.

## auto-insta-scroller

This project automates scrolling on Instagram by pressing the down arrow key at regular intervals.

### Requirements

- Python 3.x
- `pyautogui` library

### Installation

1. Install the required Python library:
    ```bash
    pip install pyautogui
    ```

### Usage

1. Run the script:
    ```bash
    python autoscroll.py
    ```

2. The script will wait for 15 seconds and then press the down arrow key to scroll down.
