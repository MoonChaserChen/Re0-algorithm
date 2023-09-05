def parse(idx, s):
    commands = []
    command_open = False

    command = ""
    for x in s:
        if x == '"':
            command += '"'
            command_open = not command_open
        elif x == '_':
            if command_open:
                command += x
            elif command != "":
                commands.append(command)
                command = ""
        else:
            command += x
    if command != "":
        commands.append(command)
    le = len(commands)
    if idx < 0 or idx > le - 1:
        return "ERROR"
    result = ""
    for i, x in enumerate(commands):
        if i == idx:
            result += "_******"
        else:
            result += "_" + x
    return result[1:]


print(parse(int(input()), input()))