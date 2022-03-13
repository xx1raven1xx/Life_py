import tkinter as tk
import random


'''
Правила игры жизнь: 
- пустое место рядом с которым есть 3 живые клетки - зарождается жизнь
- 2 или 3 живые соседки - продолжает жить
- если < 2 или > 3 - умирает (от одиночества или от перенаселения)
'''
global tempI
tkHEIGHT = 600 # 300 - помещается 26 клеток ()
tkWIDTH = 1000 # 500 - помещается 44 клетки
root = tk.Tk()
c = tk.Canvas(root, height=tkHEIGHT, width=tkWIDTH, bg='black')
c.pack()
a = [[0 for j in range(tkHEIGHT//11-1)] for i in range(tkWIDTH//11-1)]
#a = [[0 for j in range(tkWIDTH//11-2)] for i in range(tkHEIGHT//11-2)]
print((tkHEIGHT//11-2), (tkWIDTH//11-2))
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
        print(self.x,self.y)
        a[self.x][self.y] = 1
        pass

    def create():
        '''Функция рождения клетки'''
        pass
    
    def death(self):
        '''Функция смерти клетки'''
        c.delete(self.id)
        a[self.x][self.y] = 0
        pass

    def check():
        '''Поверка окружения'''
        for i in range(tkHEIGHT//11-2):
            for j in range(tkWIDTH//11-2):
                pass
        pass
    
    def update():
        pass


def drawcell():
    global tempI
    # c1 = cell(random.randint(0, tkWIDTH//11-2), random.randint(0, tkHEIGHT//11-2))
    # print((0, tkWIDTH//11-2),(0, tkHEIGHT//11-2))
    cell(tempI, 10)
    tempI += 1
    root.after(1000,drawcell)


def main():
    global tempI
    tempI = 0
    cell(1, 1)
    cell(0, 0)
    cell(88, 52)
    root.after(1000,drawcell)
    root.mainloop()


if __name__ == "__main__":
    main()