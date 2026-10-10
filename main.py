
import tkinter as tk
from tkinter import ttk
import webbrowser

REPOSITORY = "https://github.com/topcuogly/eyluul"

root = tk.Tk()
root.title("eyluul — Project Overview")
root.geometry("680x620")
root.minsize(580, 560)
root.configure(bg="#f7f8fa")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "App.TFrame",
    background="#f7f8fa",
)

style.configure(
    "Title.TLabel",
    background="#f7f8fa",
    foreground="#161b22",
    font=("Sans", 30, "bold"),
)

style.configure(
    "Subtitle.TLabel",
    background="#f7f8fa",
    foreground="#57606a",
    font=("Sans", 11),
)

style.configure(
    "Heading.TLabel",
    background="#f7f8fa",
    foreground="#24292f",
    font=("Sans", 12, "bold"),
)

style.configure(
    "Body.TLabel",
    background="#f7f8fa",
    foreground="#424a53",
    font=("Sans", 10),
)

style.configure(
    "Link.TButton",
    font=("Sans", 10),
    padding=(14, 9),
)

container = ttk.Frame(root, style="App.TFrame", padding=32)
container.pack(fill="both", expand=True)

ttk.Label(
    container,
    text="eyluul",
    style="Title.TLabel",
).pack(anchor="w")

ttk.Label(
    container,
    text="An experimental bilingual legal language model",
    style="Subtitle.TLabel",
).pack(anchor="w", pady=(0, 20))


def section(title, description):
    ttk.Label(
        container,
        text=title,
        style="Heading.TLabel",
    ).pack(anchor="w", pady=(14, 6))

    label = ttk.Label(
        container,
        text=description,
        style="Body.TLabel",
        justify="left",
        wraplength=590,
    )
    label.pack(anchor="w")


section(
    "OVERVIEW",
    "eyluul is an open-source research project focused on "
    "developing a small Turkish-English language model "
    "from scratch, with an emphasis on Turkish criminal law.",
)

section(
    "RESEARCH OBJECTIVES",
    "• Design and train a language model from scratch.\n"
    "• Investigate Turkish-English legal language modeling.\n"
    "• Identify relevant provisions of the Turkish Penal Code.\n"
    "• Evaluate offense elements in hypothetical legal cases.\n"
    "• Compare performance against classical NLP baselines.\n"
    "• Document experiments for reproducibility.",
)

section(
    "COMPUTATIONAL CONSTRAINTS",
    "Training and evaluation are designed around a single "
    "consumer-grade GPU: NVIDIA GeForce RTX 5060 (8 GB VRAM).",
)

section(
    "PROJECT STATUS",
    "Early development, repository initialized. "
    "Model architecture, datasets, and evaluation "
    "methodology are not yet finalized.",
)

ttk.Separator(container, orient="horizontal").pack(
    fill="x",
    pady=(22, 16),
)

footer = ttk.Frame(container, style="App.TFrame")
footer.pack(fill="x")

ttk.Label(
    footer,
    text="Open-source research project",
    style="Subtitle.TLabel",
).pack(side="left")

ttk.Button(
    footer,
    text="View on GitHub ↗",
    style="Link.TButton",
    command=lambda: webbrowser.open(REPOSITORY),
).pack(side="right")

root.mainloop()
