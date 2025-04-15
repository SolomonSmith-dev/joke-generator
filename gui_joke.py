import tkinter as tk  # GUI framework included with Python
from tkinter import messagebox  # For pop-up error dialogs
import requests

# === Function to fetch a joke from the API ===
def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        joke = response.json()

        # Update the text in the GUI
        setup_var.set(f"🃏 {joke['setup']}")
        punchline_var.set(f"😂 {joke['punchline']}")
    
    except requests.Timeout:
        messagebox.showwarning("Timeout", "⏰ The request timed out. Try again.")
    
    except requests.RequestException as e:
        messagebox.showerror("Error", f"❌ Failed to fetch joke:\n{e}")

# === Set up the main application window ===
root = tk.Tk()
root.title("Joke Generator 😂")
root.geometry("500x250")
root.resizable(False, False)

# === Variables to hold joke text ===
setup_var = tk.StringVar()
punchline_var = tk.StringVar()

# === Widgets (UI Elements) ===
title_label = tk.Label(root, text="Joke Generator", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

setup_label = tk.Label(root, textvariable=setup_var, wraplength=450, font=("Helvetica", 14))
setup_label.pack(pady=10)

punchline_label = tk.Label(root, textvariable=punchline_var, wraplength=450, font=("Helvetica", 14, "italic"))
punchline_label.pack(pady=10)

joke_button = tk.Button(root, text="Tell Me a Joke 🎭", font=("Helvetica", 12), command=fetch_joke)
joke_button.pack(pady=10)

# === Start the GUI event loop ===
root.mainloop()
