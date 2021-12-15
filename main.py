import tkinter as tk
import random


'''
Правила игры жизнь: 
- пустое место с которым есть 3 живые клетки - зарождается жизнь
- 2 или 3 живые соседки - продолжает жить
- если < 2 или > 3 - умирает (от одиночества или от перенаселения)
'''
root = tk.Tk()
c = tk.Canvas(root, height=300, width=500, bg='black')
c.pack()


class cell():
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.id = c.create_rectangle(10+(11*self.x), 10+(11*self.y), 20+(11*self.x), 20+(11*self.y), fill='red', outline='black')
    
    def draw(self):
        pass

    def create():
        pass
    
    def death():
        pass
    
    def update():
        pass


def drawcell():
    for i in range(25):
        c1 = cell(random.randint(0, 44), random.randint(0, 26))


def main():
    drawcell()
    root.after(500,main)
    root.mainloop()


if __name__ == "__main__":
    main()