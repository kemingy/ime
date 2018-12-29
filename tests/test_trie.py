from ime.trie import Trie

t = Trie()


def test_batch():
    data = {
        'xian': [('先', 233), ('西安', 140), ('仙', 88)],
        'lian': [('连', 186), ('立案', 88)],
    }
    t.batch_add(data)
    assert len(t.find_word('lian')) == 2
    assert len(t.find_word('xian')) == 3


def test_add():
    t.add_word('pinyin', '拼音')
    assert t.find_word('pinyin')[0].han == '拼音'


def test_sort():
    t.add_word('lihai', '里海', 45)
    t.add_word('lihai', '厉害', 239)

    assert t.find_word('lihai')[0].han == '里海'
    t.sort_by_freq()
    assert t.find_word('lihai')[0].han == '厉害'
