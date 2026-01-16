


user_choice = None
while True:
    user_choice = input("choice: ")

    try:
        match user_choice:

            case "1":
                description = input("Enter a description for the new task: ")
                priority = input("Enter a priority for the new task: ")

                # Add task
                #print(new_task)

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

    except:
        print("An error occured. Please try again")


quit()