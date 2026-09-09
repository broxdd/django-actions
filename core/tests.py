from django.test import SimpleTestCase


class BasicTest(SimpleTestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)


from django.test import SimpleTestCase

from .tasks import add


class BasicTest(SimpleTestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)

    def test_celery_add_task(self):
        self.assertEqual(add.run(2, 3), 5)
