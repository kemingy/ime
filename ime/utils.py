from pypinyin import lazy_pinyin
import sqlite3

from ime.config import Config


def get_ngram_phrase(n, db_path=Config.db_path):
    """
    :param int n: n-gram
    """
    assert 0 < n < 16

    data = {}
    count = 0
    for i in range(n):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('select phrase, freq from py_phrase_{}'.format(i))
        res = cur.fetchall()
        count += len(res)

        for phrase, freq in res:
            pinyin = ''.join(lazy_pinyin(phrase))
            if pinyin not in data:
                data[pinyin] = []

            data[pinyin].append((phrase, freq))

    print('Get {} words and {} pinyin.'.format(count, len(data)))

    return data
