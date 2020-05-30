import sys
from epochis.date_parser import DateParser
from epochis.from_epoch import *


def _print_usage():
    print("Usage")
    print("\tepochis {date}{unit}")
    print("Example")
    print("\tepochis 604m")
    print("Supported Units")
    print("\tm:  months since epoch")
    print("\td:  days since epoch")
    print("\ts:  seconds since epoch")
    print("\tms: milliseconds since epoch")


def _check_args(args):
    if len(args) != 2:
        print("Incorrect number of arguments\n", file=sys.stderr)
        _print_usage()
        sys.exit(2)
    elif args[1] == "--help" or args[1] == "-h":
        _print_usage()
        sys.exit(0)


def main(args=None):
    if args is None:
        args = sys.argv

    _check_args(args)

    try:
        # get date from input
        date_input = args[1]
        date_parser = DateParser(date_input)
        epoch_offset = date_parser.epoch_date()
    except ValueError as ve:
        print(str(ve) + "\n", file=sys.stderr)
        _print_usage()
        sys.exit(2)

    # convert from epoch offset to human readable date
    if epoch_offset.unit == 'm':
        print(month(epoch_offset.offset).strftime("%Y-%m"))
    elif epoch_offset.unit == 'd':
        print(day(epoch_offset.offset))
    elif epoch_offset.unit == 's':
        print(seconds(epoch_offset.offset))
    elif epoch_offset.unit == 'ms':
        print(millis(epoch_offset.offset))
    else:
        print("Unit '{}' is not supported\n".format(epoch_offset.unit), file=sys.stderr)
        _print_usage()
        sys.exit(2)


if __name__ == "__main__":
    main()
