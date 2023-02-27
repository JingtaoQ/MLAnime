import unittest
from app import app

class AppTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_predict_page(self):
        data = {'feature1': 'anime', 'feature2': 'action'}
        result = self.app.post('/predict', data=data)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(b'yes' in result.data or b'no' in result.data)

if __name__ == '__main__':
    unittest.main()
