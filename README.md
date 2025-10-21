## QR-Generator
A Python-based GUI tool to generate custom QR codes from URLs. It allows choosing eye patterns (square, circle, dotted, none) and body styles (default, dotted, lines). Users can also select custom colors for the QR body and background using a color palette. The generated QR is saved as fancy_qr.png automatically.

# 🎨 Fancy QR Code Generator (Python GUI Tool)

A simple **Python-based GUI tool** to generate **custom QR codes** from any URL.  
It provides stylish customization options like **eye patterns**, **body styles**, and **color themes** using a **Tkinter interface**.

---

## 🧩 Overview

This tool helps you easily create visually appealing QR codes with options to:
- Choose **eye patterns** – Square, Circle, Dotted, or None  
- Choose **body patterns** – Default, Dotted, or Lines  
- Customize **QR and background colors** using a color palette  
- Save the final QR automatically as **`fancy_qr.png`**

---

## ⚙️ Requirements

Make sure Python (3.8 or later) is installed.  
Then install these libraries:

```bash
pip install qrcode[pil]
pip install pillow
```

---

## 🚀 Installation & Usage

Clone this repository

```bash
git clone https://github.com/vikaas-0304/QR-Generator.git
cd QR-Generator
```

Run the tool
```bash
python qr_gen.py
```

# How to use

- Enter the URL or text you want to encode
- Select Eye Pattern and Body Pattern
- Pick QR color and Background color using the color picker
- Click "Generate QR Code" to create and save it as fancy_qr.png

