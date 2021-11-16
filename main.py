import tkinter as tk
import time

root = tk.Tk()
c = tk.Canvas(root, height=300, width=500, bg='black')
c.pack()
# с.configure(background='black')

# c.create_rectangle(10,10,20,20, fill='red')
'''
class cell():
    def __init__(x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
    
    def create():
        pass
    
    def death():
        pass
'''


def cell():
    for i in range(20):
        for n in range(20):
            c.create_rectangle(10+(11*i), 10+(11*n), 20+(11*i), 20+(11*n), fill='red', outline='black')
    


def main():
    while True:
        cell()
        root.update_idletasks()
        root.update()
        time.sleep(0.1)
        #root.mainloop()


if __name__ == "__main__":
    main()