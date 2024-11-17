import tkinter as tk
from tkinter.ttk import Combobox
import math
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox


# Определение основного окна
window = tk.Tk()
window.title("Калькулятор площади")
window.geometry("1000x500+1000+0")  # Устанавливаем размер и положение окна
window.configure(bg="#e0f7fa")


# Функции для расчета площади треугольника
def calculate_area_with_base_and_height(base, height):
    try:
        base = float(base)
        height = float(height)

        # Проверка на отрицательные числа и 0
        if base <= 0 or height <= 0:
            show_error("Основание и высота имеют только положительные числа")
            return

        area = 0.5 * base * height
        show_result(area)

    except ValueError:
        show_error("Введите числа")


def calculate_area_with_sides_and_angle(a, b, alpha):
    try:
        a, b = float(a), float(b)

        # Проверка на отрицательные числа и 0 для сторон a и b
        if a <= 0 or b <= 0:
            show_error("Стороны должны быть положительными числами.")
            return

        # Проверка на допустимый диапазон угла alpha
        alpha = float(alpha)
        if alpha < 0 or alpha > 180:
            show_error("Угол должен быть между 0 и 180 градусами.")
            return

        alpha_rad = math.radians(alpha)
        area = 0.5 * a * b * math.sin(alpha_rad)
        show_result(area)

    except ValueError:
        show_error("Неверный ввод, пожалуйста, введите числовые значения.")


def calculate_area_with_three_sides(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)

        # Проверка на отрицательные числа и 0 для сторон a, b и c
        if a <= 0 or b <= 0 or c <= 0:
            show_error("Стороны должны быть положительными числами.")
            return

        # Проверка на неравенство треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            show_error("Стороны не могут образовать треугольник.")
            return

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        show_result(area)

    except ValueError:
        show_error("Неверный ввод, пожалуйста, введите числовые значения.")

# Функции для отображения результата и обработки ошибок
def show_result(area):
    area = round(area, 2)
    result_label.config(text=f'Площадь треугольника равна {area}', fg='black')
    result_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))
    back_btn.grid(row=9, column=0, columnspan=2, pady=(10, 10))

def show_error():
    result_label.config(text='Ошибка: введите корректные значения.', fg='red')
    result_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))
    back_btn.grid(row=9, column=0, columnspan=2, pady=(10, 10))

# Очистка полей ввода и результата
def clear_input_fields_and_result():
    for widget in [result_label, back_btn, calc_btn, image_label]:
        widget.grid_forget()

    for _, ent in input_fields:
        ent.delete(0, tk.END)

    for lbl, ent in input_fields:
        lbl.grid_forget()
        ent.grid_forget()

# Настройка полей ввода
def setup_input_fields(fields):
    for lbl, ent, row in fields:
        lbl.grid(row=row, column=0, pady=10, sticky="ew")
        ent.grid(row=row, column=1, pady=10, sticky="ew")

# Обновление изображения
def update_image(image_path):
    try:
        pil_image = Image.open(image_path)
        pil_image.thumbnail((300, 200))
        image = ImageTk.PhotoImage(pil_image)
        image_label.config(image=image)
        image_label.image = image
        image_label.grid(row=7, column=0, columnspan=2, pady=(10, 10))
    except Exception as e:
        print(f"Не удалось загрузить изображение: {e}")

# Обработка выбора метода расчета
def selected(event):
    clear_input_fields_and_result()
    selection = combobox.get()

    if selection == "Через основание и высоту":
        method_with_base_and_height()
    elif selection == "Через две стороны и угол":
        method_with_sides_and_angle()
    elif selection == "Через три стороны":
        method_with_three_sides()

# Определение методов регулирования
def method_with_base_and_height():
    fields = [(base_lbl, base_ent, 3), (height_lbl, height_ent, 4)]
    setup_input_fields(fields)
    calc_btn.config(command=lambda: calculate_area_with_base_and_height(base_ent.get(), height_ent.get()))
    calc_btn.grid(row=5, column=0, columnspan=2, pady=10)
    update_image(r"Step 1.jpg")


def method_with_sides_and_angle():
    fields = [(a_lbl, a_ent, 3), (b_lbl, b_ent, 4), (alpha_lbl, alpha_ent, 5)]
    setup_input_fields(fields)
    calc_btn.config(command=lambda: calculate_area_with_sides_and_angle(a_ent.get(), b_ent.get(), alpha_ent.get()))
    calc_btn.grid(row=6, column=0, columnspan=2, pady=10)
    update_image(r"Step 2.jpg")


def method_with_three_sides():
    fields = [(a_lbl, a_ent, 3), (b_lbl, b_ent, 4), (c_lbl, c_ent, 5)]
    setup_input_fields(fields)
    calc_btn.config(command=lambda: calculate_area_with_three_sides(a_ent.get(), b_ent.get(), c_ent.get()))
    calc_btn.grid(row=6, column=0, columnspan=2, pady=10)
    update_image(r"Step 3.jpg")


# Функция для открытия калькулятора площади квадрата с переходом
def open_square_area_calculator():
    fade_out()


def fade_out():
    alpha = 1.0  # Начальная прозрачность

    def update_opacity():
        nonlocal alpha
        alpha -= 0.05  # Уменьшаем прозрачность
        if alpha > 0:
            window.attributes("-alpha", alpha)
            window.after(50, update_opacity)  # Запланировать следующее обновление
        else:
            window.attributes("-alpha", 0)  # Полностью прозрачное
            open_square_calculator()  # Открыть новый калькулятор

    update_opacity()


def open_square_calculator():
    # Настройка интерфейса калькулятора площади квадрата
    square_window = tk.Toplevel(window)
    square_window.title("Калькулятор площади квадрата")
    square_window.geometry("1000x500+1000+0")
    window.attributes("-alpha", 1)  # Возвращаем прозрачность

    # Создание элементов для калькулятора площади квадрата
    square_label = tk.Label(square_window, text="Введите длину стороны квадрата:", bg="#e0f7fa", font=('Helvetica', 12))
    square_label.pack(pady=(20, 0))

    square_entry = tk.Entry(square_window)
    square_entry.pack(pady=(0, 20))

    # Функция для расчета площади
    def calculate_square_area():
        side_length_str = square_entry.get()
        try:
            side_length = float(side_length_str)
            if side_length < 0:
                raise ValueError("Длина стороны не может быть отрицательной.")
            area = side_length ** 2
            messagebox.showinfo("Результат", f"Площадь квадрата: {area}")
            square_window.destroy()  # Закрываем приложение после нажатия "OK"
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Некорректное значение: {e}")


    # Кнопка для расчета
    calculate_square_button = tk.Button(square_window, text="Рассчитать площадь квадрата",command=calculate_square_area)
    calculate_square_button.pack(pady=20)




# Функция для переключения полноэкранного режима
def toggle_fullscreen():
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)


# Заголовок
method_lbl = tk.Label(window, text="Выберите способ расчёта площади треугольника", bg="#e0f7fa",
                      font=('Helvetica', 16, 'bold'))
method_lbl.grid(row=0, column=0, columnspan=2, pady=10)

# Кнопка для полноэкранного режима
fullscreen_btn = tk.Button(window, text="Полный экран", command=toggle_fullscreen, bg='green', fg='white')
fullscreen_btn.grid(row=0, column=10, sticky='ne')  # Устанавливаем кнопку в правом верхнем углу

# Комбобокс для выбора метода
methods = ["Через основание и высоту", "Через две стороны и угол", "Через три стороны"]
combobox = Combobox(window, values=methods, width=40, state="readonly")
combobox.set("Через основание и высоту")
combobox.bind("<<ComboboxSelected>>", selected)
combobox.grid(row=1, column=0, columnspan=2, pady=10)


# Элементы ввода для калькулятора треугольника
input_fields = [
    (base_lbl := tk.Label(window, text="Основание:", font=('Helvetica', 12)), base_ent := tk.Entry(window)),
    (height_lbl := tk.Label(window, text="Высота:", font=('Helvetica', 12)), height_ent := tk.Entry(window)),
    (a_lbl := tk.Label(window, text="Сторона 'a':", font=('Helvetica', 12)), a_ent := tk.Entry(window)),
    (b_lbl := tk.Label(window, text="Сторона 'b':", font=('Helvetica', 12)), b_ent := tk.Entry(window)),
    (c_lbl := tk.Label(window, text="Сторона 'c':", font=('Helvetica', 12)), c_ent := tk.Entry(window)),
    (alpha_lbl := tk.Label(window, text="Угол (в градусах):", font=('Helvetica', 12)), alpha_ent := tk.Entry(window)),
]

# Метка для результата
result_label = tk.Label(window, text='', bg="#e0f7fa", font=('Helvetica', 12))
# Кнопка "Вернуться"
back_btn = tk.Button(window, text="Вернуться", command=clear_input_fields_and_result, bg='red', fg='white')
# Кнопка "Рассчитать площадь"
calc_btn = tk.Button(window, text="Рассчитать площадь", bg='green', fg='white', activebackground='darkgreen')

# Метка для изображения (если есть)
image_label = tk.Label(window, bg="#e0f7fa")

# Кнопка для открытия калькулятора площади квадрата
square_calc_button = tk.Button(window, text="Калькулятор площади квадрата", command=open_square_area_calculator, bg='blue', fg='white')
square_calc_button.grid(row=10, column=0, columnspan=2, pady=(10, 0))

# Запуск основного цикла
window.mainloop()
