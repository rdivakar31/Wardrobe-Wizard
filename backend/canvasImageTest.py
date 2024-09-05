from PIL import Image
from io import BytesIO
from src.core.canvasImage import compose_outfit_image
# Assuming CLOTHING_CATEGORIES is defined as per  existing setup
CLOTHING_CATEGORIES = {
    'top': 'Top',
    'accessories': 'Accessories',
    'bottom': 'Bottom',
    'shoes': 'Shoes'
}

def create_mock_image(color, size=(100, 100)):
    """
    Creates a simple colored square image for testing.
    """
    img = Image.new('RGBA', size, color)
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)
    return img_io

def prepare_items_data():
    """
    Prepares items_data with mock images for testing.
    """
    items_data = [
        {'category': 'top', 'bytes_io': create_mock_image('red')},
        {'category': 'accessories', 'bytes_io': create_mock_image('blue')},
        {'category': 'bottom', 'bytes_io': create_mock_image('green')},
        {'category': 'shoes', 'bytes_io': create_mock_image('yellow')}
    ]
    return items_data

# Include the implementations of compute_layout, dynamic_resize_and_place_images, and compose_outfit_image here

def test_compose_outfit_image():
    items_data = prepare_items_data()
    result_io = compose_outfit_image(items_data, canvas_width=300, canvas_height=380)

    # Assertions
    assert isinstance(result_io, BytesIO), "Result should be a BytesIO object"

    result_image = Image.open(result_io)
    assert result_image.size == (300, 380), "Resulting image size is incorrect"



    print("Test Passed!")

# Run the test
test_compose_outfit_image()
