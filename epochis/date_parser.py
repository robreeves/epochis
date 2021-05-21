"""
Contains classes related to parsing the date input args
"""
from enum import Enum
from dataclasses import dataclass


class DateLexer:
    """
    Converts the date input into tokens
    """
    def __init__(self, date_input):
        self._input = date_input.strip()
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
        """
        :return: The next token in the input. If no more input is available an EOF token is
        returned.
        """
        if self._look_ahead is DateTokenType.EOF:
            return DateToken(DateTokenType.EOF)

        if self._look_ahead.isdigit():
            token = DateToken(DateTokenType.NUMBER, self._look_ahead)
        elif self._look_ahead.isalpha():
            token = DateToken(DateTokenType.LETTER, self._look_ahead)
        else:
            raise ValueError(
                f"Unexpected character while parsing date input. Index: {self._look_ahead_index}, \
                Value: '{self._look_ahead}'"
            )

        self._consume()
        return token


class DateParser:
    """
    Parses a date input in the format {date}{unit} (e.g. 604m)
    """
    def __init__(self, date_input):
        """
        :param date_input: The date input to parse
        """
        self._lexer = DateLexer(date_input)
        self._look_ahead = self._lexer.next()

    def epoch_date(self):
        """
        Parses the date input
        :return: The parsed input as an epoch offset
        """
        offset = self._offset()
        unit = self._unit()
        self._match(DateTokenType.EOF)

        return EpochOffset(offset, unit)

    def _match(self, expected_token_type):
        if self._look_ahead.type is not expected_token_type:
            raise ValueError(
                f"Error parsing date input. Expected token type: {expected_token_type}, \
                but found: {self._look_ahead.type}"
            )

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
        if self._look_ahead.type is DateTokenType.EOF:
            # This supports the case where the user does not provide units
            return ''

        letters = self._consume_until(DateTokenType.LETTER)
        return ''.join(letters)


@dataclass
class EpochOffset:
    """
    The date represented as an epoch offset

    :param offset: The number offset from epoch
    :param unit: The offset unit (e.g. 'm' for months)
    """
    offset: int
    unit: str


class DateTokenType(Enum):
    """
    The valid token types for the data lexer
    """
    NUMBER = 1
    LETTER = 2
    EOF = 3


@dataclass
class DateToken:
    """
    The date lexer token

    :param type: The date lexer token type
    :param value: The token value
    """
    type: DateTokenType
    value: str = None
