import numpy as np
import cv2

from favourites import favourites

array = [[0, 1], [0, 2], [0, 3], [0, 5], [0, 6], [1, 1], [1, 2], [1, 4], [1, 5], [1, 7], [2, 1], [2, 3], [2, 5], [2, 6]]
favourites.massPointDisplacementFromBlock(favourites, array, [0, 2] )
