# Chinese Pinyin Input Method Engine

[![Build Status](https://travis-ci.org/kemingy/ime.svg?branch=master)](https://travis-ci.org/kemingy/ime)

Yet another input method engine.

You can download data from [Google code(hslinuxextra)](https://code.google.com/archive/p/hslinuxextra/downloads).

## Tutorial

```py
>> from ime.engine import Engine
>> e = Engine()

>> e.search('daima')
[(5, Word(han='代码', freq=6955)),
 (3, Word(han='带', freq=7438)),
 (3, Word(han='待', freq=6568)),
 ......]

>> e.search('bitebi')
[(4, Word(han='比特', freq=4210)),
 (4, Word(han='彼特', freq=912)),
 (2, Word(han='比', freq=7543)),
 ......]
```

## TODO

- [x] word(full match)
- [x] candidate(sort by 1. length 2. frequence)
- [ ] sentence(try to find correct words)
- [ ] correct misspelling(fuzzy spell)
- [ ] search with initials
- [ ] adjust frequence of word dynamically
