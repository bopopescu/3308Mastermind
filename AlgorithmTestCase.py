#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sonia Szeton
# Fall 2015
# CSCI 3308
# Univerity of Colorado

import unittest
from mastermind_alg import *
#from mastermind_alg import Peg
#from mastermind_alg import Pin

class AlgorithmTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        code = [Peg.blue, Peg.yellow, Peg.green, Peg.red]
        guess = [Peg.yellow, Peg.red, Peg.yellow, Peg.red]
        score = scoreGuess(guess,code)
        expected = [Pin.white, Pin.black]
        print("TEST 1")
        print("Code: " + str(code))
        print("Guess: " + str(guess))
        print("Actual Score: " + str(score))
        print("Expected Score: " + str(expected))
        self.assertEqual(score, expected, "Incorrect score on test1: " + str(score))

    def test_2(self):
        code = [Peg.yellow, Peg.yellow, Peg.blue, Peg.red]
        guess = [Peg.green, Peg.yellow, Peg.red, Peg.green]
        score = scoreGuess(guess,code)
        expected = [Pin.black, Pin.white]
        print("TEST 2")
        print("Code: " + str(code))
        print("Guess: " + str(guess))
        print("Actual Score: " + str(score))
        print("Expected Score: " + str(expected))
        self.assertEqual(score, expected, "Incorrect score on test2: " + str(score))

    def test_3(self):
        code = [Peg.orange, Peg.green, Peg.red, Peg.blue]
        guess = [Peg.blue, Peg.green, Peg.blue, Peg.orange]
        score = scoreGuess(guess,code)
        expected = [Pin.white, Pin.black, Pin.white]
        print("TEST 3")
        print("Code: " + str(code))
        print("Guess: " + str(guess))
        print("Actual Score: " + str(score))
        print("Expected Score: " + str(expected))
        self.assertEqual(score, expected, "Incorrect score on test3: " + str(score))

    def test_4(self):
        code = [Peg.orange, Peg.purple, Peg.red, Peg.purple]
        guess = [Peg.red, Peg.purple, Peg.empty, Peg.green]
        score = scoreGuess(guess,code)
        expected = [Pin.black, Pin.white]
        print("TEST 4")
        print("Code: " + str(code))
        print("Guess: " + str(guess))
        print("Actual Score: " + str(score))
        print("Expected Score: " + str(expected))
        self.assertEqual(score, expected, "Incorrect score on test4: " + str(score))


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
