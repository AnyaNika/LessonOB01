# Менеджер задач
#
# Задача: Создай класс `Task`, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline, status = "Не выполнено"):
        self.description = description
        self.deadline = deadline
        self.status = status

    def add_task(self):
        print(f'Задача {self.description} добавлена.')
        self.status = "Не выполнено"
        todo_list.append(self.description)

    def done_task(self):
        print(f'Задача {self.description} выполнена.')
        self.status = "Выполнено"
        todo_list.remove(self.description)

def task_info():
    print("Список текущих задач:")
    print(todo_list)
    print()

todo_list = []

task1 = Task("Помыть посуду", "22 часа")
task2 = Task("Поработать", "4.03.2025")
task3 = Task("Сходить в кино", "7.03.2025")

task1.add_task()
task_info()

task2.add_task()
task_info()

task3.add_task()
task_info()

task1.done_task()

task_info()