from unittest import TestCase

from indexnow.errors import Exception202, Exception422, ErrorMessages
from indexnow.submitter import IndexNow


class TestIndexNow(TestCase):
    def test_202(self):
        index_now = IndexNow(key='30d227a8fd7447458801c5ff69189470', host='https://www.example.com')

        with self.assertRaises(Exception202) as cm:
            index_now.send_urls(['https://www.example.com'])

        self.assertEqual(str(cm.exception), ErrorMessages.ERROR_202)

        with self.assertRaises(Exception202) as cm:
            index_now.send_url('https://www.example.com')

        self.assertEqual(str(cm.exception), ErrorMessages.ERROR_202)

    def test_422(self):
        index_now = IndexNow(key='random_key', host='https://www.example.com')

        with self.assertRaises(Exception422) as cm:
            index_now.send_urls(['https://www.example.com'])

        self.assertEqual(str(cm.exception), ErrorMessages.ERROR_422)

        index_now = IndexNow(key='30d227a8fd7447458801c5ff69189470', host='https://www.example.com')

        with self.assertRaises(Exception422) as cm:
            index_now.send_urls(['https://www.bad_example.com'])

        self.assertEqual(str(cm.exception), ErrorMessages.ERROR_422)
