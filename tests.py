import unittest

import typographer


class TypographerTestCase(unittest.TestCase):
    def test_quotes(self):
        sample_text = "Hello 'my friend', hello; happy \"new year\""
        self.assertEqual(
            typographer.process(sample_text),
            "Hello «my friend», hello; happy «new year»",
        )

    def test_phone_numbers(self):
        phone_number = "8(999)888{0}77{0}22"
        sample_text = phone_number.format(typographer.HYPHEN)
        self.assertEqual(
            typographer.process(sample_text),
            phone_number.format(typographer.EN_DASH),
        )

    def test_spaces(self):
        sample_text = " hello   world!  \n"
        self.assertEqual(typographer.process(sample_text), "hello world!")

    def test_short_words(self):
        sample_text = "Пришло счастье в каждый дом"
        self.assertEqual(
            typographer.process(sample_text),
            "Пришло счастье в&nbsp;каждый дом",
        )
        sample_text = "И началась буря"
        self.assertEqual(
            typographer.process(sample_text), "И&nbsp;началась буря"
        )

    def test_digit_word(self):
        sample_text = "Hello 123 world!"
        self.assertEqual(
            typographer.process(sample_text), "Hello 123&nbsp;world!"
        )

    def test_dashes_and_hyphens(self):
        sample_text = "hello {} world"
        self.assertEqual(
            typographer.process(sample_text.format(typographer.HYPHEN)),
            sample_text.format(typographer.EM_DASH),
        )
        sample_text = "Saxony{}Anhalt"
        self.assertEqual(
            typographer.process(sample_text.format(typographer.EM_DASH)),
            sample_text.format(typographer.HYPHEN),
        )
