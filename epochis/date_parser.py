from enum import Enum


class DateLexer:
    """
    Converts the date input into tokens
    """
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
        """
        :return: The next token in the input. If no more input is available an EOF token is returned.
        """
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


class EpochOffset:
    """
    The date represented as an epoch offset
    """
    def __init__(self, offset, unit):
        """
        :param offset: The number offset from epoch
        :param unit: The offset unit (e.g. 'm' for months)
        """
        self.offset = offset
        self.unit = unit


class DateTokenType(Enum):
    """
    The valid token types for the data lexer
    """
    NUMBER = 1
    LETTER = 2
    EOF = 3


class DateToken:
    """
    The date lexer token
    """
    def __init__(self, token_type, value=None):
        """
        :param token_type: The date lexer token type
        :param value: The token value
        """
        self.type = token_type
        self.value = value
