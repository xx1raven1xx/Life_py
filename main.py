import tkinter as tk
import random


'''
Правила игры жизнь: 
- пустое место рядом с которым есть 3 живые клетки - зарождается жизнь
- 2 или 3 живые соседки - продолжает жить
- если < 2 или > 3 - умирает (от одиночества или от перенаселения)
'''

tkHEIGHT = 600 # 300 - помещается 26 клеток ()
tkWIDTH = 1000 # 500 - помещается 44 клетки
root = tk.Tk()
c = tk.Canvas(root, height=tkHEIGHT, width=tkWIDTH, bg='black')
c.pack()
a = [[0 for j in range(tkWIDTH//11-2)] for i in range(tkHEIGHT//11-2)]
# for i in range(tkHEIGHT//11-2):
#     print(a[i])

class cell():
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.draw()
        # self.id = c.create_rectangle(10+(11*self.x), 10+(11*self.y), 20+(11*self.x), 20+(11*self.y), fill='red', outline='black')
    
    def draw(self):
        self.id = c.create_rectangle(10+(11*self.x), 10+(11*self.y), 20+(11*self.x), 20+(11*self.y), fill='red', outline='black')
        pass

    def create():
        '''Функция рождения клетки'''
        pass
    
    def death():
        '''Функция смерти клетки'''
        pass

    def check():
        '''Поверка окружения'''
        pass
    
    def update():
        pass


def drawcell():
    c1 = cell(random.randint(0, tkWIDTH//11-2), random.randint(0, tkHEIGHT//11-2))
    root.after(1,drawcell)
    # c1.draw()


def main():
    root.after(100,drawcell)
    root.mainloop()


if __name__ == "__main__":
    main()