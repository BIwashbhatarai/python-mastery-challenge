import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

padx_val = 15
pady_val = 20
btn_width = 5  # approximate width
btn_height =2 # approximate height

button_1 = tk.Button(root, text='1', font=20,  width=btn_width, height=btn_height, command=lambda: button_click(1))
button_2 = tk.Button(root, text='2', font=20,width=btn_width, height=btn_height, command=lambda: button_click(2))
button_3 = tk.Button(root, text='3', font=20,width=btn_width, height=btn_height, command=lambda: button_click(3))
button_4 = tk.Button(root, text='4', font=20,width=btn_width, height=btn_height, command=lambda: button_click(4))
button_5 = tk.Button(root, text='5', font=20,width=btn_width, height=btn_height, command=lambda: button_click(5))
button_6 = tk.Button(root, text='6', font=20,width=btn_width, height=btn_height, command=lambda: button_click(6))
button_7 = tk.Button(root, text='7', font=20,width=btn_width, height=btn_height, command=lambda: button_click(7))
button_8 = tk.Button(root, text='8', font=20,width=btn_width, height=btn_height, command=lambda: button_click(8))
button_9 = tk.Button(root, text='9', font=20,width=btn_width, height=btn_height, command=lambda: button_click(9))
button_0 = tk.Button(root, text='0', font=20,width=btn_width, height=btn_height, command=lambda: button_click(0))

button_1.grid(row=3, column=0, padx=padx_val, pady=pady_val, sticky='w')
button_2.grid(row=3, column=1, padx=padx_val, pady=pady_val, sticky='w')
button_3.grid(row=3, column=2, padx=padx_val, pady=pady_val, sticky='w')

button_4.grid(row=2, column=0, padx=padx_val, pady=pady_val, sticky='w')
button_5.grid(row=2, column=1, padx=padx_val, pady=pady_val, sticky='w')
button_6.grid(row=2, column=2, padx=padx_val, pady=pady_val, sticky='w')

button_7.grid(row=1, column=0, padx=padx_val, pady=pady_val, sticky='w')
button_8.grid(row=1, column=1, padx=padx_val, pady=pady_val, sticky='w')
button_9.grid(row=1, column=2, padx=padx_val, pady=pady_val, sticky='w')

button_0.grid(row=4, column=0, padx=padx_val, pady=pady_val, sticky='w')



button_add = tk.Button(root, text='+',font=20, width=btn_width, height=btn_height, command=lambda: button_click("+"))
button_sub = tk.Button(root, text='-',font=20, width=btn_width, height=btn_height, command=lambda: button_click("-"))
button_mul= tk.Button(root, text='*',font=20, width=btn_width, height=btn_height, command=lambda: button_click("*"))
button_div = tk.Button(root, text='/',font=20, width=btn_width, height=btn_height, command=lambda: button_click("/"))

button_add.grid(row=1,column=3, padx=padx_val, pady=pady_val)
button_sub.grid(row=2,column=3, padx=padx_val, pady=pady_val)
button_mul.grid(row=3,column=3, padx=padx_val, pady=pady_val)
button_div.grid(row=4,column=3, padx=padx_val, pady=pady_val)

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    try:
        result = str(eval(expression))
        display.delete(0,tk.END)
        display.insert(0,result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")   

button_c = tk.Button(root, text='C',font=20, width=btn_width, height=btn_height, command= button_clear)
button_e = tk.Button(root, text='=',font=20,  width=btn_width, height=btn_height, command= button_equal)

button_c.grid(row=4, column=1, padx=padx_val, pady=pady_val, sticky='w')
button_e.grid(row=4, column=2, padx=padx_val, pady=pady_val, sticky='w')
root.mainloop()
