import secrets
import string
from tkinter import *
from tkinter import ttk,messagebox,Tk
# основная функция генерирования пароля
def generate_password(): 
    password = ''.join(secrets.choice(all_chars) for _ in range(length)) # сам пароль
    length = int(scale.get()) # длина пароля,беря значение из ползунка
    available_sets = {
        'digits': string.digits if enabled.get() else '',
        'letters': string.ascii_letters if enabled2.get() else '',
        'punctuation': string.punctuation if enabled1.get() else ''
    }
    digit = available_sets["digits"]
    letters = available_sets["letters"]
    punctuations = available_sets["punctuation"]
    all_chars = digit+letters+punctuations # общий набор
    if all_chars == "":
        all_chars = string.ascii_letters + string.digits
    password_entry.delete(0, 'end') # удаление
    password_entry.insert(0, password) # вставление-
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
root.geometry("1450x550")

# для информирования
label1 = ttk.Label(root,text="По умолчанию пароль генерируется из букв и цифр", width=200,font=("Arial","20","bold"),anchor='center')
label1.pack(padx=6,pady=6,anchor=S)

# 1 флажок: Включить только цифры
enabled = BooleanVar()
enabled_checkbutton = ttk.Checkbutton(text="Включить только цифры", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)

# 2 флажок: Включить только знаки
enabled1 = BooleanVar()
enabled1_checkbutton = ttk.Checkbutton(text="Включить знаки", variable=enabled1)
enabled1_checkbutton.pack(padx=7, pady=7, anchor=NW)

# 3 флажок: Включить только буквы
enabled2 = BooleanVar()
enabled2_checkbutton = ttk.Checkbutton(text="Включить только буквы", variable=enabled2)
enabled2_checkbutton.pack(padx=8, pady=8, anchor=NW)

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
