"""skebob — этап 1: простой цикл «ввод → ответ».

Запуск:  python3 main.py
Выход:   введите  exit  (или нажмите Ctrl+C)
"""

EXIT_COMMANDS = {"exit", "quit", "выход"}


def respond(text: str) -> str:
    """Принимает строку от пользователя и возвращает ответ.

    Пока это просто «эхо». На следующих этапах здесь появятся
    команды для заметок, а потом — агент.
    """
    text = text.strip()
    if not text:
        return "Напишите что-нибудь 🙂"
    if text.lower() == "help":
        return "Я пока умею только повторять за вами. Команды: help, exit."
    return f"Вы сказали: {text}"


def main() -> None:
    print("Привет! Я skebob. Напишите что-нибудь (help — подсказка, exit — выход).")
    while True:
        try:
            text = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nПока!")
            break

        if text.strip().lower() in EXIT_COMMANDS:
            print("Пока!")
            break

        print(respond(text))


if __name__ == "__main__":
    main()
