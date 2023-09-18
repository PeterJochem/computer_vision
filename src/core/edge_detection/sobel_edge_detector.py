# --- External imports ---
import numpy as np
# --- Internal imports ---
from computer_vision.code.src.core.edge_detection.edge_detector import EdgeDetector
from computer_vision.code.src.core.edge_detection.sobel_edge_detector_parameters import SobelEdgeDetectorParameters
from computer_vision.code.src.core.primitives.grayscale_image import GrayscaleImage
from computer_vision.code.src.core.primitives.image import Image
from computer_vision.code.src.core.utilities import is_pixel_in_image


class SobelEdgeDetector(EdgeDetector):
    """
    A class which implements the Sobel edge detection algorithm.
    """
    def __init__(self, parameters: SobelEdgeDetectorParameters):
        """Constructor.

        Args:
            parameters: SobelEdgeDetectorParameters
                Parameterize the edge detection algorithm.
        """
        super().__init__()
        self.parameters = parameters
        self.kernel = parameters.kernel

    def detect(self, image: Image) -> Image:
        """Detects edges in the provided image.

        Args:
            image: Image
                The image to detect edges in.

        Returns:
            Image:
                The edges from the provided image.
        """
        result_image = GrayscaleImage.create_empty_image(image.height, image.width)
        for row_index in range(image.height):
            for column_index in range(image.width):
                value = self.apply_kernel(image, row_index, column_index)
                result_image.set(row_index, column_index, value)
        return result_image

    def can_apply_kernel(self, image: Image, row: int, column: int) -> bool:
        """Checks if the given kernel can be applied at the provided coordinates in the image.

        We can only apply the kernel at a coordinate if the kernel fits entirely on the image when
        centered at the coordinate.

        Args:
            image: Image
                The image to check one of its pixels for kernel application.
            row: int
                The row coordinate of the pixel in the image.
            column: int
                The column coordinate of the pixel in the image.

        Returns:
            bool:
                True iff the given kernel can be applied at the provided coordinates in the image.
        """
        kernel_height = len(self.kernel)
        kernel_width = len(self.kernel[0])
        for row_delta, kernel_row_index in zip([-1, 0, 1], range(kernel_height)):
            for column_delta, kernel_column_index in zip([-1, 0, 1], range(kernel_width)):
                row_index = row + row_delta
                column_index = column + column_delta
                if not is_pixel_in_image(image, row_index, column_index):
                    return False
        return True

    def apply_kernel(self, image: Image, row: int, column: int) -> float:
        """Applies the edge detection kernel to the image at the indicated coordinates.

        Args:
            image: Image
                The image to apply the edge detection kernel to.
            row: int
                The row coordinate in the image.
            column: int
                The column coordinate in the image.
        """
        if not self.can_apply_kernel(image, row, column):
            return 0.
        kernel_height = len(self.kernel)
        kernel_width = len(self.kernel[0])
        sum = 0.
        for row_delta, kernel_row_index in zip([-1, 0, 1], range(kernel_height)):
            for column_delta, kernel_column_index in zip([-1, 0, 1], range(kernel_width)):
                row_index = row + row_delta
                column_index = column + column_delta
                sum += self.kernel[kernel_row_index][kernel_column_index] * \
                       image.get(row_index, column_index)
        return sum
