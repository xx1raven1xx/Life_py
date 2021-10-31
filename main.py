import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, height=300, width=500, bg='black')
c.pack()
# с.configure(background='black')

# c.create_rectangle(10,10,20,20, fill='red')


def cell():
    for i in range(20):
        c.create_rectangle(10+i, 10, 20*i, 20, fill='red', outline='yellow')
    pass


def main():
    cell()
    root.mainloop()


if __name__ == "__main__":
    main()