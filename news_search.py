"""
This script is used to print the reference of the documents with respect to the seach criterion OR and AND on the query strings.
"""

from argparse import ArgumentParser
import sys


def get_content_from_file(file_name):
    """
    This helper method is used to read the contents of the file.
    :param file_name: Filename to read contents
    :return: Read contents as a list of line separted stringa.
    """
    with open(file_name, 'r') as file_read:
        document_content = file_read.readlines()
    file_read.close()
    return document_content


def main(arguments=None):
    """
    This the main method that will read the contents of hscic-news, and then based on the query and search criteria, will display the document reference.
    :param arguments:
    :return: The referenced documents after OR and AND search criterion.
    """
    argv = sys.argv[1:] if arguments is None else arguments
    parser = ArgumentParser()
    parser.add_argument('--query', metavar='query', help='Search Query')
    parser.add_argument('--search-type', metavar='search_type', help='Seach type either OR or AND')

    args = parser.parse_args(argv)

    document = ''
    ref_document = set()

    try:
        if args.search_type is None and args.query is None:
            parser.print_help()
        elif args.search_type is None:
            parser.print_help()
        elif args.query is None:
            parser.print_help()
        else:
            query_string = args.query
            search_type = args.search_type
            if search_type.upper() == 'OR':
                query = query_string.split(",")
                document_content = get_content_from_file('hscic-news')
                for x in range(len(document_content)):
                    for query_param in query:
                        if query_param in document_content[x]:
                            ref_document.add(x)
            elif search_type.upper() == 'AND':
                query = query_string.split(",")
                counter = 0
                document_content = get_content_from_file('hscic-news')
                for x in range(len(document_content)):
                    for query_param in query:
                        if query_param in document_content[x]:
                            counter += 1
                        else:
                            counter = 0
                        if counter == len(query):
                            ref_document.add(x)
            else:
                raise Exception('You have passed a wrong search criteria, please pass search type either as OR or AND')
            ref_document = sorted(ref_document)
            document = ','.join(str(x) for x in ref_document)
        return document
    except Exception as e:
        print(str(e))
        exit()


if __name__ == '__main__':
    main()
