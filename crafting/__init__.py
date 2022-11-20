__version__ = "0.0.1"

from typing import List


def get_original_sentence(words_list: List[str], sentence_as_string: str) -> List[str]:

    return get_words_in_sentence_first_match(
        words_list=words_list, sentence_as_string=sentence_as_string
    )


def get_words_in_sentence_first_match(
    words_list: List[str], sentence_as_string: str, generated_words_list: List[str] = []
):
    if len(words_list) == 0:
        return get_words_in_sentence_match(generated_words_list, sentence_as_string)
    else:
        i = 0
        range_ctn = len(words_list)
        words_in_sentence_not_found = True
        while words_in_sentence_not_found:
            words_in_sentence_match_list = get_words_in_sentence_first_match(
                words_list[:i] + words_list[i + 1 :],
                sentence_as_string,
                generated_words_list + words_list[i : i + 1],
            )
            i += 1
            words_in_sentence_not_found = (
                len(words_in_sentence_match_list) == 0 and i < range_ctn
            )

        return words_in_sentence_match_list


def get_words_in_sentence_match(
    words_list: List[str], sentence_as_string: str
) -> List[str]:
    words_in_sentence_match_list = []

    words_cnt = len(words_list)
    word_index = 0
    while sentence_as_string and word_index < words_cnt:
        word = words_list[word_index]
        word_len = len(word)
        sentence_len = len(sentence_as_string)

        if word_len <= sentence_len and word == sentence_as_string[:word_len]:
            sentence_as_string = sentence_as_string[word_len:sentence_len]
            words_in_sentence_match_list.append(word)

        word_index += 1

    if sentence_as_string:
        words_in_sentence_match_list = []

    return words_in_sentence_match_list
