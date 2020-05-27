import sys
from whenis.date_lexer import *


def main():
    date_input = sys.argv[1]
    date_lexer = DateLexer(date_input)

    token = date_lexer.next()
    while token.token_type is not DateTokenType.EOF:
        print("type: {}, value: {}".format(token.token_type, token.token_value))
        token = date_lexer.next()


if __name__ == "__main__":
    main()
