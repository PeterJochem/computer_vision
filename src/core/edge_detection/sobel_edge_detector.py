# --- External imports ---
import numpy as np
# --- Internal imports ---
from computer_vision.code.src.core.edge_detection.edge_detector import EdgeDetector
from computer_vision.code.src.core.primitives.image import Image
from computer_vision.code.src.core.utilities import is_pixel_in_image


class SobelEdgeDetector(EdgeDetector):
    """
    ...
    """
    def __init__(self):
        """Constructor."""
        self.kernel = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])

    def detect(self, image: Image) -> Image:
        """..."""

        result_image = Image.create_empty_image(image.height, image.width)
        for row_index in range(image.height):
            for column_index in range(image.width):
                value = self.apply_kernel(image, row_index, column_index)
                result_image.set(row_index, column_index, value)
        return result_image

    def can_apply_kernel(self, image: Image, row: int, column: int) -> bool:
        """..."""
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
        """..."""
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


