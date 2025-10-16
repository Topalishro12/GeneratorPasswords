import secrets
import string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk



# основная функция генерирования пароля
def generate_password(): 
    password = "" # сам пароль
    all_chars = "" # общий набор из цифр и знаков
    length = int(scale.get()) # длина пароля,беря значение из ползунка


    # по умолчанию
    if enabled.get() == False and enabled1.get() == False and enabled2.get() == False and enabled3.get() == False:
        all_chars = string.digits + string.ascii_letters
        for i in range(length):
            password += secrets.choice(all_chars)

    # если все флажки включены
    elif enabled.get() == True and enabled1.get() == True and enabled2.get() == True and enabled3.get() == True:
        all_chars = string.digits + string.ascii_letters + string.punctuation
        for i in range(length):
            password += secrets.choice(all_chars)       
    
    # если первые три флажка включены
    elif enabled.get() == True and enabled1.get() == True and enabled2.get() == True:
        all_chars = string.ascii_letters + string.digits + string.punctuation
        for i in range(length):
            password += secrets.choice(all_chars) 
    # если 1 и 3 флажок включен
    elif enabled.get() == True and enabled2.get() == True:
        all_chars = string.ascii_letters + string.digits
        for i in range(length):
            password += secrets.choice(all_chars)
    # если 2 и 3 флажок включен
    elif enabled1.get() == True and enabled2.get() == True:
        all_chars = string.ascii_letters + string.punctuation
        for i in range(length):
            password += secrets.choice(all_chars)
    # если 3 и 4 флажок включен
    elif enabled2.get() == True and enabled3.get() == True:
        all_chars = string.ascii_letters + string.punctuation
        for i in range(length):
            password += secrets.choice(all_chars)
    # если 1 и 4 флажок включен
    elif enabled.get() == True and enabled3.get() == True:
        all_chars = string.punctuation + string.digits
        for i in range(length):
            password += secrets.choice(all_chars)

    # если включены первые два флажка
    elif enabled.get() == True and enabled1.get() == True:
        all_chars = string.digits + string.punctuation
        for i in range(length):
            password += secrets.choice(all_chars)   
    elif enabled.get() == True:  # если только 1-ый флажок включен то генерируем пароль только с цифрами
        all_chars = string.digits
        for i in range(length):
            password += secrets.choice(all_chars)
    elif enabled1.get() == True: # если только 2-ой флажок включен то генерируем пароль только со знаками
        all_chars = string.punctuation
        for i in range(length):
            password += secrets.choice(all_chars)
    elif enabled2.get() == True: # если только 3-ий флажок включен то генерируем только с буквами
        all_chars = string.ascii_letters
        for i in range(length):
            password += secrets.choice(all_chars)
    elif enabled3.get() == True: # если 4 флажок включен то добавлям знаки
        all_chars = string.punctuation + string.ascii_letters + string.digits
        for i in range(length):
            password += secrets.choice(all_chars)

    
    password_entry.delete(0, 'end') # удаление
    password_entry.insert(0, password) # вставление


# функция для копирования
def append():
    if password_entry.get():
        root.clipboard_clear()
        root.clipboard_append(password_entry.get())
        messagebox.showinfo("Успех", "Пароль скопирован")
    else:
        messagebox.showwarning("Ошибка", "Сначала сгенерируй пароль")

# функция для выведения значения ползунка целым числом
def change(newVal):
    float_value = float(newVal)     # получаем из строки значение float
    int_value = round(float_value)  # округляем до целочисленного значения
    label["text"] = int_value


# настройки
root = Tk()
root["bg"] = "#287091"
root.title("Generator Passwords")
root.geometry("1650x550")


# для информирования
label1 = ttk.Label(root,text="По умолчанию пароль генерируется из букв и цифр", width=200,font=("Arial","24","bold"))
label1.pack(padx=6,pady=6,anchor=S)

# 1 флажок: Включить только цифры
enabled = BooleanVar()
enabled_checkbutton = ttk.Checkbutton(text="Включить только цифры", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)

# 2 флажок: Включить только знаки
enabled1 = BooleanVar()
enabled1_checkbutton = ttk.Checkbutton(text="Включить только знаки", variable=enabled1)
enabled1_checkbutton.pack(padx=7, pady=7, anchor=NW)

# 3 флажок: Включить только буквы
enabled2 = BooleanVar()
enabled2_checkbutton = ttk.Checkbutton(text="Включить только буквы", variable=enabled2)
enabled2_checkbutton.pack(padx=8, pady=8, anchor=NW)

# 4 флажок: Добавить знаки
enabled3 = BooleanVar()
enabled3_checkbutton = ttk.Checkbutton(text="Добавить знаки", variable=enabled3)
enabled3_checkbutton.pack(padx=9, pady=9, anchor=NW)

# поле с паролем
password_entry = ttk.Entry(root, width =40, font=("Arial", 12))
password_entry.pack(pady=20)

# кнопка сгенерировать
generate_btn = ttk.Button(root, text="Сгенерировать пароль",
                          command=generate_password)
generate_btn.pack(pady=10)

# кнопка скопировать
append_btn = ttk.Button(root, text="Скопировать",
                        command=append)
append_btn.pack(pady=11)

# поле который показывает текущее значение длина пароля
label = ttk.Label()
label.pack(anchor=S)
# ползунок для пользовательского выбора длина пароля
scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=8, to=24, command=change)
scale.pack(anchor=S)


root.mainloop()
