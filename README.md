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