import numpy as np

class Image:
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

    @property
    def pixels(self) -> np.ndarray:
        """Gets the images pixels.

        Returns:
            numpy.ndarray:
                The images pixels.

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
            raise TypeError("...")
        self._pixels = input_value
        self.width = self.extract_width_from_pixels()
        self.height = self.extract_height_from_pixels()

    @property
    def height(self) -> int:
        """Gets the image's height in pixels.

        Returns:
            int:
                The images height in pixels.

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
            raise TypeError("...")
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
            raise RuntimeError("...")
        return self._width

    @width.setter
    def width(self, input_value: int):
        """Sets the image's width in pixels.

        Args:
            input_value: int
                The images width in pixels.

        Raises:
            TypeError:
                If the provided width is not an int.
        """
        if not isinstance(input_value, int):
            raise TypeError("...")
        self._width = input_value

    def extract_height_from_pixels(self) -> int:
        """..."""
        return len(self.pixels)

    def extract_width_from_pixels(self) -> int:
        return len(self.pixels[0])
