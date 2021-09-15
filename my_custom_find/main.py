from find_duplicate_files import duplicate_files_generator
from find_large_files import large_files_generator
from images_generator import images_generator
from old_file_generator import old_file_generator
from output import output
from args_parser_settings import parser_add_args, parser


def main():
    parser_add_args()  # Add arguments to our arguments parser

    if parser.parse_args().argument == "duplicates":
        output(duplicate_files_generator(
            parser.parse_args().path), parser.parse_args().o)

    elif parser.parse_args().argument == "large":
        output(large_files_generator(
            parser.parse_args().path,
            parser.parse_args().size), parser.parse_args().o)

    elif parser.parse_args().argument == "images":
        output(images_generator(
            parser.parse_args().path), parser.parse_args().o)

    elif parser.parse_args().argument == "old":
        output(old_file_generator(
            parser.parse_args().path), parser.parse_args().o)

    else:
        raise TypeError


if __name__ == '__main__':
    main()
