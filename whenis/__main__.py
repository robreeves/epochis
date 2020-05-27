import sys
from whenis.date_lexer import *
from whenis.cli import *


def main():
    date_input = sys.argv[1]
    date_lexer = DateLexer(date_input)

    # todo validate types and EOF
    date_token = date_lexer.next()
    units_token = date_lexer.next()
    eof_token = date_lexer.next()

    if units_token.type is DateTokenType.MONTHS:
        print(month(date_token.value))
    elif units_token.type is DateTokenType.DAYS:
        print(day(date_token.value))
    elif units_token.type is DateTokenType.SECONDS:
        print(seconds(date_token.value))
    elif units_token.type is DateTokenType.MILLIS:
        print(millis(date_token.value))
    else:
        raise Exception("I forgot to implement unit {}".format(units_token.type))


if __name__ == "__main__":
    main()
