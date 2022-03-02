from tkinter import *
import math

root = Tk()
# tytuł
root.title("Kalkulator ~by OfioN")
# ustawienie okna
root.geometry('364x444+700+200')
root.configure(background='black')
root.resizable(width=False, height=False)

# typ kalkulatora
type_cal = Label(text="Standardowy",font=('Helventica', 12), background='black', fg='white').grid(row=0,column=0, padx=100, columnspan=4)

# wyświetlacz
screen = Entry(root,bd=3, font=('Helventica', 20))
screen.grid(row=1, column=0, columnspan=4, pady=10, padx=7)
# funkcja wyświetlania na ekran

def show_numbers(number):
    show = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(show) + str(number))
    
# funkcja equals

def button_equals_show():
    second_number = screen.get()
    screen.delete(0, END)
    
    if solution == "add":
        screen.insert(0, f_num + float(second_number))
    elif solution == "subtract":
        screen.insert(0, f_num - float(second_number))
    elif solution == "multiply":
        screen.insert(0, f_num * float(second_number))
    elif solution == "devide":
        screen.insert(0, f_num / float(second_number))
    elif solution == "modulo":
        screen.insert(0, f_num % float(second_number))
    elif solution == "square":
        screen.insert(0, (f_num * f_num))
    elif solution == "1_per_x":
        screen.insert(0, (1/f_num))
    elif solution == "element":
        ele = math.sqrt(f_num)
        screen.insert(0, ele)
    

# funkcje operacji matematycznych    

def button_add_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "add"
    f_num = float(first_number)
    screen.delete(0, END)

def button_subtract_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "subtract"
    f_num = float(first_number)
    screen.delete(0, END)
    
def button_multiply_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "multiply"
    f_num = float(first_number)
    screen.delete(0, END)

def button_element_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "element"
    f_num = float(first_number)
    screen.delete(0, END)
    ele = math.sqrt(f_num)
    screen.insert(0, ele)

def button_square_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "square"
    f_num = float(first_number)
    screen.delete(0, END)
    screen.insert(0, (float(f_num) * float(f_num)))

def button_devide_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "devide"                     # pisze się divide
    f_num = float(first_number)
    screen.delete(0, END)
    
def button_modulo_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "modulo"
    f_num = float(first_number)
    screen.delete(0, END)

def button_1_per_x_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "1_per_x"
    f_num = float(first_number)
    screen.delete(0, END)  
    screen.insert(0, (1/f_num))
 
def button_backspace_f():
    show = screen.get()[:-1]
    screen.insert(0, str(show))    
    screen.delete(0, END)
    screen.insert(0, str(show))

def button_clear_f():  
    screen.delete(0, END)

def button_plus_per_minus_f():
    first_number = screen.get()
    global f_num
    global solution
    solution = "plus_per_minus"
    f_num = float(first_number)
    screen.delete(0, END)  
    screen.insert(0, (-f_num))

# przypisanie zmiennych

number_1 = Button(root, text="1",font=('Helventica', 12), pady=15, command=lambda:show_numbers(1), background='black', fg='white', width=9)
number_2 = Button(root, text="2",font=('Helventica', 12), pady=15, command=lambda:show_numbers(2), background='black', fg='white', width=9)
number_3 = Button(root, text="3",font=('Helventica', 12), pady=15, command=lambda:show_numbers(3), background='black', fg='white', width=9)
number_4 = Button(root, text="4",font=('Helventica', 12), pady=15, command=lambda:show_numbers(4), background='black', fg='white', width=9)
number_5 = Button(root, text="5",font=('Helventica', 12), pady=15, command=lambda:show_numbers(5), background='black', fg='white', width=9)
number_6 = Button(root, text="6",font=('Helventica', 12), pady=15, command=lambda:show_numbers(6), background='black', fg='white', width=9)
number_7 = Button(root, text="7",font=('Helventica', 12), pady=15, command=lambda:show_numbers(7), background='black', fg='white', width=9)
number_8 = Button(root, text="8",font=('Helventica', 12), pady=15, command=lambda:show_numbers(8), background='black', fg='white', width=9)
number_9 = Button(root, text="9",font=('Helventica', 12), pady=15, command=lambda:show_numbers(9), background='black', fg='white', width=9)
number_0 = Button(root, text="0",font=('Helventica', 12), pady=15, command=lambda:show_numbers(0), background='black', fg='white', width=9)
button_comma = Button(root, text=",",font=('Helventica', 12), pady=15, command=lambda:show_numbers("."), background='black', fg='white', width=9)
button_equals = Button(root, text="=",font=('Helventica', 12), pady=15, command= button_equals_show, background='black', fg='white', width=9)
button_add = Button(root, text="+",font=('Helventica', 12), pady=15, command=button_add_f, background='black', fg='white', width=9)
button_subtract = Button(root, text="-",font=('Helventica', 12), pady=15, command=button_subtract_f, background='black', fg='white', width=9)
button_multiply = Button(root, text="*",font=('Helventica', 12), pady=15, command=button_multiply_f, background='black', fg='white', width=9)
button_devide = Button(root, text="/",font=('Helventica', 12), pady=15, command=button_devide_f, background='black', fg='white', width=9)
button_percent = Button(root, text="%\n(modulo)",font=('Helventica', 12), pady=6, command=button_modulo_f, background='black', fg='white', width=9)
button_clear = Button(root, text="C",font=('Helventica', 12), pady=15, command=button_clear_f, background='black', fg='white', width=9)
button_ce = Button(root, text="CE",font=('Helventica', 12),pady=15, command=button_clear_f, background='black', fg='white', width=9)
button_backspace = Button(root, text="←",font=('Helventica', 12), pady=15, command=button_backspace_f, background='black', fg='white', width=9)
button_1_per_x = Button(root, text="1/x",font=('Helventica', 12), pady=15, command=button_1_per_x_f, background='black', fg='white', width=9)
button_x_square = Button(root, text="x²",font=('Helventica', 12), pady=15, command=button_square_f, background='black', fg='white', width=9)
button_x_element = Button(root, text="√",font=('Helventica', 12), pady=15, command=button_element_f, background='black', fg='white', width=9)
button_plus_per_minus = Button(root, text="+/-",font=('Helventica', 12), pady=15, command=button_plus_per_minus_f, background='black', fg='white', width=9)

# ułożenie zmiennych graficznie

button_percent.grid(row=2,column=0)
button_ce.grid(row=2,column=1)
button_clear.grid(row=2,column=2)
button_backspace.grid(row=2,column=3)

button_1_per_x.grid(row=3,column=0,)
button_x_square.grid(row=3,column=1)
button_x_element.grid(row=3,column=2)
button_devide.grid(row=3,column=3)

number_7.grid(row=4, column=0)
number_8.grid(row=4, column=1)
number_9.grid(row=4, column=2)
button_multiply.grid(row=4, column=3)

number_4.grid(row=5, column=0)
number_5.grid(row=5, column=1)
number_6.grid(row=5, column=2)
button_subtract.grid(row=5, column=3)

number_1.grid(row=6, column=0)
number_2.grid(row=6, column=1)
number_3.grid(row=6, column=2)
button_add.grid(row=6, column=3)

button_plus_per_minus.grid(row=7, column=0)
number_0.grid(row=7, column=1)
button_comma.grid(row=7, column=2)
button_equals.grid(row=7, column=3)

root.mainloop()