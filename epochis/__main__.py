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
    epoch_offset = date_parser.epoch_date()

    if epoch_offset.unit == 'm':
        print(month(epoch_offset.offset).strftime("%Y-%m"))
    elif epoch_offset.unit == 'd':
        print(day(epoch_offset.offset))
    elif epoch_offset.unit == 's':
        print(seconds(epoch_offset.offset))
    elif epoch_offset.unit == 'ms':
        print(millis(epoch_offset.offset))
    else:
        raise Exception("Unit '{}' is unknown".format(epoch_offset.unit))


if __name__ == "__main__":
    main()
