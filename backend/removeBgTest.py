import unittest
from unittest.mock import patch, MagicMock
from io import BytesIO
from PIL import Image
from main import app

class TestRemoveBgApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    @patch('src.routers.save_outfit.upload_clothing_items')  # Patch the function you want to mock
    def test_file_upload(self, mock_upload_clothing_items):
        # Generate mock image data
        image = Image.new('RGB', (100, 100), color='red')  # Create a mock image
        mock_image_data = BytesIO()
        image.save(mock_image_data, format='PNG')
        mock_image_data.seek(0)
        mock_image_data.filename = 'test.png'

        # Mock the upload function to return some mock response
        mock_upload_clothing_items.return_value = MagicMock(status_code=200, mimetype='image/png', data=mock_image_data.getvalue())       

        # Make a request to your endpoint
        response = self.app.post('/remove-bg', data={'image_file': (mock_image_data, 'test.png')})

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('image/png', response.mimetype)

        # Open the image from the response data (mock image)
        image = Image.open(BytesIO(response.data))

if __name__ == '__main__':
    unittest.main()
