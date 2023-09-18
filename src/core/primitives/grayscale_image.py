# --- External imports ---
import numpy as np
from PIL import Image as PILImage
# --- Internal imports ---
from computer_vision.code.src.core.primitives.image import Image


class GrayscaleImage(Image):

    def __init__(self, pixels: np.ndarray):
        """Constructor."""
        super().__init__(pixels)

    @staticmethod
    def create_empty_image(height: int, width: int) -> "Image":
        """Constructs an image where all pixel values are 0.

        Args:
            height: int
                The image's height in pixels.
            width: int
                The image's width in pixels.

        Returns:
            Image:
                An image where all pixel values are 0.
        """
        pixels = np.zeros((height, width))
        return GrayscaleImage(pixels)

    @staticmethod
    def create_from_path(path: str) -> "Image":
        """Constructs ...

        Args:
            path: str
                The ...

        Returns:
            Image:
                ...
        """
        pixels = np.asarray(PILImage.open(path))
        return to_grayscale_from_pixels(pixels)

    def get(self, row: int, column: int) -> float:
        """..."""
        # if is_pixel_in_image ...
        return self.pixels[row][column]

    def set(self, row: int, column: int, value: float):
        """..."""
        # if is_pixel_in_image ...
        self.pixels[row][column] = value


def rgb2gray(pixel: np.ndarray) -> float:
    """..."""
    r, g, b = pixel[0], pixel[1], pixel[2]
    return (0.2989 * r) + (0.5870 * g) + (0.1140 * b)


def to_grayscale(image: "RGBImage") -> "GrayscaleImage":
    """..."""
    grayscale_image = GrayscaleImage.create_empty_image(image.width, image.height)
    for row_index in range(image.height):
        for column_index in range(image.width):
            grayscale_pixel = rgb2gray(image.get(row_index, column_index))
            grayscale_image.set(row_index, column_index, grayscale_pixel)
    return grayscale_image


def to_grayscale_from_pixels(pixels: np.ndarray) -> GrayscaleImage:
    """..."""
    height, width, depth = pixels.shape
    grayscale_pixels = np.zeros((height, width))
    for row_index in range(height):
        for column_index in range(width):
            grayscale_pixel = rgb2gray(pixels[row_index][column_index])
            grayscale_pixels[row_index][column_index] = grayscale_pixel
    return GrayscaleImage(grayscale_pixels)
