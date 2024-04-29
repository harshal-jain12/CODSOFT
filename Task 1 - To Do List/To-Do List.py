#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {'description': task_description, 'completed': False}
        print("Task added successfully!")

    def view_tasks(self):
        print("To-Do List:")
        if self.tasks:
            for task_id, task in self.tasks.items():
                status = "Completed" if task['completed'] else "Pending"
                print(f"{task_id}. {task['description']} - {status}")
        else:
            print("No tasks in the list.")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f"Task {task_id} marked as completed.")
        else:
            print("Task not found.")


def main():
    todo_list = TodoList()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.complete_task(task_id)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# In[ ]:




