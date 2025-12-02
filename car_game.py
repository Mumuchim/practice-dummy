started = False

while True:
    user_input = input("Start Game? ")
    if user_input.lower() == "start":
        if started:
            print("Game already started.")
        else:
            started = True
            print("Game started!")
    elif user_input.lower() == "stop":
        if not started:
            print("Game is not started yet.")
        else:
            started = False
            print("Game stopped.")

    elif user_input.lower() == "help":
        print("Type \n'start' to begin the game \n'stop' to stop the game \n'quit' to exit.")
    elif user_input.lower() == "quit":
        print("Exiting the game. Goodbye!")
        break

    else:
        print("Invalid command. Type 'help' for assistance.")
