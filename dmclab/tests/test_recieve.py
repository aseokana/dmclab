import re

from django.test import TestCase, tag


@tag('recieve')
class TestRecieve(TestCase):

    def test_subject_identifier_regex_true(self):
        identifier = '1111111ABCDE1111'
        pattern = re.compile(r'\d{1,7}[a-zA-Z]{1,5}\d{1,4}')
        self.assertTrue(pattern.match(identifier))

    def test_subject_identifier_regex_false(self):
        identifier = '111'
        pattern = re.compile(r'\d{1,7}[a-zA-Z]{1,5}\d{1,4}')
        self.assertFalse(pattern.match(identifier))
