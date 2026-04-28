tasks = []

def show_tasks():
    if not tasks:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена")

def delete_task():
    show_tasks()
    try:
        num = int(input("Введите номер задачи для удаления: "))
        tasks.pop(num - 1)
        print("Задача удалена")
    except:
        print("Ошибка")

def main():
    while True:
        print("\n1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Выход...")
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()