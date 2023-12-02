What is IndexNow?
====

`IndexNow`_ is an easy way for websites owners to instantly inform search engines about latest content changes on their website. In its simplest form, IndexNow is a simple ping so that search engines know that a URL and its content has been added, updated, or deleted, allowing search engines to quickly reflect this change in their search results.

Without IndexNow, it can take days to weeks for search engines to discover that the content has changed, as search engines don’t crawl every URL often. With IndexNow, search engines know immediately the "URLs that have changed, helping them prioritize crawl for these URLs and thereby limiting organic crawling to discover new content."

IndexNow is offered under the terms of the Attribution-ShareAlike Creative Commons License and has support from `Microsoft Bing`_, `Seznam.cz`_, Yandex.

.. _IndexNow: https://www.indexnow.org/
.. _Microsoft Bing: https://www.bing.com/
.. _Seznam.cz: https://www.seznam.cz/

Submitting One URL
----
.. code-block:: python

    from indexnow.submitter import IndexNow

    index_now = IndexNow(key=<index_now_key>, host='https://example.com/')

    status = index_now.send_url('https://www.example.com/')

    print(status)

    #status == 200 is OK

Submitting set of URLs
----
.. code-block:: python

    from indexnow.submitter import IndexNow

    index_now = IndexNow(key=<index_now_key>, host='https://example.com/')

    status = index_now.send_urls(['https://www.example.com/', 'https://www.example.com/whatever'])

    print(status)

    #status == 200 is OK

Custom key location
----
.. code-block:: python

    index_now = IndexNow(key=<index_now_key>, host='https://example.com/', key_location='https://example.com/path_to_key.txt')

