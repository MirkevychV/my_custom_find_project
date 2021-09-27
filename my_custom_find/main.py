from my_custom_find.find_duplicate_files import duplicate_files_generator
from my_custom_find.find_large_files import large_files_generator
from my_custom_find.images_generator import images_generator
from my_custom_find.old_file_generator import old_file_generator
from my_custom_find.output import output
from my_custom_find.args_parser_settings import parser_add_args, parser


def main():
    parser_add_args()  # Add arguments to our arguments parser

    # Initialize arguments
    path_arg = parser.parse_args().path
    output_arg = parser.parse_args().output
    size_arg = parser.parse_args().size

    if parser.parse_args().argument == "duplicates":
        output(duplicate_files_generator(path_arg),
               output_arg)

    elif parser.parse_args().argument == "large":
        output(large_files_generator(path_arg, size_arg),
               output_arg)

    elif parser.parse_args().argument == "images":
        output(images_generator(path_arg),
               output_arg)

    elif parser.parse_args().argument == "old":
        output(old_file_generator(path_arg),
               output_arg)

    else:
        raise TypeError


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError as e:
        print(f'Path is not valid')
    except ValueError as e:
        print(f'Invalid format of size')
    except IOError as e:
        print(f'Could not write to file')
    finally:
        exit(2)
