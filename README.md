# Screen Region OCR Tool

A Python script that captures a screen region based on user-defined coordinates, saves it as an image, and optionally extracts text from the image using Optical Character Recognition (OCR).

## Features

- **Screen Region Capture**: Define a screen region by selecting the top-left and bottom-right corners using your mouse.
- **Image Saving**: The captured region is saved as a PNG image in the `img/` directory.
- **OCR Text Extraction**: Uses Tesseract OCR to extract text from the captured image and saves it to a `.txt` file in the `output/` directory.
- **Rich Console Interface**: Utilizes the `rich` library for a visually appealing and user-friendly console interface.

## Requirements

- Python 3.x
- Required Python packages:
  ```bash
  keyboard
  pyautogui
  pytesseract
  rich

## Installation

1) Clone the repository
2) Install the required dependencies
3) Install Tesseract OCR (https://github.com/tesseract-ocr/tesseract)
4) Ensure the Tesseract executable path is correctly set in the script:
```bash
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

## Usage
