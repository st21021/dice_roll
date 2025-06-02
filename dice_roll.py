import tkinter as tk
import random as r

def gen_rand():
    '''Generate two random numbers and display with labels'''
    num1.set(r.randint(1,6))
    num2.set(r.randint(1,6))
    count.set(count.get()+1)
    if num1.get() == 6 and num2.get() == 6:
        lbl1.configure(bg="#44ff44")
        lbl2.configure(bg="#44ff44")
    else:
        lbl1.configure(bg="#ff4444")
        lbl2.configure(bg="#ff4444")

def close_window():
    '''Close the tk root window'''
    root.destroy()


root = tk.Tk()
root.title("Dice Roll")
root.rowconfigure([0, 1, 2], minsize=30)
root.columnconfigure([0, 1], minsize=150)

num1 = tk.IntVar(root, "")
num2 = tk.IntVar(root, "")
count = tk.IntVar(root, 0)

btn_quit = tk.Button(root, text="Quit", command=close_window)
btn_random = tk.Button(root, text="Random", command=gen_rand)

lbl1 = tk.Label(root, textvariable=num1, bg="#ff4444", fg="black")
lbl2 = tk.Label(root, textvariable=num2, bg="#ff4444", fg="black")

lbl_roll = tk.Label(root, text="Roll count =", justify="right")
lbl_count = tk.Label(root, textvariable=count, justify="left")

btn_quit.grid(row=0, column=0, sticky="NSWE", padx=10, pady=3)
btn_random.grid(row=0, column=1, sticky="NSWE", padx=10, pady=3)
lbl1.grid(row=1, column=0, sticky="NSWE", padx=10, pady=3)
lbl2.grid(row=1, column=1, sticky="NSWE", padx=10, pady=3)
lbl_roll.grid(row=2, column=0, sticky="E", padx=10, pady=3)
lbl_count.grid(row=2, column=1, sticky="W", padx=10, pady=3)

root.mainloop()