import os
from datetime import datetime
import json


task_file = "tasks.json"
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, "r") as file :
            return json.load(file)
    else :
        return []

def write_tasks(tasks):
    with open(task_file, "w") as file :
        json.dump(tasks, file, indent = 2)

def add_tasks(tasks, title, description, due_date) : 
     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     task = {"title": title, "description" : description, "due_date" : due_date, "completed" : False, "createdAt" : now, "updatedAt" : now}
     tasks.append(task)
     write_tasks(tasks)
     print("Task(s) added successfully.")

def list_tasks(tasks):
    for index, task in enumerate(tasks, start = 1) :
        print(f"{index}. {task['title']} - Due : {task['due_date']} - {'Completed' if task['completed'] else 'Incomplete'} - Created On : {task['createdAt']} - Last Updated: {task['updatedAt']}")

def update_tasks(tasks, title, description, due_date, index) : 
    if 0 < index <= len(tasks) :        
        task = tasks[index - 1]
        task['title'] = title
        task['description'] = description
        task['due_date'] = due_date
        task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_tasks(tasks)
        print("Tasks updated successfully!")
    else :
        print("Error! Invalid index input!")

def delete_tasks(tasks, index):
    if 0 < index <= len(tasks) :
        task = tasks[index-1]
        tasks.remove(task)
        write_tasks(tasks)
        print("Task deleted successfully!")
    else :
        print("Error! Invalid index input!")

def search_tasks(tasks, index) :
    if 0 < index <= len(tasks) :
        task = tasks[index - 1]
        print("\n--- Task Details ---")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {'Completed' if task['completed'] else 'Incomplete'}")
        print(f"Created At:  {task['createdAt']}")
        print(f"Updated At:  {task['updatedAt']}")
        print("--------------------")
        print("Task shown successfully!")
    else :
        print("Error! Invalid index input!")

def mark_task_complete(tasks, index):
    if 0 < index <= len(tasks) :
        task = tasks[index-1]
        task['completed'] = True
        task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_tasks(tasks)
        print("Task marked as complete successfully!")
    else :
        print("Error! Invalid index input!")

def mark_task_inprog(tasks, index):
    if 0 < index <= len(tasks) :
        task = tasks[index-1]
        task['completed'] = "In-Progress"
        task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_tasks(tasks)
        print("Task marked as in-progress successfully!")
    else :
        print("Error! Invalid index input!")

def show_task_incomplete(tasks) :
    incomplete_tasks = []
    for task in tasks :
        if task['completed'] == False :
            incomplete_tasks.append(task)
    if incomplete_tasks :
        print("\n--- INCOMPLETE TASKS ---")
        for tsk in incomplete_tasks:
            print(f"Title       : {tsk['title'].strip()}")
            print(f"Description : {tsk['description'].strip()}")
            print("Status      : Incomplete")
            print("-----------------------")
        print("Listed incomplete tasks!")   
    else :
        print("Incomplete tasks not found!")
    

def show_task_complete(tasks) :
    completed_tasks = []
    for task in tasks :
        if task['completed'] == True :
            completed_tasks.append(task)
    if completed_tasks :
        print("\n--- COMPLETED TASKS ---")
        for tsk in completed_tasks:
            print(f"Title       : {tsk['title'].strip()}")
            print(f"Description : {tsk['description'].strip()}")
            print("Status      : Completed")
            print("-----------------------")
        print("Listed completed tasks!")
    else :
        print("Incomplete tasks not found!")
    

def show_task_inprog(tasks) :
    inprog_tasks = []
    for task in tasks :
        if task['completed'] == "In-Progress" :
            inprog_tasks.append(task)
    if inprog_tasks :
        print("\n--- IN-PROGRESS TASKS ---")
        for tsk in inprog_tasks:
            print(f"Title       : {tsk['title'].strip()}")
            print(f"Description : {tsk['description'].strip()}")
            print("Status      : In-Progress")
            print("-----------------------")
        print("Listed in-progress tasks!")
    else :
        print("Incomplete tasks not found!")
    


def main(): 
    tasks = load_tasks()
    is_running = True
    while is_running :
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Search Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Mark Complete")
        print("7. Mark In-Progress")
        print("8. Search completed Tasks")
        print("9. Search incomplete Tasks")
        print("10. Search in-progress tasks")
        print("11. Exit")

        choice = input("Enter choice (1-11) :")  
        if choice ==  "1" :
            title = input("Enter title :")
            desc = input("Enter description :")
            due_date = input("Enter due date : (YYYY-MM-DD)")
            add_tasks(tasks, title, desc, due_date)
            
        elif choice == "2" :
            list_tasks(tasks)
            
        elif choice == "3" :
            index = int(input("Enter index to find task :"))
            search_tasks(tasks, index)
            
        elif choice == "4" :
            index = int(input("Enter index to update the task :"))
            title = input("Enter updated title :")
            desc = input("Enter updated description :")
            due_date = input("Enter updated due-date :")
            update_tasks(tasks, title, desc, due_date, index)
            
        elif choice == "5" :
            index = int(input("Enter index to delete the task :"))
            delete_tasks(tasks, index)
        
        elif choice == "6" :
            index = int(input("Enter index to mark the task as complete :"))
            mark_task_complete(tasks, index)

        elif choice == "7":
            index = int(input("Enter index to mark the task in-progress :"))
            mark_task_inprog(tasks,index)

        elif choice == "8" :
            show_task_complete(tasks)
            print()
        
        elif choice == "9":
            show_task_incomplete(tasks)
            print()

        elif choice == "10":
            show_task_inprog(tasks)
            print()

        elif choice == "11":
            print("Goodbye!")
            is_running = False

        else :
            print("Invalid option, Try again.")

if __name__ == "__main__" :
    main()
