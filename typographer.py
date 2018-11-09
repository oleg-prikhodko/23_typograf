import re


def process(input_string):
    processed_string = input_string.strip()
    processed_string = re.sub(r" {2,}", " ", processed_string)
    processed_string = re.sub(
        r"('|\")([^'\"]*)('|\")", r"«\2»", processed_string
    )
    processed_string = re.sub(r"(\d)-(\d)", r"\1–\2", processed_string)
    processed_string = re.sub(
        r"(^| )(\w{1,2}) (\w)", r"\1\2&nbsp;\3", processed_string, flags=re.U
    )
    processed_string = re.sub(
        r"(\d) (\w)", r"\1&nbsp;\2", processed_string, flags=re.UNICODE
    )

    HYPHEN = "\u2010"
    EN_DASH = "\u2013"
    EM_DASH = "\u2014"
    processed_string = re.sub(
        r"(\w)({}|{})(\w)".format(EN_DASH, EM_DASH),
        r"\1{}\3".format(HYPHEN),
        processed_string,
        re.UNICODE,
    )
    processed_string = re.sub(
        r"(\w) ({}|{}) (\w)".format(HYPHEN, EN_DASH),
        r"\1 {} \3".format(EM_DASH),
        processed_string,
        re.UNICODE,
    )
    return processed_string


if __name__ == "__main__":
    # test_str = "Hello 'my friend', hello; happy \"new year\""
    # test_str = "8(985)878-06-71"
    # test_str = " hello   world!  \n"
    # test_str = "Пришло счастье в каждый дом"
    # test_str_2 = "И началась буря"
    # test_str = "Hello 123 world!"
    test_str = "hello \u2010 world"
    print(process(test_str))
    # print(process(test_str_2))
