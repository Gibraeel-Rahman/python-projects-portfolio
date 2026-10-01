import tkinter as tk
root = tk.Tk()
root.title('Python Calculator')
root.geometry('950x600')
root.configure(bg='aliceblue')
root.resizable(False, False)

lblTitle = tk.Label(root, text='Addition Calculator')
lblTitle.pack(pady = 20)

frameFirst = tk.Frame(root)

root.mainloop()
