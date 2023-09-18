# --- External imports ---
from abc import abstractmethod, ABC
from typing import Union
import numpy as np
# --- Internal imports ---
from matplotlib import pyplot as plt


class Image(ABC):
    """
    Represents a 2-D image.
    """
    def __init__(self, pixels: np.ndarray):
        """Constructor.

        Args:
            pixels: numpy.ndarray
                The image's pixels.
        """
        self.pixels = pixels

    @staticmethod
    @abstractmethod
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
        pass

    @staticmethod
    @abstractmethod
    def create_from_path(path: str) -> "Image":
        """Constructs ...

        Args:
            path: str
                The ...

        Returns:
            Image:
                ...
        """
        pass

    @property
    def pixels(self) -> np.ndarray:
        """Gets the image's pixels.

        Returns:
            numpy.ndarray:
                The image's pixels.

        Raises:
            RuntimeError:
                If the image's pixels are None.
        """
        if self._pixels is None:
            raise RuntimeError("The image's pixels are None.")
        return self._pixels

    @pixels.setter
    def pixels(self, input_value: np.ndarray):
        """Sets the image's pixels.

        Args:
            input_value: numpy.ndarray
                The image's pixels.

        Raises:
            TypeError:
                If the provided pixels are not a numpy array.
        """
        if not isinstance(input_value, np.ndarray):
            raise TypeError("The provided pixels are not a numpy array.")
        self._pixels = input_value
        self.width = self.extract_width_from_pixels()
        self.height = self.extract_height_from_pixels()

    @property
    def height(self) -> int:
        """Gets the image's height in pixels.

        Returns:
            int:
                The image's height in pixels.

        Raises:
            RuntimeError:
                If the image's height is None.
        """
        if self._height is None:
            raise RuntimeError("The image's height is None.")
        return self._height

    @height.setter
    def height(self, input_value: int):
        """Sets the image's height in pixels.

        Args:
            input_value: int
                The image's height in pixels.

        Raises:
            TypeError:
                If the provided height is not an int.
        """
        if not isinstance(input_value, int):
            raise TypeError("The provided height is not an integer.")
        self._height = input_value

    @property
    def width(self) -> int:
        """Gets the width of the image in pixels.

        Returns:
            int:
                The width of the image in pixels.

        Raises:
            RuntimeError:
                If the image's width is None.
        """
        if self._width is None:
            raise RuntimeError("The image width has not been set.")
        return self._width

    @width.setter
    def width(self, input_value: int):
        """Sets the image's width in pixels.

        Args:
            input_value: int
                The image's width in pixels.

        Raises:
            TypeError:
                If the provided width is not an integer.
        """
        if not isinstance(input_value, int):
            raise TypeError("The provided width is not an integer.")
        self._width = input_value

    @abstractmethod
    def get(self, row: int, column: int) -> Union[float, np.ndarray]:
        """..."""
        pass

    @abstractmethod
    def set(self, row: int, column: int, value: Union[float, np.ndarray]):
        """..."""
        pass

    def view(self):
        """..."""
        plt.imshow(self.pixels)
        plt.show()

    def extract_height_from_pixels(self) -> int:
        """..."""
        return len(self.pixels)

    def extract_width_from_pixels(self) -> int:
        return len(self.pixels[0])
