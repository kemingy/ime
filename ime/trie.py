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

        if word in [w.han for w in node.words]:
            print('Word "{}" already in this tree.'.format(word))
        else:
            node.add_word(word, freq)

    def find_word(self, pinyin):
        node = self.root
        for char in pinyin:
            if char not in node.children:
                return None
            node = node.children[char]

        return node.words

    def find_candidate(self, pinyin):
        node = self.root
        candidate = []
        cur_index = 0
        length = len(pinyin)
        while cur_index < length:
            if node.words:
                candidate.extend([(cur_index, w) for w in node.words])
            if pinyin[cur_index] not in node.children:
                break

            node = node.children[pinyin[cur_index]]
            cur_index += 1

        if cur_index == length:
            candidate.extend([(length, w) for w in node.words])

        candidate.sort(key=lambda x: (x[0], x[1].freq), reverse=True)
        return candidate

    def sort_by_freq(self):
        def _sort(node):
            node.words.sort(key=lambda w: w.freq, reverse=True)
            for child in node.children:
                _sort(node.children[child])

        _sort(self.root)

    def batch_add(self, data):
        """
        :param dict data: pinyin-[(word, freq)]
        """
        count = 0
        for pinyin in data:
            node = self.root
            for char in pinyin:
                if char not in node.children:
                    child = Node(char)
                    node.children[char] = child
                node = node.children[char]

            words = set([w.han for w in node.words])
            for han, freq in data[pinyin]:
                if han in words:
                    continue

                words.add(han)
                node.words.append(Word(han, freq))
                count += 1

        print('Added {} wrods.'.format(count))
