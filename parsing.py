__author__ = 'juka'

from nltk import data
from nltk.parse import RecursiveDescentParser
import unittest


def get_parser():
    grammar = data.load('grammar.cfg')

    return RecursiveDescentParser(grammar)


class TextCollocation(unittest.TestCase):
    VALID_SENTENCES = [
        "does that flight include a meal",
        "does that flight include a breakfast"
    ]

    INVALID_SENTENCES = [
        "does that flightss include a meal",
        "that does that flight include a meal"
    ]

    rd = get_parser()

    def assert_valid(self, sentence):
        try:
            parsed = self.rd.parse(sentence.split())
            next(parsed)
        except ValueError:
            self.fail("Couldn't parse \"{}\"".format(sentence))

    def assert_invalid(self, sentence):
        with self.assertRaises(ValueError, msg="Parsed the invalid sentence \"{}\"".format(sentence)):
            self.rd.parse(sentence.split())

    def test_parse(self):
        for s in self.VALID_SENTENCES:
            self.assert_valid(s)
        for s in self.INVALID_SENTENCES:
            self.assert_invalid(s)
