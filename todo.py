def task():
    tasks = []
    print("------Welcome to the To-Do list Application------")

    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range (1,total_tasks+1):
        task_name = input(f"Enter task {i}:")
        tasks.append(task_name)

    print(f"\n you have today added {total_tasks} taks to your To-Do list")
    print(f"Today tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\nChoose your operation: "))
        if operation == 1:
            add = int(input("How many tasks you want to add?"))
            for j in range (1,add+1):
                new_task = input("Enter new task:")
                tasks.append(new_task)
                print(f"New {add} tasks add successfully")

        elif operation == 2:
            print(f"Your current tasks are:\n{tasks}")
            update = int(input("Enter the method of updating tasks\n 1-By index number \n 2-By task name \n Choose your operation: "))
            if update == 1:
                print(f"Your current tasks are:\n{tasks}")
                update_index = int(input("Enter the task number you want to update: "))
                if 1 <= update_index <= len(tasks):
                    up_task = input("Enter the updated task:")
                    tasks[update_index - 1] = up_task
                    print("Task updated successfully")
                else:
                    print("Invalid task number whatever you want to update !! ")
            elif update == 2:
                print(f"Your current tasks are:\n{tasks}")
                update_name = input("Enter the task name what you want to update: ")
                if update_name in tasks:
                    up_to_do = input("Enter update task: ")
                    ind = tasks.index(update_name)
                    tasks[ind] = up_to_do
                    print("Tasks Update successfully.")
                else:
                    print("Invalid method choice for updation !!")


        elif operation == 3:
            print(f"Your current tasks are:\n{tasks}")
            delete = int(input("Enter the method of deleting tasks\n 1-By index number \n 2-By task name \n Choose your operation: "))
            if delete == 1:
                print(f"Your current tasks are:\n{tasks}")
                delete_index = int(input("Enter the task number you want to delete:"))
                if 1 <= delete_index <= len(tasks):
                    tasks.pop(delete_index - 1)
                    print("Task deleted successfully")
                else:
                    print("Invalid task number whatever you want to delete !! ")

            elif delete == 2:
                print(f"Your current tasks are:\n{tasks}")
                delete_To_Do = input("Enter the task name you want to delete: ")
                if delete_To_Do in tasks:
                    tasks.remove(delete_To_Do)
                    print(f"Task '{delete_To_Do}' deleted successfully")
            else:
                print("Invalid delete method options !!")

        elif operation == 4:
            print(f"your current tasks are:\n{tasks}")


        elif operation == 5:
            print("**********Thankyou for visiting*********** ")
            break

        else:
            print("!!!! Invalid operation choice !!!!")

task()
