import argparse
class Task:
    def __init__(self, id, title, description,completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    def mark_as_completed(self):
        self.completed = True
class TaskManager:
    def __init__(self):
        self.tasks = {}
    def add_task(self, title, description):
        id = len(self.tasks) + 1
        task = Task(id, title, description)
        self.tasks[id] = task
        return task
    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
            print(f"Task removed: ID {id}")
        else:
            print(f"Task is not found.")
            
            
    def mark_task_completed(self, id):
        task = self.find_task(id)
        if task:
            task.mark_as_completed()
    def list_tasks(self):
        for id, task in self.tasks.items():
            print(f"ID: {id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")
    def find_task(self, id):
        return self.tasks.get(id)
    
    def Save(self):
        with open("text.txt",'w') as file:
            for id,task in self.tasks.items():
                file.write(str(id)+"|"+task.title+"|"+task.description+"|"+str(task.completed)+"\n")      
                

def read_from_text(tasks):
    with open("text.txt", "r") as file:
       for line in file:
        data = line.strip().split("|")
        task = Task(data[0], data[1], data[2], data[3])
        tasks[len(tasks) + 1]=task
    return tasks
def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    add_task_parser = subparsers.add_parser('add_task')
    add_task_parser.add_argument('-title')
    add_task_parser.add_argument('-description')
    
    remove_task_parser = subparsers.add_parser('remove_task')
    remove_task_parser.add_argument('-id')
    
    mark_task_completed_parser = subparsers.add_parser('mark_task_completed')
    mark_task_completed_parser.add_argument('-id')
    
    list_tasks_parser = subparsers.add_parser('list_tasks')
    find_task_parser = subparsers.add_parser('find_task')
    find_task_parser.add_argument('-id')
    args = parser.parse_args()
    
    task_manager = TaskManager()
    
    task_manager.tasks = read_from_text(task_manager.tasks)
    
    if args.command == 'add_task':
        task = task_manager.add_task(args.title, args.description)
        print(f"Task added: ID: {task.id}, Title: {task.title}, Description: {task.description}")
    elif args.command == 'remove_task':
        task_manager.remove_task(int(args.id))
    elif args.command == 'mark_task_completed':
        task = task_manager.find_task(int(args.id))
        if task:
            task.mark_as_completed()
            print(f"Task marked as completed: ID {args.id}")
        else:
            print(f"Task not found: ID {args.id}")
    elif args.command == 'list_tasks':
        task_manager.list_tasks()
    elif args.command == 'find_task':
        task1 = task_manager.find_task(int(args.id))
        if task1:
            print(f"Task: ID: {task1.id}, Title: {task1.title}, Description: {task1.description}")
        else:
            print("None")
    task_manager.Save()
if __name__ == '__main__':
    main()        
