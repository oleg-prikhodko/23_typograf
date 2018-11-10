import re


HYPHEN = "\u2010"
EN_DASH = "\u2013"
EM_DASH = "\u2014"

MULTIPLE_SPACE_PATTERN = re.compile(r" {2,}")
QUOTES_PATTERN = re.compile(r"('|\")([^'\"]*)('|\")")
DIGITS_HYPHEN_PATTERN = re.compile(r"(\d){}(\d)".format(HYPHEN))
SHORT_WORDS_PATTERN = re.compile(r"(^| )(\w{1,2}) (\w)", re.UNICODE)
DIGIT_WORD_PATTERN = re.compile(r"(\d) (\w)", re.UNICODE)
DASH_INSIDE_WORD_PATTERN = re.compile(
    r"(\w)({}|{})(\w)".format(EN_DASH, EM_DASH), re.UNICODE
)
HYPHEN_BETWEEN_WORDS_PATTERN = re.compile(
    r"(\w) ({}|{}) (\w)".format(HYPHEN, EN_DASH), re.UNICODE
)


def process(input_string):
    processed_string = input_string.strip()
    processed_string = re.sub(MULTIPLE_SPACE_PATTERN, " ", processed_string)
    processed_string = re.sub(QUOTES_PATTERN, r"«\2»", processed_string)
    processed_string = re.sub(
        DIGITS_HYPHEN_PATTERN, r"\1{}\2".format(EN_DASH), processed_string
    )
    processed_string = re.sub(
        SHORT_WORDS_PATTERN, r"\1\2&nbsp;\3", processed_string
    )
    processed_string = re.sub(
        DIGIT_WORD_PATTERN, r"\1&nbsp;\2", processed_string
    )
    processed_string = re.sub(
        DASH_INSIDE_WORD_PATTERN, r"\1{}\3".format(HYPHEN), processed_string
    )
    processed_string = re.sub(
        HYPHEN_BETWEEN_WORDS_PATTERN,
        r"\1 {} \3".format(EM_DASH),
        processed_string,
    )
    return processed_string
