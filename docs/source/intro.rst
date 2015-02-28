=================
Browler
=================

Browler is a Selenium based web crawler. It was built out of a need to crawl and scrape content from Javascript heavy
web sites.


------------
Example
------------
Perform a crawl with two concurrent processes with a limit of two visits per process. Additionally, do not follow any
links that contain ``bad-stuff`` in the url::

    from browler import Browler
    import re

    config = {
        "browser": "firefox",
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

-------------
Features
-------------

* Concurrent processing for faster web crawls (Use at your own risk)
* Selenium Grid support with remote browser configuration
* Plugin support with hooks to customize the crawler

--------------
Configuration
--------------

:browser: ``(string)(required)`` must be supported Selenium browser ``firefox``, ``chrome``, ``phantomjs``, or (``remote`` requires see ``remote`` below)
:remote: ``(dict)(optional)`` required when ``browser`` is set to ``remote``

    :browser: ``(string)`` see ``browser``
    :url: ``(string)`` url of the remote host ie. ``http://localhost:4444/wd/hub``

:limit: ``(int)`` maximum number of visits per process
:plugins: ``(list)`` instances which inherit from ``browler.plugins.base.Plugin`` see :doc:`plugins`
:filters: ``(list)`` filters out any links that match the following regular expressions compiled with ``re.complile``



