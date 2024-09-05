import unittest
from main import app

class TestSaveOutfitApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_file_upload(self):
        # Define the JSON data to be sent in the request
        data = {
            "urls": ["https://firebasestorage.googleapis.com/v0/b/wardrobe-wizard-105dd.appspot.com/o/clothes%2F7l5VB8uPhHdmG24WiRqkBWmIeCs2%2FT-shirts%2Fts4.png?alt=media&token=11e3cd10-4adb-43b3-882d-89de60fd2930"],
            "categories": ["T-shirts"],
            "user_id": "7l5VB8uPhHdmG24WiRqkBWmIeCs2"
        }
        
        # Send a POST request to the /outfit endpoint with the JSON data
        response = self.app.post('/outfit', json=data)
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
