# --- External imports ---
import numpy as np
from computer_vision.code.src.core.primitives.image import Image


def is_pixel_in_image(image: Image, row: int, column: int) -> bool:
    """Checks if the given coordinates are in the image.

    Args:
        image: Image
        row: int
        column: int

    Returns:
        bool:
            True iff the coordinates are in the image.
    """
    return (row >= 0) and (column >= 0) and (row < image.height) and (column < image.width)


def rgb2gray(pixel: np.ndarray) -> float:
    """..."""
    r, g, b = pixel[:,:,0], pixel[:,:,1], pixel[:,:,2]
    return (0.2989 * r) + (0.5870 * g) + (0.1140 * b)


def to_grayscale(image: Image) -> Image:
    """..."""
    grayscale_image = Image.create_empty_image(image.width, image.height)
    for row_index in range(image.height):
        for column_index in range(image.width):
            grayscale_pixel = rgb2gray(image.get(row_index, column_index))
            grayscale_image.set(row_index, column_index, grayscale_pixel)
    return grayscale_image
