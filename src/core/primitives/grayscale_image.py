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
        return Image(pixels)

    def get(self, row: int, column: int) -> float:
        """..."""
        # if is_pixel_in_image ...
        return self.pixels[row][column]

    def set(self, row: int, column: int, value: float):
        """..."""
        # if is_pixel_in_image ...
        self.pixels[row][column] = value
