__author__ = 'juka'

from nltk import data
from nltk.parse import RecursiveDescentParser
import unittest


def get_parser():
    grammar = data.load('grammar.cfg')

    return RecursiveDescentParser(grammar)


class TextCollocation(unittest.TestCase):
    VALID_SENTENCES = [
        "i will book",
        "i will book a flight",
        "could you book a flight",
        "i could book a flight",
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
            print(sentence)
            print(next(parsed))
        except Exception:
            self.fail("Couldn't parse \"{}\"".format(sentence))

    def assert_invalid(self, sentence):
        with self.assertRaises(Exception, msg="Parsed the invalid sentence \"{}\"".format(sentence)):
            parsed = self.rd.parse(sentence.split())
            print(next(parsed))

    def test_parse(self):
        for s in self.VALID_SENTENCES:
            self.assert_valid(s)
        for s in self.INVALID_SENTENCES:
            self.assert_invalid(s)
