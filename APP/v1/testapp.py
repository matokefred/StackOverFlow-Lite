import unittest
from app import *


class Tdd(unittest.TestCase):
    def test_get_all_questions(self):
        testing = app.test_client(self)
        response = testing.get('/questions', content_type='json')
        self.assertIn(b'All questions', response.data)

    def test_get_a_question(self):
        testing = app.test_client(self)
        response = testing.get('/questions/1', content_type='json')
        self.assertIn(b'Requested Question', response.data)

    def test_add_question(self):
        testing = app.test_client(self)
        response = testing.post('/questions', content_type='json')
        self.assertEqual(response.status_code, 400)

    def test_add_answer(self):
        testing = app.test_client(self)
        response = testing.post('/questions/2/answers', content_type='json')
        self.assertIn(b'You answered this question', response.data)


if __name__ == '__main__':
    unittest.main()
