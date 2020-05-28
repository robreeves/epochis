"""Methods to convert date offsets from epoch to proper dates
"""
from datetime import *


EPOCH = datetime(1970, 1, 1)
MONTHS_IN_YEAR = 12


def month(months_since_epoch):
    years = int(months_since_epoch / MONTHS_IN_YEAR)
    months = months_since_epoch % MONTHS_IN_YEAR

    return date(EPOCH.year + years, EPOCH.month + months, EPOCH.day)


def day(days_since_epoch):
    return (EPOCH + timedelta(days=days_since_epoch)).date()


def seconds(seconds_since_epoch):
    return EPOCH + timedelta(seconds=seconds_since_epoch)


def millis(millis_since_epoch):
    return EPOCH + timedelta(milliseconds=millis_since_epoch)
