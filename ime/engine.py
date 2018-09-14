from ime.trie import Trie
from ime.utils import get_ngram_phrase


class Engine:
    def __init__(self, ngram=2):
        self.trie = Trie()
        data = get_ngram_phrase(ngram)
        self.trie.batch_add(data)
        self.trie.sort_by_freq()

    def search(self, pinyin):
        # whole word
        # word = self.trie.find_word(pinyin)
        # if word:
        #     return word

        # candidate
        return self.trie.find_candidate(pinyin)
