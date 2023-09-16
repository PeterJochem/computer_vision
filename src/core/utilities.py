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
