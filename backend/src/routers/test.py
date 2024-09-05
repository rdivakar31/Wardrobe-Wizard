import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from save_outfit import save_outfit
class TestUploadClothingItems(unittest.TestCase):
    @patch('requests.get')
    @patch('src.core.saveToFirestore.save_to_firestore')
    @patch('src.core.saveToStorage.upload_to_firebase_storage')
    @patch('src.core.canvasImage.compose_outfit_image')
    def test_upload_clothing_items_success(self, mock_compose_outfit_image, mock_upload_to_firebase_storage, mock_save_to_firestore, mock_requests_get):
        # Mock data
        mock_request = MagicMock()
        mock_request.json.return_value = {
            "urls": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
            "categories": ["top", "bottom"],
            "user_id": "user123"
        }
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'mock image content'
        mock_requests_get.return_value = mock_response
        # Mock function returns
        mock_outfit_image_io = MagicMock()
        mock_compose_outfit_image.return_value = mock_outfit_image_io
        mock_upload_to_firebase_storage.return_value = "https://example.com/outfit.png"
        mock_save_to_firestore.return_value = "document123"
        # Call the function
        with patch('your_module.request', mock_request):
            response = save_outfit.upload_clothing_items()
        # Assertions
        mock_compose_outfit_image.assert_called_once_with([
            {"category": "top", "bytes_io": mock.ANY},
            {"category": "bottom", "bytes_io": mock.ANY}
        ])
        mock_upload_to_firebase_storage.assert_called_once_with(mock_outfit_image_io, mock.ANY, "user123")
        mock_save_to_firestore.assert_called_once_with("https://example.com/outfit.png", mock.ANY, "user123")
        self.assertEqual(response.json(), {"document_id": "document123", "outfit_url": "https://example.com/outfit.png"})

    # Add more test cases for edge cases and failure scenarios as needed
if __name__ == '__main__':
    unittest.main()



