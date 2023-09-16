# --- External imports ---
import numpy as np
import pytest
# --- Internal imports ---
from computer_vision.code.src.core.edge_detection.sobel_edge_detector import SobelEdgeDetector
from computer_vision.code.src.core.primitives.image import Image


def are_images_equal(image_1: Image, image_2: Image) -> bool:
    """..."""

    assert image_1.width == image_2.width
    assert image_2.height == image_2.height

    image_1_pixels = image_1.pixels
    image_2_pixels = image_2.pixels
    for row_index in range(image_1.height):
        for column_index in range(image_1.width):
            if not image_1_pixels[row_index][column_index] == pytest.approx(image_2_pixels[row_index][column_index]):
                return False
    return True

pixels_1 = np.array([[5, 5, 5, 5, 5],
                     [4, 4, 4, 4, 4],
                     [3, 3, 3, 3, 3],
                     [2, 2, 2, 2, 2],
                     [1, 1, 1, 1, 1]])
expected_edge_image_1 = Image(np.zeros((5, 5)))

pixels_2 = np.zeros((5, 5))
pixels_2[2][2] = 1.
expected_edge_image_2 = Image(np.array([[0., 0., 0., 0., 0.],
                                        [0., 1., 0., -1., 0.],
                                        [0., 2., 0, -2., 0.],
                                        [0., 1., 0., -1., 0.],
                                        [0., 0., 0., 0., 0.]]))


@pytest.mark.parametrize("pixels, expected_edge_image", [(pixels_1, expected_edge_image_1),
                                                         (pixels_2, expected_edge_image_2)])
def test_dummy(pixels, expected_edge_image):
    image = Image(pixels)
    edge_detector = SobelEdgeDetector()
    edges = edge_detector.detect(image)
    assert are_images_equal(edges, expected_edge_image)
