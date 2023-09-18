# --- External imports ---
import numpy as np
import pytest
# --- Internal imports ---
from computer_vision.code.src.core.edge_detection.sobel_edge_detector import SobelEdgeDetector
from computer_vision.code.src.core.edge_detection.sobel_edge_detector_parameters import SobelEdgeDetectorParameters
from computer_vision.code.src.core.primitives.grayscale_image import GrayscaleImage
from computer_vision.code.src.core.primitives.image import Image
from computer_vision.code.src.tests.core.test_utilities import are_images_equal

constant_column_pixels = np.array([[5, 5, 5, 5, 5],
                                   [4, 4, 4, 4, 4],
                                   [3, 3, 3, 3, 3],
                                   [2, 2, 2, 2, 2],
                                   [1, 1, 1, 1, 1]])
expected_constant_column_pixels_edges = GrayscaleImage(np.zeros((5, 5)))

pixels_2 = np.zeros((5, 5))
pixels_2[2][2] = 1.
expected_edge_image_2 = GrayscaleImage(np.array([[0., 0., 0., 0., 0.],
                                                 [0., 1., 0., -1., 0.],
                                                 [0., 2., 0, -2., 0.],
                                                 [0., 1., 0., -1., 0.],
                                                 [0., 0., 0., 0., 0.]]))


@pytest.mark.parametrize("pixels, expected_edge_image",
                         [(constant_column_pixels, expected_constant_column_pixels_edges),
                          (pixels_2, expected_edge_image_2)])
def test_dummy(pixels: np.ndarray, expected_edge_image: Image):
    image = GrayscaleImage(pixels)
    parameters = SobelEdgeDetectorParameters(detect_vertical=True)
    edge_detector = SobelEdgeDetector(parameters)
    edges = edge_detector.detect(image)
    # assert are_images_equal(edges, expected_edge_image)
    edges.view()
    print(image.width)
    print(image.height)


def test_dummy_2():
    return True
    path = "/Users/peterjochem/Desktop/Personal_Learning/computer_vision/code/data/Lenna_binary.png"
    image = GrayscaleImage.create_from_path(path)
    # image.view()
    print("")
    print(image.pixels)
    print(image.width)
    print(image.height)
    print(image.pixels.shape)
    parameters = SobelEdgeDetectorParameters(detect_vertical=True)
    edge_detector = SobelEdgeDetector(parameters)
    edges = edge_detector.detect(image)
    edges.view()
