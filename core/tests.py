from django.test import SimpleTestCase


class BasicTest(SimpleTestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)