from queue import PriorityQueue as Priority_Queue

current_tasks = dict()
priority_idx = Priority_Queue()
newest_id = 0

def add_task(description, priority):
    new_task = {
        "id": newest_id,
        "description": description,
        "priority": priority,
        "status": "incomplete"
    }

    current_tasks[new_task["id"]] = new_task
    priority_idx.put_nowait((new_task["priority"], new_task["id"]))

    return current_tasks[new_task["id"]]


user_choice = None
while True:
    user_choice = input("choice: ")
    
    match user_choice:

        case "1":
            description = input("Enter a description for the new task: ")
            priority = input("Enter a priority for the new task: ")

            new_task = add_task(description, int(priority))
            newest_id += 1
            print(new_task)

        case "2":
            # Get task by priority
            # print(next_task)
            pass

        case "3":
            id = input("Enter the task's id: ")

            # Get task by id
            # print(found_task))

        case "4":
            id = input("Enter the task's id: ")

            # Mark task as complete with id
            # print(task)

        case "quit":
            print("Shutting down...")
            break

        case _:
            print("You must choose 1, 2, 3, or 4")


quit()