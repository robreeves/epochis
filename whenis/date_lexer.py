from enum import Enum


class DateLexer:
    """Tokenizes the CLI date input

    Rules:
    DATE: [0-9]
    MONTHS: m
    DAYS: d
    SECONDS: s
    MILLIS: ms
    """
    def __init__(self, input):
        self._input = input
        self._look_ahead_index = -1
        self._look_ahead = None

        self._consume()

    def _consume(self):
        self._look_ahead_index += 1
        if len(self._input) > self._look_ahead_index:
            self._look_ahead = self._input[self._look_ahead_index]
        else:
            self._look_ahead = DateTokenType.EOF

    def _date(self):
        start_index = self._look_ahead_index

        while self._look_ahead.isdigit():
            self._consume()

        end_index = self._look_ahead_index
        date = int(self._input[start_index:end_index])
        return DateToken(DateTokenType.DATE, date)

    def next(self):
        while len(self._input) > self._look_ahead_index:

            if self._look_ahead.isdigit():
                return self._date()
            elif self._look_ahead is 'm':
                self._consume()
                # todo do a better job of this parsing
                if self._look_ahead is DateTokenType.EOF:
                    return DateToken(DateTokenType.MONTHS)
                elif self._look_ahead is 's':
                    return DateToken(DateTokenType.MILLIS)
                else:
                    raise ValueError("Unexpected unit input at '' (index {}) of '{}'".format(self._look_ahead,
                                                                                             self._look_ahead_index,
                                                                                             self._input))
            elif self._look_ahead is 'd':
                self._consume()
                return DateToken(DateTokenType.DAYS)
            elif self._look_ahead is 's':
                self._consume()
                return DateToken(DateTokenType.SECONDS)
            elif self._look_ahead is 's':
                self._consume()
                return DateToken(DateTokenType.SECONDS)
            else:
                raise ValueError("Unexpected date input at '' (index {}) of '{}'".format(self._look_ahead,
                                                                                         self._look_ahead_index,
                                                                                         self._input))
        return DateToken(DateTokenType.EOF)


class DateTokenType(Enum):
    DATE = 1
    MONTHS = 2
    DAYS = 3
    SECONDS = 4
    MILLIS = 5
    EOF = 6


class DateToken:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
