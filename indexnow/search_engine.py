from enum import Enum


class SearchEngine(Enum):
    INDEX_NOW = 'https://api.indexnow.org/indexnow'
    SEZNAM_CZ = 'https://search.seznam.cz/indexnow'
    AMAZON = 'https://indexnow.amazonbot.amazon/indexnow'
    BING = 'https://www.bing.com/indexnow'
    YANDEX = 'https://yandex.com/indexnow'
    NAVER = 'https://searchadvisor.naver.com/indexnow'
    YEP = 'https://indexnow.yep.com/indexnow'
