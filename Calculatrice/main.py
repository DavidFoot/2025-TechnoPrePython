import tkinter as tk

current_operande=''
array_operande=[]
array_operator=[]

def clic_handler_number(_value):
    global result, current_operande
    current_operande+= str(_value)
    result.config(text=str(current_operande))


def remove_last_number():
    global result, current_operande
    current_operande = current_operande[0:len(current_operande)-1]
    result.config(text=str(current_operande))


def operation(_value):
    global array_operande, current_operande, array_operator
    array_operande.append(current_operande)
    array_operator.append(_value)
    current_operande=''
    result.config(text="")


def reset_all():
    global array_operande, current_operande, array_operator
    array_operande = []
    current_operande = ''
    array_operator = []
    result.config(text="")


def get_calc_done():
    global array_operande, current_operande, array_operator
    res=0
    array_operande.append(current_operande)
    current_operande = ''
    if len(array_operande) >=2 and len(array_operator) >= 1 :
        res = float(array_operande[0])
        for x in range(1,len(array_operande)):
            if array_operator[x-1] == '+' :
                res = res + float(array_operande[x])
            if array_operator[x - 1] == '-':
                res = res - float(array_operande[x])
            if array_operator[x - 1] == '*':
                res = res * float(array_operande[x])
            if array_operator[x - 1] == '/':
                res = res / float(array_operande[x])
        array_operande = []
        array_operator = []
        result.config(text=str(res))
        current_operande = str(res)

#Creation de la fenetre principale du programme
main_window = tk.Tk(screenName="Ma calculatrice",baseName="",useTk=True,className="HelloWorld" )
result = tk.Label(main_window, text='0')
# Les chiffres
button1 = tk.Button(main_window, text="7", command=lambda:clic_handler_number(7))
button2 = tk.Button(main_window, text="8", command=lambda:clic_handler_number(8))
button3 = tk.Button(main_window, text="9", command=lambda:clic_handler_number(9))
button4 = tk.Button(main_window, text="4", command=lambda:clic_handler_number(4))
button5 = tk.Button(main_window, text="5", command=lambda:clic_handler_number(5))
button6 = tk.Button(main_window, text="6", command=lambda:clic_handler_number(6))
button7 = tk.Button(main_window, text="1", command=lambda:clic_handler_number(1))
button8 = tk.Button(main_window, text="2", command=lambda:clic_handler_number(2))
button9 = tk.Button(main_window, text="3", command=lambda:clic_handler_number(3))
button0 = tk.Button(main_window, text="0", command=lambda:clic_handler_number(0))
# Les operations
button_decimal_point = tk.Button(main_window, text=".", command=lambda:clic_handler_number('.'))
button_equal = tk.Button(main_window, text="=", command=get_calc_done)
button_sum = tk.Button(main_window, text="+", command=lambda:operation('+'))
button_substract = tk.Button(main_window, text="-", command=lambda:operation('-'))
button_divide = tk.Button(main_window, text="/" , command=lambda:operation('/'))
button_multiply = tk.Button(main_window, text="*" , command=lambda:operation('*'))
button_reset = tk.Button(main_window, text="C", command=reset_all)
button_backspace = tk.Button(main_window, text="<-", command=remove_last_number)


#Positionnement dans la fenetre
# Top Row For result display
result.grid(row=0, columnspan=3, pady=5)
# Row 1
button1.grid(row=1,column=0,ipadx=10, pady=2,padx=5)
button2.grid(row=1,column=1,ipadx=10, pady=2,padx=5)
button3.grid(row=1,column=2,ipadx=10, pady=2,padx=5)
# Row 2
button4.grid(row=2,column=0,ipadx=10, pady=2,padx=5)
button5.grid(row=2,column=1,ipadx=10, pady=2,padx=5)
button6.grid(row=2,column=2,ipadx=10, pady=2,padx=5)
# Row 3
button7.grid(row=3,column=0,ipadx=10, pady=2,padx=5)
button8.grid(row=3,column=1,ipadx=10, pady=2,padx=5)
button9.grid(row=3,column=2,ipadx=10, pady=2,padx=5)
# Column Operator
button_sum.grid(row=0 ,column=3, ipadx=10, pady=2,padx=5)
button_substract.grid(row=1 ,column=3, ipadx=10, pady=2,padx=5)
button_multiply.grid(row=2 ,column=3, ipadx=10, pady=2,padx=5)
button_divide.grid(row=3 ,column=3, ipadx=10, pady=2,padx=5)
# Row 4
button_reset.grid(row=4 ,column=0,ipadx=10, pady=2,padx=5)
button0.grid(row=4 ,column=1,ipadx=10, pady=2,padx=5)
button_backspace.grid(row=4 ,column=2,ipadx=10, pady=2,padx=5)
button_equal.grid(row=4 ,column=3, ipadx=10, pady=2,padx=5)
# Row 5
button_decimal_point.grid(row=5 ,column=1,ipadx=10, pady=2,padx=5)

# Machin brol qui loop
main_window.mainloop()