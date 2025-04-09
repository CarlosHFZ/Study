# def execute_command(command: str):
#     match command:
#         case 'ls':
#             print('$ listing fiels')

#         case 'cd':
#             print('$ changing directory')

#         case _:
#             print("$ command not implemented")


# execute_command('pwd')

# def execute_command(command):
#     match command.split():
#         case ['ls', *directories, '--force']:
#             for directory in directories:
#                 print('$ listing fiels FORCED', directory)

#         case ['ls', *directories]:
#             for directory in directories:
#                 print('$ listing fiels files', directory)

#         case ['cd', path, *_]:
#             print('$ changing directory to', path)

#         case _:
#             print("$ command not implemented")



# execute_command('ls /home /users /etc --force')
# execute_command('ls /home /users /etc')


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories,]:
#             for directory in directories:
#                 print('$ listing fiels from', directory)

#         case ['cd' | 'change', path, *_]:
#             print('$ changing directory to', path)

#         case _:
#             print("$ command not implemented")
#     print('...rest of the code')

# execute_command('ls /home /users /etc')
# execute_command('change /etc')


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)

#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing ONE directory from', directories[0])

#         case ['cd' | 'change', path, *_]:
#             print('$ changing directory to', path)

#         case _:
#             print("$ command not implemented")
#     print('...rest of the code')


# execute_command('ls /home /users /etc')
# execute_command('ls /etc')


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)
#             print(f'{the_command=}, {the_list=}')
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing ONE directory from', directories[0])

#         case ['cd' | 'change', path, *_]:
#             print('$ changing directory to', path)

#         case _:
#             print("$ command not implemented")
#     print('...rest of the code')


# execute_command('ls /home /users /etc')
# execute_command('ls /etc')



# def execute_command(command):
#     match command:
#         case {'command': 'ls', 'directories': [_, *_]}:
#             for directory in command['directories']:
#                 print('$ listing ALL directories from', directory)
#         case _:
#             print("$ command not implemented")
#     print('...rest of the code')


# execute_command({'command': 'ls', 'directories': ['/users', '/home']})


from dataclasses import dataclass


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command):
    match command:

        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)

        case Command(command=_, directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case _:
            print("$ command not implemented")

    print('...rest of the code')

command_1 = Command('ls', ['/users'])
command_2 = Command('ls', ['/users'])

execute_command(command_1)
execute_command(command_2)