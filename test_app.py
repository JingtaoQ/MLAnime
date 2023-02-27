import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        data = {
            'title': 'Spirited Away',
            'genre': 'Adventure, Drama, Fantasy',
            'description': 'On the way to their new home, 10-year-old Chihiro Ogino\'s family stumbles upon a deserted theme park. Amidst the rides and food stalls is a mysterious bathhouse which turns out to be a home to gods and monsters.',
            'type': 'Movie',
            'producer': 'Studio Ghibli',
            'studio': 'Studio Ghibli'
        }
        response = self.app.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'no', response.data)

if __name__ == '__main__':
    unittest.main()
