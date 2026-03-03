import tkinter as tk
import random

word_bank = {
    "Technology": [
        "python", "javascript", "database", "algorithm", "compiler",
        "processor", "encryption", "network", "firewall", "backend",
        "frontend", "hardware", "software", "cybersecurity", "blockchain",
        "debugging", "interface", "protocol", "bandwidth", "cloud"
    ],
    "Electronics": [
        "resistor", "capacitor", "inductor", "diode", "transistor",
        "voltage", "current", "frequency", "amplifier", "oscillator",
        "multiplexer", "encoder", "decoder",
        "flipflop", "register", "counter", "logicgate",
        "fpga", "vlsi", "verilog", "mosfet", "circuit"
    ],
    "Science": [
        "gravity", "atom", "molecule", "photosynthesis",
        "evolution", "quantum", "relativity", "neutron",
        "electron", "proton", "thermodynamics",
        "biology", "chemistry", "physics", "ecosystem",
        "planet", "galaxy", "telescope", "microscope"
    ]
}


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e2f")

        self.word = ""
        self.hint = ""
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_wrong = 6

        self.setup_ui()
        self.start_game()

    def setup_ui(self):
        self.title_label = tk.Label(
            self.root,
            text="🎮 Hangman Game",
            font=("Segoe UI", 22, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.title_label.pack(pady=10)

        self.canvas = tk.Canvas(
            self.root,
            width=300,
            height=250,
            bg="#1e1e2f",
            highlightthickness=0
        )
        self.canvas.pack()

        self.hint_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 12),
            bg="#1e1e2f",
            fg="#00ffcc"
        )
        self.hint_label.pack(pady=5)

        self.word_label = tk.Label(
            self.root,
            text="",
            font=("Consolas", 24, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.word_label.pack(pady=15)

        self.entry = tk.Entry(self.root, font=("Segoe UI", 16), justify="center", width=5)
        self.entry.pack()

        self.guess_button = tk.Button(
            self.root,
            text="Guess",
            font=("Segoe UI", 12, "bold"),
            bg="#ffcc00",
            command=self.guess_letter
        )
        self.guess_button.pack(pady=10)

        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 12, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.status_label.pack()

        self.restart_button = tk.Button(
            self.root,
            text="Restart",
            command=self.start_game
        )
        self.restart_button.pack(pady=10)

    def start_game(self):
        category = random.choice(list(word_bank.keys()))
        self.word = random.choice(word_bank[category])
        self.hint = f"Category: {category}"

        self.guessed_letters = []
        self.wrong_guesses = 0

        self.status_label.config(text="", fg="white")
        self.hint_label.config(text=self.hint)
        self.entry.delete(0, tk.END)

        self.canvas.delete("all")
        self.draw_base()
        self.update_display()

    def update_display(self):
        display = " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.word
        )
        self.word_label.config(text=display)

        if "_" not in display:
            self.status_label.config(text="🎉 You Won!", fg="#00ff00")

    def guess_letter(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not letter or letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.wrong_guesses += 1
            self.animate_draw(self.wrong_guesses)

        self.update_display()

        if self.wrong_guesses >= self.max_wrong:
            self.status_label.config(
                text=f"💀 Game Over! Word was: {self.word}",
                fg="red"
            )

    def draw_base(self):
        self.canvas.create_line(20, 230, 280, 230, fill="white", width=3)
        self.canvas.create_line(70, 230, 70, 30, fill="white", width=3)
        self.canvas.create_line(70, 30, 170, 30, fill="white", width=3)
        self.canvas.create_line(170, 30, 170, 50, fill="white", width=3)

    def animate_draw(self, step):
        parts = [
            lambda: self.canvas.create_oval(150, 50, 190, 90, outline="white", width=3),
            lambda: self.canvas.create_line(170, 90, 170, 150, fill="white", width=3),
            lambda: self.canvas.create_line(170, 110, 140, 130, fill="white", width=3),
            lambda: self.canvas.create_line(170, 110, 200, 130, fill="white", width=3),
            lambda: self.canvas.create_line(170, 150, 140, 190, fill="white", width=3),
            lambda: self.canvas.create_line(170, 150, 200, 190, fill="white", width=3),
        ]

        if step <= len(parts):
            self.root.after(200, parts[step - 1])


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()