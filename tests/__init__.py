# -*- coding: utf-8 -*-
import unittest
import sys

from thainlp import *


class TestUM(unittest.TestCase):
    def test_use(self):
        thai=nlp("ทดสอบระบบ")
        self.assertIsNotNone(thai.words)
        self.assertIsNotNone(thai.tags)
        self.assertIsNotNone(thai.romanize)
        self.assertIsNotNone(thai.ngrams())
        

if __name__ == '__main__':
    unittest.main()