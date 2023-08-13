from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from calculations import calculate

class calculation_units:
    def __init__(self, num1, num2, operator, answer):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.equals = "="
        self.answer = answer

    def num_pressed(self, number_added):
        self.num2.append(number_added)
        return

root = Tk()
root.title("Calculator")
root.minsize(348, 495)
root.maxsize(348, 495)
operators = ("-", "+", "%", "x")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)

button_symbols = ["ce", " ", " ", "%", 7, 8, 9, "x", 4, 5, 6, "-", 1, 2, 3, "+", "+/-", 0, ".", "="]
main_font = Font(family="Helvetica", size=32)
small_font = Font(family="Helvetica", size=12)

def calc_buttons():
    x, y = 0, 0
    buttons = Frame(root, height=5, width=3, bg="#2c2c2c")
    buttons.grid(row=1, column=0, columnspan=1, sticky="news")


    for symbol in button_symbols:
        button = Button(buttons, width=3,  height=1, bg="#484848", text=symbol,
                        font=main_font, borderwidth=1, relief="solid")
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

    if calc.operator not in operators:
        '''happens first'''
        p = calc.num2
        q = ""
    else:
        p = calc.num1
        q = calc.num2

    first_number = Label(display, text=p, font=small_font, bg="#595959")
    first_number.grid(row=0, column=0)

    symbols = Label(display, text=calc.operator, font=small_font, bg="#595959")
    symbols.grid(row=0, column=1)

    second_number = Label(display, text=q, font=small_font, bg="#595959")
    second_number.grid(row=0, column=2)

    equals = Label(display, text="=", font=small_font, bg="#595959")
    equals.grid(row=0, column=3)

    result = Label(display, text=calc.answer, font=main_font, bg="#595959")
    result.grid(row=0, column=4)

def clicked_button(event):
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
    try:
        int(character)
        '''only numbers work within here'''
        calc.num_pressed(character)

    except ValueError:
        '''any other button'''
        if character == "CE":
            calc.num1 = []
            calc.num2 = []
            calc.operator = ""
            calc.answer = ""

        if character in operators:
            calc.operator = character
            calc.num1 = "".join(str(val) for val in calc.num2)
            calc.num2.clear()

        if character == "=":
            calc.num2 = "".join(str(val) for val in calc.num2)
            calc.answer = calculate(calc.num1, calc.num2, calc.operator)

    results()

calc = calculation_units([], [], "", 0) #init class

# vv Main Program vv
calc_buttons()
results()
root.mainloop()