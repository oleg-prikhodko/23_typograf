import unittest

import typographer


class TypographerTestCase(unittest.TestCase):
    def test_typographer(self):
        sample_text = "Hello 'my friend', hello; happy \"new year\""
        self.assertEqual(
            typographer.process(sample_text),
            "Hello «my friend», hello; happy «new year»",
        )
        phone_number = "8(999)888{0}77{0}22"
        sample_text = phone_number.format(typographer.HYPHEN)
        self.assertEqual(
            typographer.process(sample_text),
            phone_number.format(typographer.EN_DASH),
        )
        sample_text = " hello   world!  \n"
        self.assertEqual(typographer.process(sample_text), "hello world!")
        sample_text = "Пришло счастье в каждый дом"
        self.assertEqual(
            typographer.process(sample_text),
            "Пришло счастье в&nbsp;каждый дом",
        )
        sample_text = "И началась буря"
        self.assertEqual(
            typographer.process(sample_text), "И&nbsp;началась буря"
        )
        sample_text = "Hello 123 world!"
        self.assertEqual(
            typographer.process(sample_text), "Hello 123&nbsp;world!"
        )
        sample_text = "hello \u2010 world"
        self.assertEqual(
            typographer.process(sample_text), "hello \u2014 world"
        )
