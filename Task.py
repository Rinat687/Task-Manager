# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач,
#  отметки выполненных задач и вывода списка текущих (не выполненных) задач.



# class Task():
#     def __init__(self,task_description, due_date, status):
#         self.task_description = task_description
#         self.due_date = due_date
#         self.status = status

class Task:
    def __init__(self, description, due_date):
        self.description = description  # Описание задачи
        self.due_date = due_date  # Срок выполнения задачи
        self.completed = False  # Статус выполнения задачи

    def mark_completed(self):
        # Отметить задачу как выполненную.
        self.completed = True

    def __str__(self):
        # Возвращает строковое представление задачи.
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, description, due_date):
            #Добавить новую задачу.
        new_task = Task(description, due_date)  # Создаем экземпляр Task
        self.tasks.append(new_task)  # Добавляем задачу в список

    def mark_task_completed(self, task_index):
        #Отметить задачу как выполненную по индексу.
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()  # Используем метод класса Task
        else:
            print("Ошибка: Индекс задачи вне диапазона.")

    def get_current_tasks(self):
       #Вывести список текущих (не выполненных) задач.
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):

        if not self.tasks:  # Выводит все задачи с их статусами.
            print("Список задач пуст.")
            return

        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Купить продукты", "2024-11-20")  # Здесь используется класс Task
    manager.add_task("Сделать домашнее задание", "2024-11-18")  # Здесь используется класс Task

    # Вывод всех задач
    print("Все задачи:")
    manager.display_tasks()

    # Отметка задачи как выполненной
    manager.mark_task_completed(0)

    # Вывод текущих задач после отметки
    print("\nТекущие задачи после выполнения первой:")
    current_tasks = manager.get_current_tasks()

    if current_tasks:
        for task in current_tasks:
            print(task)
    else:
        print("Нет текущих задач.")

