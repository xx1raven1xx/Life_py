import tkinter as tk


root = tk.Tk()
c = tk.Canvas(root, height=300, width=500, bg='black')
c.pack()
# с.configure(background='black')

# c.create_rectangle(10,10,20,20, fill='red')

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
    for i in range(44):
        for n in range(26):
            c1 = cell(i, n)


def main():
    drawcell()
    root.after(500,main)
    root.mainloop()


if __name__ == "__main__":
    main()