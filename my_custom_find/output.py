def output(command, file=None):
    if file:
        write_to_file(command, file)
    else:
        output_to_console(command)


def output_to_console(command):
    print(f'{work_info(command)}\n')
    for text in command:
        print(text)


def write_to_file(command, log_file):
    try:
        with open(log_file, 'w') as file:
            file.write(work_info(command))
            for text in command:
                file.write(f'\n{text}')
        return True
    except IOError:
        print(f'Could not write to file: {file}')
        exit()


def work_info(text_iter):
    arguments_dict = {'duplicate_files_generator': 'Result of working MY CUSTOM FIND -duplicates:',
                      'large_files_generator': 'Result of working MY CUSTOM FIND -large files:',
                      'images_generator': 'Result of working MY CUSTOM FIND -images:',
                      'old_file_generator': 'Result of working MY CUSTOM FIND -old files:'}
    argument = str(text_iter).split()[2]  # Get a name of generator
    return arguments_dict[argument]
