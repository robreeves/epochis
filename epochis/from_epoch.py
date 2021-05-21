"""Methods to convert date offsets from epoch to proper dates
"""
from datetime import date, datetime, timedelta

EPOCH = datetime(1970, 1, 1)
MONTHS_IN_YEAR = 12


def month(months_since_epoch: int) -> date:
    """Converts a month offset from epoch to a date

    Args:
        months_since_epoch (int): The month offset from epoch

    Returns:
        date: The date the offset represents
    """
    years = int(months_since_epoch / MONTHS_IN_YEAR)
    months = months_since_epoch % MONTHS_IN_YEAR

    return date(EPOCH.year + years, EPOCH.month + months, EPOCH.day)


def day(days_since_epoch: int) -> date:
    """Converts a day offset from epoch to a date

    Args:
        days_since_epoch (int): The day offset from epoch

    Returns:
        date: The date the offset represents
    """
    return (EPOCH + timedelta(days=days_since_epoch)).date()


def seconds(seconds_since_epoch: int) -> date:
    """Converts a seconds offset from epoch to a date

    Args:
        seconds_since_epoch (int): The second offset from epoch

    Returns:
        date: The date the offset represents
    """
    return EPOCH + timedelta(seconds=seconds_since_epoch)


def millis(millis_since_epoch: int) -> date:
    """Converts a milliseconds offset from epoch to a date

    Args:
        millis_since_epoch (int): The millisecond offset from epoch

    Returns:
        date: The date the offset represents
    """
    return EPOCH + timedelta(milliseconds=millis_since_epoch)
