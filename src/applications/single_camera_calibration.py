# --- External imports ---
import numpy as np
import sys
import os
# --- Internal imports ---
sys.path.append(os.path.abspath('../'))
from core.primitives.image import Image

"""
1. Images have the exif tag which has their intrinsic parameters! I can use this to check my estimation.
Estimate the camera's intrinsic parameters and the extrinsic parameters.
Use a dataset saved out to the filesystem.

2. Make an article talking about how to derive these. Build my portfolio and brand.
"""


if __name__ == "__main__":
	print("Hello Computer Vision!")

	pixels = np.array([[1, 2, 3], [4, 5, 6]])
	image = Image(pixels)




