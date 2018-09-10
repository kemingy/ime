from collections import namedtuple


Word = namedtuple('Word', ['han', 'freq'])


class Node:
    def __init__(self, char):
        self.char = char
        self.words = []
        self.children = {}

    def add_word(self, word, freq):
        self.words.append(Word(word, freq))


class Trie:
    def __init__(self):
        self.root = Node('')

    def add_word(self, pinyin, word, freq=1):
        node = self.root
        for char in pinyin:
            if char not in node.children:
                child = Node(char)
                node.children[char] = child
            node = node.children[char]

        node.add_word(word, freq)

    def find_word(self, pinyin):
        node = self.root
        for char in pinyin:
            if char not in node.children:
                return None
            node = node.children[char]

        return node.words

    def sort_by_freq(self):
        def _sort(node):
            node.words.sort(key=lambda w: w.freq, reverse=True)
            for child in node.children:
                _sort(child)

        _sort(self.root)

    def batch_build(self, data):
        """
        :param dict data: pinyin-[words]
        """
        count = 0
        for pinyin in data:
            node = self.root
            for char in pinyin:
                if char not in node.children:
                    child = Node(char)
                    node.children[char] = child
                node = node.children[char]
            
            node.words.extend(data[pinyin])
            count += len(data[pinyin])

        print('Add {} phrases.'.format(count))
