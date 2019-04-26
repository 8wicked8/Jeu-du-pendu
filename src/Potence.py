from tkinter import *

def dessiner(canvas, nombre_de_vie):
    if nombre_de_vie < 11:
        canvas.create_line(100, 400, 300, 400)
        if nombre_de_vie < 10:
            canvas.create_line(200, 400, 200, 100)
            if nombre_de_vie < 9:
                canvas.create_line(200, 100, 350, 100)
                if nombre_de_vie < 8:
                    canvas.create_line(237.5, 100, 200, 150)
                    if nombre_de_vie < 7:
                        canvas.create_line(350, 100, 350, 150)
                        if nombre_de_vie < 6:
                            canvas.create_oval(325, 150, 375 ,200)
                            if nombre_de_vie < 5:
                                canvas.create_line(350, 200, 350 ,275)
                                if nombre_de_vie < 4:
                                    canvas.create_line(350, 275, 400, 325)
                                    if nombre_de_vie < 3:
                                        canvas.create_line(350, 275, 300, 325)
                                        if nombre_de_vie < 2:
                                            canvas.create_line(350, 230, 375, 260)
                                            if nombre_de_vie < 1:
                                                canvas.create_line(350, 230, 325, 260)



