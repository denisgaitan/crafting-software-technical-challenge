from crafting import get_original_sentence, get_words_in_sentence_match


class TestGetWordsInSentenceMatch:
    def test_words_list_in_sentence(self):
        words_list = ["bed", "bath", "bedbath", "and", "beyond"]
        sentence_as_string = "bedbathandbeyond"

        actual_words_in_sentence_match = get_words_in_sentence_match(words_list=words_list, sentence_as_string=sentence_as_string)
        expected_words_in_sentence_match = ["bed", "bath", "and", "beyond"]

        assert len(actual_words_in_sentence_match) == len(expected_words_in_sentence_match)
        assert all(zip(actual_words_in_sentence_match, expected_words_in_sentence_match))


    def test_words_list_order_in_not_in_sentence(self):
        words_list = ["quick", "brown", "the", "fox"]
        sentence_as_string = "thequickbrownfox"

        actual_words_in_sentence_match = get_words_in_sentence_match(words_list=words_list, sentence_as_string=sentence_as_string)
        expected_words_in_sentence_match = []

        assert len(actual_words_in_sentence_match) == len(expected_words_in_sentence_match)
        assert all(zip(actual_words_in_sentence_match, expected_words_in_sentence_match))


class TestGetOriginalSentence:
    def test_use_case_1(self):
        words_list = ["quick", "brown", "the", "fox"]
        sentence_as_string = "thequickbrownfox"

        actual_original_sentence = get_original_sentence(
            words_list=words_list, sentence_as_string=sentence_as_string
        )
        expected_original_sentence = ["the", "quick", "brown", "fox"]

        assert len(actual_original_sentence) == len(expected_original_sentence)
        assert all(zip(actual_original_sentence, expected_original_sentence))

    def test_use_case_2(self):
        words_list = ["bed", "bath", "bedbath", "and", "beyond"]
        sentence_as_string = "bedbathandbeyond"

        actual_original_sentence = get_original_sentence(
            words_list=words_list, sentence_as_string=sentence_as_string
        )
        expected_original_sentence = ["bed", "bath", "and", "beyond"]

        assert len(actual_original_sentence) == len(expected_original_sentence)
        assert all(zip(actual_original_sentence, expected_original_sentence))
