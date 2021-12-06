import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import json
from image_downloader import ImageDownloader


class Barcode:

    def __init__(self, barcode_type, item_name):
        self.barcode_type = barcode_type
        self.item_name = item_name
        self.barcode_number = None
        self.length = 0
        self.picture_link = None

    def validate(self):
        if len(self.barcode_number) > 0:
            x = self.barcode_number  # does the calculation for the barcode modulo
            cal1 = x[0] + x[2] + x[4] + x[6] + x[8] + x[10]
            cal0 = cal1 * 3
            cal2 = x[1] + x[3] + x[5] + x[7] + x[9]
            cal3 = cal0 + cal2
            cal4 = cal3 % 10
            fnl = 10 - cal4
            if fnl != x[11]:
                return False
            else:
                return True
        else:
            return False

    def convert2binary(self):
        if len(self.barcode_number) > 0:
            lst = ['101']
            left = str(self.barcode_number)[1:6]
            right = str(self.barcode_number)[6:11]

            for s in left:  # left side of the barcode
                i = int(s)
                if i == 0:
                    lst.append('0001101')
                elif i == 1:
                    lst.append('0011001')
                elif i == 2:
                    lst.append('0010011')
                elif i == 3:
                    lst.append('0111101')
                elif i == 4:
                    lst.append('0100011')
                elif i == 5:
                    lst.append('0110001')
                elif i == 6:
                    lst.append('0101111')
                elif i == 7:
                    lst.append('0111011')
                elif i == 8:
                    lst.append('0110111')
                elif i == 9:
                    lst.append('0001011')
            lst.append('01010')  # the center
            for s in right:  # right side
                i = int(s)
                if i == 0:
                    lst.append('1110010')
                elif i == 1:
                    lst.append('1100110')
                elif i == 2:
                    lst.append('1101100')
                elif i == 3:
                    lst.append('1000010')
                elif i == 4:
                    lst.append('1011100')
                elif i == 5:
                    lst.append('1001110')
                elif i == 6:
                    lst.append('1010000')
                elif i == 7:
                    lst.append('1000100')
                elif i == 8:
                    lst.append('1001000')
                elif i == 9:
                    lst.append('1110100')
            lst.append('101')  # ending guard
            return "".join(lst)
        else:
            return None


class BarcodeGenerator:

    def __init__(self, barcode):
        self.barcode = barcode

    def generate(self):
        nsc = "0"
        manufacturer_id = str(random.randint(0, 99999)).zfill(5)
        item_number = str(random.randint(0, 99999)).zfill(5)
        modulo_check = str(self.__calculate_modulo_check(nsc, manufacturer_id, item_number))
        self.barcode.barcode_number = nsc + manufacturer_id + item_number + modulo_check
        self.barcode.length = 12

    def find_picture(self):
        imd = ImageDownloader(self.barcode.item_name)
        self.barcode.picture_link = imd.search_link()

    def __calculate_modulo_check(self, nsc, l, r):
        x = nsc + l + r
        x = list(map(int, [char for char in x]))
        cal1 = x[0] + x[2] + x[4] + x[6] + x[8] + x[10]
        cal0 = cal1 * 3
        cal2 = x[1] + x[3] + x[5] + x[7] + x[9]
        cal3 = cal0 + cal2
        cal4 = cal3 % 10
        return 0 if cal4 == 0 else 10 - cal4


class BarcodeDrawer:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.barcode_number = None
        self.barcode_image = None
        self.item_name = None
        self.item_picture = None

    def draw(self, barcode, canvas):
        if self.barcode_number is not None:
            canvas.delete(self.barcode_number)
        if self.barcode_image is not None:
            self.__deleteBarcodeBars(canvas)
        if self.item_name is not None:
            canvas.delete(self.item_name)
        if self.item_picture is not None:
            canvas.delete(self.item_picture)
        self.barcode_number = canvas.create_text(415, 350, font=("Tahoma", 24), text=barcode.barcode_number)
        self.barcode_image = self.__drawBarcodeBars(barcode, canvas)
        self.item_name = canvas.create_text(415, 240, font=("Tahoma", 18), text=barcode.item_name)
        global img
        img = ImageDownloader.download_image(barcode.picture_link, barcode.item_name)
        barcode.picture_link = "./img/" + barcode.item_name + ".jpg"
        self.item_picture = canvas.create_image((370, 140), image=img, anchor=NW)

    def __deleteBarcodeBars(self, canvas):
        for rect in self.barcode_image:
            canvas.delete(rect)

    def __drawBarcodeBars(self, barcode, canvas):
        binary_str = barcode.convert2binary()
        bar_width = self.width
        bar_height = self.height
        x_offset = 337
        y_offset = 270
        rects = []
        for ch in binary_str:
            if ch == "1":
                rect = canvas.create_rectangle(x_offset, y_offset,
                                               x_offset + bar_width,
                                               y_offset + bar_height,
                                               fill='black')
                rects.append(rect)
            x_offset = x_offset + bar_width
        return rects


class MyGUI(Frame):

    def __init__(self, parent, bd):
        Frame.__init__(self, parent)
        self.parent = parent
        self.bd = bd
        self.__initUI()

    def __initUI(self):

        self.parent.title("Barcode Generator")
        self.config(bg='#F0F0F0')
        self.pack(fill=BOTH, expand=1)

        # Create canvas
        self.my_canvas = Canvas(self, relief=FLAT, background="#D2D2D2",
                         width=180, height=500)
        self.my_canvas.pack(fill=BOTH, expand=1)

        # Create button to generate barcode
        self.generate_button = Button(self.my_canvas, text="Generate Barcode", command=self.__handleGenerate,
                         width=20, height=5, font=("Tahoma", 12), state=DISABLED)
        self.generate_button.pack(side=BOTTOM)
        self.generate_button.place(x=320, y=400)

        # Create button to save generated barcode to JSON file
        self.save_button = Button(self.my_canvas, text="Save",
                         width=5, font="Tahoma", state=DISABLED, command=self.__saveToFile)
        self.save_button.pack(side=BOTTOM)
        self.save_button.place(x=550, y=534)

        # Add listener for input text modification
        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.__activateGenerateBtn(sv))

        # Create input field and label to enter item's name
        self.e_item_name = Entry(self.my_canvas, textvariable=sv)
        l_item_name = Label(self.my_canvas, text="Enter item name:", bg="white")
        self.my_canvas.create_window(460,550,window=self.e_item_name)
        self.my_canvas.create_window(340,550,window=l_item_name)

        # Information labels or text messages
        self.l_saved_success = self.my_canvas.create_text(615, 520, font=("Tahoma", 8),
                                                          text="Barcode saved successfully", fill="green",
                                                          state=HIDDEN)

    def __activateGenerateBtn(self, sv):
        if len(sv.get()) > 0:
            self.generate_button["state"] = "active"
        else:
            self.generate_button["state"] = "disabled"

    def __handleGenerate(self):
        self.my_canvas.itemconfig(self.l_saved_success, state=HIDDEN)
        item_name = "Undefined"
        e_item_name_text = self.e_item_name.get()
        if len(e_item_name_text) > 0:
            item_name = e_item_name_text
        if not self.__checkAlreadyExists(item_name):
            self.bd.barcode = Barcode("UPC-A", item_name)
            bg = BarcodeGenerator(self.bd.barcode)
            bg.generate()
            bg.find_picture()
            self.bd.draw(self.bd.barcode, self.my_canvas)
            self.save_button["state"] = "active"
        else:
            showinfo("Error", "Barcode for this item already exists")

    def __checkAlreadyExists(self, item_name):
        filename = 'barcodes.json'
        with open(filename, "r") as file:
            data = json.load(file)
        for barcode in data:
            if item_name == barcode["item_name"]:
                return True
        return False

    def __saveToFile(self):
        filename = 'barcodes.json'
        entry = {
            "barcode_type": self.bd.barcode.barcode_type,
            "barcode_number": self.bd.barcode.barcode_number,
            "item_name": self.bd.barcode.item_name,
            "picture_link": self.bd.barcode.picture_link
        }
        with open(filename, "r") as file:
            data = json.load(file)
        data.append(entry)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
        self.e_item_name.delete(0, "end")
        self.my_canvas.itemconfig(self.l_saved_success, state=NORMAL)
        self.save_button["state"] = "disabled"


def main():
    root = Tk()
    root.geometry('800x600+10+50')
    bd = BarcodeDrawer(2, 60)
    app = MyGUI(root, bd)
    app.mainloop()


if __name__ == "__main__":
    main()