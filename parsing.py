__author__ = 'juka'

from nltk import data
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
        "i would like",
        "i would like to book",
        "i would like to book a flight to atlanta",
        "how may i serve",
        "how may i serve you",
        "the airport is closed",
        "i would like to reserve a ticket",
        "the flight arrives",
        # _time_ is used to present any time like value
        "the flight arrives at _time_",
        "the flight departs at _time_",
        "the flight to frankfurt departs at _time_",
        "the flight from frankfurt arrives at _time_",
        "there is a bus",
        "there is a bus transition",
        "there are bus transitions",
        "i am flying",
        "where are you flying",
        "the plane is flying",
        "the plane is going to crash",
        "i fly planes",
        "i want to fly",
        "i want to fly to london",
        "the flight is late",
        "the weather is bad",
        "the flight weather is bad",
        "the air plane is white",
        "the toilet of the plane is out of use",
        "the plane has the autopilot on",
        "cats are allowed",
        "cats are allowed in the plane",
        "no cats are allowed in the plane",
        "there is a bird inside the air plane",
        "this is your captain",
        "this is your captain speaking",
    ]

    INVALID_SENTENCES = [
        "does that flightss include a meal",
        "that does that flight include a meal",
        "she could want that flight breakfast meal",
        "he book that flight",
        "she could wants me",
        "she want to book",
        "she could flights to book",
        "she want to book to like",
        "she could closed to book",
        "i would like to reserved a ticket",
        "the flight from frankfurt arrive at _time_",
        "there are a bus transition",
        "there is a bus transitions",
        "i are flying",
        "i could is",
        "flying scary"
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

    for sentence in generate(grammar, n=10):
        if(parser.parse_one(sentence)):
            print(' '.join(sentence))
