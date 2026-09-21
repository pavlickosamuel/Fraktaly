import tkinter as tk

window = tk.Tk()
window.title("Sierpinskeho trojuholník")
canvas = tk.Canvas(window, width=1000, height=1000, bg="lightblue")  
canvas.pack() 
def draw_carpet(a, x, y):
    if a > 10:
        canvas.create_rectangle(x, y, x + a, y+a, outline = "black")
        draw_carpet(a , x + a / 3, y)
        
draw_carpet (900, 50, 50)
window.mainloop()