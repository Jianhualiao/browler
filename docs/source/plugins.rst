=================
Custom Plugins
=================

To make Browler useful, you will need to add custom plugins to hook into the crawler.

------------------------
Example Plugin
------------------------

Here is an example of how to save a copy of all the urls crawled with a multiprocessing lock::

    # plugins.py
    from browler.plugins.base import Plugin

    class Urls(Plugin):

        def __init__(self):
            self.stream = open('urls.txt', 'w')

        def match(self, page):
            """
            only run on allowed pages
            """
            return page.crawler.allowed(page.visited)

        def run(self, page):
            """
            run when match returns True
            """
            with page.crawler.lock:
                self.stream.write(page.url + '\n')
                self.stream.flush()

        def startup(self, context):
            """
            run within multiprocesses
            """
            pass

        def shutdown(self, crawler):
            """
            run within multiprocesses
            """
            self.stream.close()



------------------------
Example Usage
------------------------

::

    import re
    from browler import Browler
    import plugins

    config = {
        "browser": "firefox",
        "url": "https://en.wikipedia.org/wiki/Main_Page",
        "limit": 2,
        "processes": 2,
        "plugins": [
            plugins.Urls() # Must instantiate the plugin
        ],
        "filters": [
            re.compile('bad-stuff'),
        ]
    }
    crawler = Browler(config)
    crawler.crawl()
