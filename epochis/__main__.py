"""
Entry point for epochis CLI
"""
import sys

from epochis.date_parser import DateParser, EpochOffset
from epochis.from_epoch import day, millis, month, seconds


UNIT_GUESSES = ['m', 'd', 's', 'ms']


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


def _print_date(epoch_offset: EpochOffset):
    """Prints the date for the given epoch offset

    Args:
        epoch_offset (EpochOffset): The epoch representation of the date to print
    """
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


def main(args=None):
    """
    Entry point for CLI
    """
    if args is None:
        args = sys.argv

    _check_args(args)

    try:
        # get date from input
        date_input = args[1]
        date_parser = DateParser(date_input)
        epoch_offset = date_parser.epoch_date()
    except ValueError as value_error:
        print(str(value_error) + "\n", file=sys.stderr)
        _print_usage()
        sys.exit(2)

    if epoch_offset.unit == '':
        # If there are no units, try all of them and let the user pick the best option
        for unit in UNIT_GUESSES:
            print(f"{unit}:", end="\n\t")
            _print_date(EpochOffset(epoch_offset.offset, unit))
    else:
        _print_date(epoch_offset)


if __name__ == "__main__":
    main()
