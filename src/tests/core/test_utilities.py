# --- External imports ---
import pytest
# --- Internal imports ---
from computer_vision.code.src.core.primitives.image import Image


def are_images_equal(image_1: Image, image_2: Image) -> bool:
    """Checks if the two provided images have approximately equal pixel values.

    Returns:
        bool:
            True iff the two provided images have approximately equal pixel values.
    """
    assert image_1.width == image_2.width
    assert image_2.height == image_2.height

    image_1_pixels = image_1.pixels
    image_2_pixels = image_2.pixels
    for row_index in range(image_1.height):
        for column_index in range(image_1.width):
            if not image_1_pixels[row_index][column_index] == \
                   pytest.approx(image_2_pixels[row_index][column_index]):
                return False
    return True
