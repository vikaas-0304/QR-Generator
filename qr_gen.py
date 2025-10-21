import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
)
from qrcode.image.styles.colormasks import SolidFillColorMask


# ---------- Utility: Convert Hex to RGB ----------
def hex_to_rgb(value):
    """Convert hex color (#rrggbb) to an (R, G, B) tuple."""
    value = value.strip()
    if value.startswith("#"):
        value = value[1:]
    if len(value) != 6:
        raise ValueError("Invalid hex color format")
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))


# ---------- QR Generator ----------
def generate_qr():
    url = url_entry.get().strip()
    eye_style_choice = eye_pattern.get()
    body_style_choice = body_pattern.get()
    fg_color = fg_color_var.get()
    bg_color = bg_color_var.get()

    if not url:
        messagebox.showwarning("Missing URL", "Please enter a URL.")
        return

    # Convert HEX → RGB tuples
    try:
        fg_color_rgb = hex_to_rgb(fg_color)
        bg_color_rgb = hex_to_rgb(bg_color)
    except Exception:
        messagebox.showerror("Invalid Color", "Please choose valid colors from palette.")
        return

    # Pattern maps
    eye_styles = {
        "square": SquareModuleDrawer(),
        "circle": CircleModuleDrawer(),
        "dotted": GappedSquareModuleDrawer(),
        "none": RoundedModuleDrawer(),
    }

    body_styles = {
        "default": SquareModuleDrawer(),
        "dotted": GappedSquareModuleDrawer(),
        "lines": RoundedModuleDrawer(),
    }

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=body_styles.get(body_style_choice, SquareModuleDrawer()),
            eye_drawer=eye_styles.get(eye_style_choice, SquareModuleDrawer()),
            color_mask=SolidFillColorMask(
                back_color=bg_color_rgb,
                front_color=fg_color_rgb,
            ),
        )

        img.save("fancy_qr.png")
        messagebox.showinfo("Success", "✅ QR Code generated as fancy_qr.png!")

    except Exception as e:
        messagebox.showerror("Error", f"QR generation failed:\n{e}")


# ---------- Color Picker Functions ----------
def pick_fg_color():
    color = colorchooser.askcolor(title="Choose QR Color")[1]
    if color:
        fg_color_var.set(color)
        fg_color_preview.config(bg=color)


def pick_bg_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        bg_color_var.set(color)
        bg_color_preview.config(bg=color)


# ---------- GUI ----------
root = tk.Tk()
root.title("🎨 Fancy QR Code Generator")
root.geometry("430x500")
root.resizable(False, False)

title = tk.Label(root, text="🎨 Fancy QR Code Generator", font=("Segoe UI", 14, "bold"))
title.pack(pady=10)

tk.Label(root, text="Enter URL:", font=("Segoe UI", 11)).pack(pady=5)
url_entry = tk.Entry(root, width=45, font=("Segoe UI", 10))
url_entry.pack(pady=5)

tk.Label(root, text="Select Eye Pattern:", font=("Segoe UI", 11)).pack(pady=5)
eye_pattern = ttk.Combobox(root, values=["square", "circle", "dotted", "none"], state="readonly")
eye_pattern.current(0)
eye_pattern.pack(pady=5)

tk.Label(root, text="Select Body Pattern:", font=("Segoe UI", 11)).pack(pady=5)
body_pattern = ttk.Combobox(root, values=["default", "dotted", "lines"], state="readonly")
body_pattern.current(0)
body_pattern.pack(pady=5)

# Foreground color
tk.Label(root, text="QR Body + Eye Color:", font=("Segoe UI", 11)).pack(pady=5)
fg_color_var = tk.StringVar(value="#000000")
fg_color_preview = tk.Label(root, bg="#000000", width=10, height=1, relief="ridge")
fg_color_preview.pack()
tk.Button(root, text="Pick QR Color", command=pick_fg_color).pack(pady=5)

# Background color
tk.Label(root, text="Background Color:", font=("Segoe UI", 11)).pack(pady=5)
bg_color_var = tk.StringVar(value="#ffffff")
bg_color_preview = tk.Label(root, bg="#ffffff", width=10, height=1, relief="ridge")
bg_color_preview.pack()
tk.Button(root, text="Pick Background Color", command=pick_bg_color).pack(pady=5)

tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 11, "bold"),
).pack(pady=20)

tk.Label(
    root,
    text="QR will be saved as 'fancy_qr.png' in this folder.",
    font=("Segoe UI", 9),
).pack(pady=5)

root.mainloop()
