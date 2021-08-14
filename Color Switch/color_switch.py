import tkinter as tk
import random

root = tk.Tk()
root.title('Color Switch')
root.geometry('500x500')

scores = []

red = tk.PhotoImage(file = 'Color Switch/red.png', width = 180, height = 180)
blue = tk.PhotoImage(file = 'Color Switch/blue.png', width = 180, height = 180)
yellow  = tk.PhotoImage(file = 'Color Switch/yellow.png', width = 180, height = 180)
green = tk.PhotoImage(file = 'Color Switch/green.png', width = 180, height = 180)

def main():
    score = len(scores)
    tricks = ['#00FF00', '#FF0000', '#FFBF00', '#0000FF']
    texc = random.choice(tricks)
    colors = ['Red', 'Green', 'Yellow', 'Blue']
    pick = random.choice(colors)
    def redb():
        for widget in root.winfo_children():
            widget.destroy()
        box = 'Red'
        if box == pick:
            scores.append('yes')
            main()  
        else:
            label = tk.Label(root, text = 'You lost')
            label.grid()
            final = 'Your score was:', score
            label = tk.Label(root, text = final)
            label.grid()
    def blueb():
        for widget in root.winfo_children():
            widget.destroy()
        box = 'Blue'
        if box == pick:
            scores.append('yes')
            main()
        else:
            label = tk.Label(root, text = 'You lost')
            label.grid()
            final = 'Your score was:', score
            label = tk.Label(root, text = final)
            label.grid()
    def yelb():
        for widget in root.winfo_children():
            widget.destroy()
        box = 'Yellow'
        if box == pick:
            scores.append('yes')
            main()
        else:
            label = tk.Label(root, text = 'You lost')
            label.grid()
            final = 'Your score was:', score
            label = tk.Label(root, text = final)
            label.grid()
    def greenb():
        for widget in root.winfo_children():
            widget.destroy()
        box = 'Green'
        if box == pick:
            scores.append('yes')
            main()
        else:
            label = tk.Label(root, text = 'You lost')
            label.grid()
            final = 'Your score was:', score
            label = tk.Label(root, text = final)
            label.grid()
    redbutton = tk.Button(root, image = red, command = redb, borderwidth = 0)
    bluebutton = tk.Button(root, image = blue, command = blueb, borderwidth = 0)
    yelbutton = tk.Button(root, image = yellow, command = yelb, borderwidth = 0)
    greenbutton = tk.Button(root, image = green, command = greenb, borderwidth = 0)
    if pick == 'Red':
        label = tk.Label(root, text = pick, fg = texc)
        label.grid()
        redbutton.grid(row = 1, column = 1)
        bluebutton.grid(row = 2, column = 1)
        yelbutton.grid(row = 1, column = 2)
        greenbutton.grid(row = 2, column = 2)
        score_text = 'Score:', score
        label = tk.Label(root, text = score_text)
        label.grid()
    elif pick == 'Blue':
        label = tk.Label(root, text = pick, fg = texc)
        label.grid()
        redbutton.grid(row = 1, column = 1)
        bluebutton.grid(row = 2, column = 1)
        yelbutton.grid(row = 1, column = 2)
        greenbutton.grid(row = 2, column = 2)
        score_text = 'Score:', score
        label = tk.Label(root, text = score_text)
        label.grid()
    elif pick == 'Yellow':
        label = tk.Label(root, text = pick, fg = texc)
        label.grid()
        redbutton.grid(row = 1, column = 1)
        bluebutton.grid(row = 2, column = 1)
        yelbutton.grid(row = 1, column = 2)
        greenbutton.grid(row = 2, column = 2)
        score_text = 'Score:', score
        label = tk.Label(root, text = score_text)
        label.grid()
    elif pick == 'Green':
        label = tk.Label(root, text = pick, fg = texc)
        label.grid()
        redbutton.grid(row = 1, column = 1)
        bluebutton.grid(row = 2, column = 1)
        yelbutton.grid(row = 1, column = 2)
        greenbutton.grid(row = 2, column = 2)
        score_text = 'Score:', score
        label = tk.Label(root, text = score_text)
        label.grid()

main()
root.mainloop()