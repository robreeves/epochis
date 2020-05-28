import sys
from epochis.date_parser import *
from epochis.from_epoch import *


def _bad_input():
    print("Expected usage: epochis {date}{unit}\nExample: epochis 604m")
    sys.exit(2)


def main():
    if len(sys.argv) != 2:
        _bad_input()

    date_input = sys.argv[1]
    date_parser = DateParser(date_input)

    date_token = date_parser.next()
    if date_token.type is not DateTokenType.DATE:
        _bad_input()

    units_token = date_parser.next()

    eof_token = date_parser.next()
    if eof_token.type is not DateTokenType.EOF:
        _bad_input()

    if units_token.type is DateTokenType.MONTHS:
        print(month(date_token.value).strftime("%Y-%m"))
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
