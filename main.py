import tkinter as tk
import random

answers = [
    "Да, конечно! ✨",
    "Нет, увы 💭",
    "Пока не ясно 🔮",
    "Лучше не знать ответ 😅",
    "Скоро всё станет понятно 🌙"
]

def get_answer():
    question = question_entry.get()
    if question.strip() == "":
        result_label.config(text="Сначала задай вопрос! 🌀")
    else:
        result = random.choice(answers)
        result_label.config(text="🔮 " + result)

# создаём окно
window = tk.Tk()
window.title("Магический Шар Судьбы 🔮")
window.geometry("400x300")
window.configure(bg="#1e1e2f")

# заголовок
title_label = tk.Label(window, text="Магический Шар Судьбы", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
title_label.pack(pady=10)

# поле ввода вопроса
question_entry = tk.Entry(window, width=40, font=("Arial", 12))
question_entry.pack(pady=10)

# кнопка
ask_button = tk.Button(window, text="Спросить ✨", command=get_answer, bg="#6c5ce7", fg="white", font=("Arial", 12, "bold"))
ask_button.pack(pady=10)

# место для результата
result_label = tk.Label(window, text="", font=("Arial", 14), bg="#1e1e2f", fg="white")
result_label.pack(pady=20)

# запускаем приложение
window.mainloop()