# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=500)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

class Barcode:

    def __init__(self, barcode_type, item_name):
        self.barcode_type = barcode_type
        self.item_name = item_name
        self.barcode_number = None
        self.length = 0

    def validate(self):
        pass

    def convert2binary(self):
        pass


class BarcodeGenerator:

    def __init__(self, barcode):
        self.barcode = barcode

    def generate(self):
        pass


class BarcodeDrawer:

    def __init__(self, width, height, bar_width):
        self.turtle = None
        self.width = width
        self.height = height
        self.bar_width = bar_width

    def draw(self, barcode, turtle):
        pass

