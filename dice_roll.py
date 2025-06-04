import tkinter as tk
import random as r

RED = "#ff4444"
GREEN = "#44ff44"

class DiceRoll:

    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll")
        self.root.rowconfigure([0, 1, 2], minsize=30)
        self.root.columnconfigure([0, 1], minsize=150)

        self.num1 = tk.IntVar(root, "")
        self.num2 = tk.IntVar(root, "")
        self.count = tk.IntVar(root, 0)

        self.btn_quit = tk.Button(root, text="Quit", command=self.close_window)
        self.btn_random = tk.Button(root, text="Random", command=self.gen_rand)

        # Labels to display dice rolls
        self.lbl1 = tk.Label(root, textvariable=self.num1, bg=RED, fg="black")
        self.lbl2 = tk.Label(root, textvariable=self.num2, bg=RED, fg="black")

        # Labels to display the number of dice rolls
        self.lbl_roll = tk.Label(root, text="Roll count =", justify="right")
        self.lbl_count = tk.Label(root, textvariable=self.count, justify="left")

        # Add everything to the window using grid
        self.btn_quit.grid(row=0, column=0, sticky="NSWE", padx=10, pady=3)
        self.btn_random.grid(row=0, column=1, sticky="NSWE", padx=10, pady=3)
        self.lbl1.grid(row=1, column=0, sticky="NSWE", padx=10, pady=3)
        self.lbl2.grid(row=1, column=1, sticky="NSWE", padx=10, pady=3)
        self.lbl_roll.grid(row=2, column=0, sticky="E", padx=10, pady=3) # Right aligned
        self.lbl_count.grid(row=2, column=1, sticky="W", padx=10, pady=3) # Left aligned

    def gen_rand(self):
        '''Generate two random numbers and display with labels'''
        self.num1.set(r.randint(1,6))
        self.num2.set(r.randint(1,6))
        self.count.set(self.count.get()+1)
        if self.num1.get() == 6 and self.num2.get() == 6:
            # Set label background to green
            self.lbl1.configure(bg=RED)
            self.lbl2.configure(bg=RED)
        else:
            # Set label background to red
            self.lbl1.configure(bg=RED)
            self.lbl2.configure(bg=RED)


    def close_window(self):
        '''Close the tk root window'''
        self.root.destroy()

# Create window
master = tk.Tk()
app = DiceRoll(master)
master.mainloop()