import unittest
from browler import Browler
import re


class BrowlerTest(unittest.TestCase):

    def test_browler(self):

        config = {
            "browser": 'remote',
            "remote": {
                "url": 'http://localhost:49044/wd/hub',
                'browser': 'firefox'
            },
            "url": "https://en.wikipedia.org/wiki/Main_Page",
            "limit": 2,
            "processes": 2,
            "plugins": [

            ],
            "filters": [
                re.compile('bad-stuff'),
            ]
        }
        crawler = Browler(config)
        crawler.crawl()

if __name__ == '__main__':
    unittest.main()
