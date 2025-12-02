import json

name = "To_do_List.json"





class Task:
    def __init__(self, text, done = False):
        self.text = text
        self.done = done
    def make_task(self):
        return {"text" : self.text, "done" : self.done}
    def write(cls, tasks):
        return cls(tasks["text"], tasks["done"])
    def tick(self):
        tick1 = "✓" if self.done else ""
        return f'[{tick1}]{self.text}'
class Control:
    def __init__(self, w = "To_do_List.json"):
        self.w = w
        self.s = []
        self.task_load()
    def task_load(self):
        try:
            with open(self.w, 'r') as f:
                task_check = json.load(f)
                self.s = [Task.write() for tesk in task_check]
            print("Task loaded")
        except(json.JSONDecodeError, UnicodeDecodeError):
            print("Task didnt open")
            self.s = []
    def save(self):
        with open(self.w, 'w') as f:
            task_check = [i.tick() for i in self.s]
            json.dump(task_check, f, ensure_ascii=False)
    def add_list(self, text):
        i = Task(text)
        self.s.append(i)
        print("Task done")
        self.save()
    def task_show(self):
        if not self.s:
            print("Task empty")
        return
        print("List of tasks")
        for tick2 , i in enumerate(self.s, 1):
            print(f"{tick2}, {i}")
        print(f"Total tasks:{len(self.s)}")
    def task_finish(self, task_num):
        one = task_num-1
        if 0 <= one <= len(self.s):
            self.s[one].done = True
            print(f"Task done{self.s[one]}")
            self.save()
        else:
            print("task not found")
    def task_delete(self, task_num):
        one = task_num-1
        if 0 <= one <= len(self.s):
            i = self.s.pop(one)
            print(f"Task deleted{self.s[one]}")
        else:
            print("Task not found")
class View_tasks:
    def __init__(self):
        self.name = "To_do_List.json"
    def open_task_menu(self):
        print("Task manager")
        print("Pick options")
        print("1 = Add task")
        print("2 = Delete task")
        print("3 = View task")
        print("4 = Tick done")
        print("5 = Finish")
        print("6 = Save")
    def help_add_task(self):
        text = input("Enter task: ")
        if text:
            self.name.add_list(text)
        else:
            print("Task empty")
    def turn_task_into_done(self):
        self.name.task_load()
        if self.name.i:
            task_num = int(input("Enter task number: "))
            self.name.task_finish(task_num)
        else:
            print("Number doesnt exist")
    def turn_task_deleted(self):
        self.name.task_load()
        if self.name.i:
            task_num = int(input("Enter task number: "))
            self.name.task_delete(task_num)
        else:
            print("Number doesnt exist")
    def task_startup(self):
        print("This is the list of tasks: ")
        while True:
            self.open_task_menu()
            task_num2 = input("Pick task number")
            if task_num2 == "1":
                self.help_add_task()
            if task_num2 == "4":
                self.turn_task_into_done()
            if task_num2 == "2":
                self.turn_task_deleted()
            if task_num2 == "6":
                self.save()
            if task_num2 == "5":
                break
if __name__ == "__main__":
    app = View_tasks()