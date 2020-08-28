from src import commands


mapping = {
    'save': commands.save,
    'get': commands.get,
    'delete': commands.delete,
    'exit': None
}


if __name__ == "__main__":
    while True:
        command = input('>')
        if command == "exit":
            break
        if command in mapping.keys():
            mapping[command]()
            continue
        print("Invalid command. These commands are allowed: %s " % [*mapping])
