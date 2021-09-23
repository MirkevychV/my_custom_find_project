import argparse


class MyParser(argparse.ArgumentParser):
    """
    A child-class of ArgumentParser class. We change output, when
    script starts without arguments.

    """

    def error(self, message):
        print(f'Error: {message}')
        self.print_help()
        exit()  # Close a program


# Creating parser from MyParser(child class of argparse.ArgumentParser)
parser = MyParser()


def parser_add_args():
    parser.add_argument('-o', '--output', type=str,
                        help='Output result to the file <-o "filename.txt">')
    parser.add_argument('-size', type=str,
                        help='Enter size of the files')
    parser.add_argument(choices=['duplicates', 'large', 'images', 'old'],
                        dest='argument',
                        help='duplicates - Search for identical files in the specified path,'
                             'large - Search files larger than the specified size,'
                             'images - Searches for image files,'
                             'old - Searches for files older than one year')

    parser.add_argument("path", help="Directory path")
