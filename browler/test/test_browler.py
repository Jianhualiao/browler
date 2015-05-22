import unittest
from browler import Browler
from browler.plugins.base import Plugin
import re


class SamplePlugin(Plugin):

    def match(self, page):
        return True

    def startup(self, context):
        context.crawler.logger.info('Plugin running start up')

    def shutdown(self, context):
        context.crawler.logger.info('Plugin running shut down')

    def startup_plugin(self, context):
        context.crawler.logger.info('Plugin running global start up')

    def shutdown_plugin(self, context):
        context.crawler.logger.info('Plugin running global shut down')


class BrowlerTest(unittest.TestCase):

    def _test_browler(self):

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
              SamplePlugin()
            ],
            "filters": [
                re.compile('bad-stuff'),
            ]
        }
        crawler = Browler(config)
        crawler.crawl()

    def test_browler_without_grid(self):

        config = {
            "browser": 'firefox',
            "url": "https://en.wikipedia.org/wiki/Main_Page",
            "limit": 2,
            "processes": 2,
            "plugins": [
                SamplePlugin()
            ],
            "filters": [
                re.compile('bad-stuff'),
                ]
        }
        crawler = Browler(config)
        crawler.crawl()

if __name__ == '__main__':
    unittest.main()
