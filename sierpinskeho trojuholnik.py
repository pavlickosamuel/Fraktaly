import tkinter as tk
 
window = tk.Tk()
window.title("Sierpinskeho trojuholník")
canvas = tk.Canvas(window, width=1000, height=1000, bg="lightblue")  
canvas.pack() 
def draw_triangle(a, x, y):
    if a > 10:
        canvas.create_line(x, y, x + a, y, fill = "black")
        canvas.create_line(x, y, x + a / 2, y - (a ** 2 - a ** 2 / 4) ** 0.5, fill = "black")
        canvas.create_line(x + a, y, x + a / 2, y - (a ** 2 - a ** 2 / 4) ** 0.5, fill = "black")
        draw_triangle(a / 2, x, y)
        draw_triangle(a / 2, x + a / 2, y)
        draw_triangle(a / 2, x + a / 4, y - (a ** 2 - a ** 2 / 4) ** 0.5 / 2)

draw_triangle(900, 50, 900)
window.mainloop()