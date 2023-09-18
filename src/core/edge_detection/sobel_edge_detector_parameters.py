# --- External imports ---
import numpy as np

vertical_edge_kernel = np.array([[-1, 0, 1],
                                 [-2, 0, 2],
                                 [-1, 0, 1]])

horizontal_edge_kernel = np.array([[-1, -2, 1],
                                   [0, 0, 0],
                                   [1, 2, 1]])


class SobelEdgeDetectorParameters:
    """
    A class which parameterizes the SobelEdgeDetector.
    """
    def __init__(self, detect_vertical: bool):
        """Constructor.

        Args:
            detect_vertical: bool
                Indicates if we are detecting vertical or horizontal edges.
        """
        self.detect_vertical = detect_vertical
        if self.detect_vertical:
            self.kernel = vertical_edge_kernel
        else:
            self.kernel = horizontal_edge_kernel

    @property
    def detect_vertical(self) -> bool:
        """Detects if this instance has been assigned a boolean indicating
        which direction to detect edges.

        Returns:
            bool:
                True iff this instance has a boolean indicating in which direction to detect edges.
        """
        if not self.has_detect_vertical():
            raise RuntimeError("The detect vertical flag has not been set.")
        return self._detect_vertical

    @detect_vertical.setter
    def detect_vertical(self, input_value: bool):
        """Sets this instance's boolean indicating which direction to check for edges.

        Args:
            input_value: bool
                Indicates which direction to check for edges.
        """
        if not isinstance(input_value, bool):
            raise TypeError("The provided detect vertical argument is not a boolean.")
        self._detect_vertical = input_value

    def has_detect_vertical(self) -> bool:
        """Checks if this instance has been assigned a boolean indicating which direction
        to check for edges.

        Returns:
            bool:
                True iff this instance has a boolean indicating which direction to check
                for edges.
        """
        return self._detect_vertical is not None

    @property
    def kernel(self) -> np.ndarray:
        """..."""
        if not self.has_kernel():
            raise RuntimeError("This instance hasn't been assigned a kernel.")
        return self._kernel

    @kernel.setter
    def kernel(self, input_value: np.ndarray):
        """..."""
        if not isinstance(input_value, np.ndarray):
            raise TypeError("The provided kernel isn't a numpy array.")
        self._kernel = input_value

    def has_kernel(self) -> bool:
        """Checks if this instance has been assigned a kernel.

        Returns:
            bool:
                True iff this instance has been assigned a kernel.
        """
        return self._kernel is not None
