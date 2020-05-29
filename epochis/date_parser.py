from enum import Enum


class DateLexer:
    def __init__(self, date_input):
        self._input = date_input
        self._look_ahead_index = -1
        self._look_ahead = None

        self._consume()

    def _consume(self):
        self._look_ahead_index += 1
        if len(self._input) > self._look_ahead_index:
            self._look_ahead = self._input[self._look_ahead_index]
        else:
            self._look_ahead = DateTokenType.EOF

    def next(self):
        if self._look_ahead is DateTokenType.EOF:
            return DateToken(DateTokenType.EOF)

        if self._look_ahead.isdigit():
            token = DateToken(DateTokenType.NUMBER, self._look_ahead)
        elif self._look_ahead.isalpha():
            token = DateToken(DateTokenType.LETTER, self._look_ahead)
        else:
            raise Exception(
                "Unexpected character while parsing date input. Index: {}, Value: '{}'".format(self._look_ahead_index,
                                                                                               self._look_ahead))

        self._consume()
        return token


class DateParser:
    """Parses date argument input

    Rules:
    DATE: [0-9]+
    MONTHS: m
    DAYS: d
    SECONDS: s
    MILLIS: ms
    """
    def __init__(self, date_input):
        self._lexer = DateLexer(date_input)
        self._look_ahead = self._lexer.next()

    def epoch_date(self):
        offset = self._offset()
        unit = self._unit()
        self._match(DateTokenType.EOF)

        return DateOffset(offset, unit)

    def _match(self, expected_token_type):
        if self._look_ahead.type is not expected_token_type:
            raise Exception(
                "Error parsing date input. Expected token type: {}, but found: {}".format(expected_token_type,
                                                                                          self._look_ahead.type))

    def _consume(self):
        self._look_ahead = self._lexer.next()

    def _consume_until(self, token):
        self._match(token)
        values = [self._look_ahead.value]
        self._consume()

        while self._look_ahead.type is token:
            values.append(self._look_ahead.value)
            self._consume()

        return values

    def _offset(self):
        digits = self._consume_until(DateTokenType.NUMBER)
        return int(''.join(digits))

    def _unit(self):
        letters = self._consume_until(DateTokenType.LETTER)
        return ''.join(letters)


class DateOffset:
    def __init__(self, offset, unit):
        self.offset = offset
        self.unit = unit


class DateTokenType(Enum):
    NUMBER = 1
    LETTER = 2
    EOF = 3


class DateToken:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value
