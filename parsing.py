__author__ = 'juka'

from nltk import data
from nltk.parse import RecursiveDescentParser
from nltk.parse.generate import generate
from nltk import load_parser
import unittest


class TextCollocation(unittest.TestCase):
    VALID_SENTENCES = [
        "i will book",
        "i will book a flight",
        "could you book a flight",
        "i could book a flight",
        "does that flight include a meal",
        "does that flight include a breakfast",
        "he books that flight",
    ]

    INVALID_SENTENCES = [
        "does that flightss include a meal",
        "that does that flight include a meal",
        "she could want that flight breakfast meal",
        "he book that flight",
        "she could wants me",
        "she want to book"
    ]

    grammar = data.load('grammar.fcfg')
    parser = load_parser('grammar.fcfg')

    def assert_valid(self, sentence):
        try:
            parsed = self.parser.parse(sentence.split())
            print(sentence)
            print(next(parsed))
        except Exception:
            self.fail("Couldn't parse \"{}\"".format(sentence))

    def assert_invalid(self, sentence):
        with self.assertRaises(Exception, msg="Parsed the invalid sentence \"{}\"".format(sentence)):
            parsed = self.parser.parse(sentence.split())
            print(next(parsed))

    def test_parse(self):
        for s in self.VALID_SENTENCES:
            self.assert_valid(s)
        for s in self.INVALID_SENTENCES:
            self.assert_invalid(s)

    for sentence in generate(grammar, n=100):
        if(parser.parse_one(sentence)):
            print(' '.join(sentence))
