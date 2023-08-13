from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import calculations

class calculation_units:
    def __init__(self, num1, num2, temp, operator, answer = None):
        self.num1 = num1
        self.num2 = num2
        self.temp = temp
        self.operator = operator
        self.equals = "="
        self.answer = answer

    def define(self, num1, num2, operator):
        print(num1, num2, operator)
        return

    def num_pressed(self, number_added):
        self.num1.append(number_added)
        return

answer = ""
num1 = 0
num2 = 0
operator = ""
calculation = []
pens = 1

root = Tk()
root.title("Calculator")
root.minsize(348, 495)
root.maxsize(348, 495)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)


button_symbols = ["ce", " ", " ", "%", 7, 8, 9, "x", 4, 5, 6, "-", 1, 2, 3, "+", "+/-", 0, ".", "="]
main_font = Font(family="Helvetica", size=32)




def calc_buttons():
    x, y = 0, 0
    buttons = Frame(root, height=5, width=3, bg="#2c2c2c")
    buttons.grid(row=1, column=0, columnspan=1, sticky="news")


    for symbol in button_symbols:
        button = Button(buttons, width=3,  height=1, bg="#484848", text=symbol, font=main_font, borderwidth=1, relief="solid")
        if x >= 4:
            x = 0
            y += 1

        button.grid(row=y, column=x, padx=2, pady=2)
        x += 1
        button.bind("<Button-1>", clicked_button)

def results():
    display = Frame(root, height=1, width=10, bg="#595959")
    display.grid(row=0, column=0, sticky="news")

    display.columnconfigure(0, weight=2)
    display.columnconfigure(1, weight=1)
    display.columnconfigure(2, weight=2)
    display.columnconfigure(3, weight=1)
    display.columnconfigure(4, weight=3)

    first_number = Label(display, text=pens, font=main_font, bg="#595959")
    first_number.grid(row=0, column=0)

    symbols = Label(display, text="+", font=calc.operator, bg="#595959")
    symbols.grid(row=0, column=1)

    second_number = Label(display, text=calc.num2, font=main_font, bg="#595959")
    second_number.grid(row=0, column=2)

    equals = Label(display, text="=", font=calc.equals, bg="#595959")
    equals.grid(row=0, column=3)

    result = Label(display, text=answer, font=main_font, bg="#595959", borderwidth=2, relief="solid")
    result.grid(row=0, column=4)

def define_num1(num1):
    calc.num1 = num1


def clicked_button(event):
    global num1, num2, operator
    button_translator = {
        "!button": "CE",
        "!button18": 0,
        "!button13": 1,
        "!button14": 2,
        "!button15": 3,
        "!button9": 4,
        "!button10": 5,
        "!button11": 6,
        "!button5": 7,
        "!button6": 8,
        "!button7": 9,
        "!button17": "+/-",
        "!button19": ".",
        "!button20": "=",
        "!button16": "+",
        "!button12": "-",
        "!button8": "x",
        "!button4": "%",
    }

    character = button_translator[event.widget._name]
    print(character)
    try:
        '''only numbers work within here'''
        calc.num_pressed(character)
        print(calc.num1)

    except ValueError:
        '''any other button'''
        if character == "CE":
            calculation.clear()

        operators = ("-", "+", "%", "*")
        if character in operators:
            operator = character
            temp = num1
            temp.join("")
            print(temp)


        if character == "=":
            temp = num2
            num2 = num1
            num1 = temp

            answer = calculations.calculate(num1, num2, operator)

        results()



calc = calculation_units([], [], "+", 0)

calc_buttons()
results()















root.mainloop()