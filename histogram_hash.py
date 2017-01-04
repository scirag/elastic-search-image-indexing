import cv2
import numpy as np


def read_image(image_path):
    """reads image by opencv"""
    return cv2.imread(image_path)


def histogram_matrix(image_path, resize_dim=32, num_bins=16):
    """reads RGB image and returns histogram matrix of BGR bands"""
    img = read_image(image_path)
    resized_image = cv2.resize(img, (resize_dim, resize_dim))
    hist_array = []
    for band in range(3):
        hist = cv2.calcHist([resized_image], [band], None, [num_bins], [0, 256])
        hist_array.append(hist.T[0].astype(int))
    return hist_array


def histogram_hash(hist_matrix, pixel_count):
    """converts histogram matrix into hexidecimal string.
       first divide matrix values by pixel_count in order to find frequency.
       second map values in range [0,1] to values in range [0,15]
       finally join hexidecimal values as string
    """
    result_hash = ""
    for band_hist in hist_matrix:
        freq = band_hist/pixel_count
        hex_values = np.interp(freq, [0, 1], [0, 15])
        hex_values = np.round(hex_values, decimals=0).astype(np.int16)
        hex_string = "".join([hex(val)[2:] for val in hex_values])
        result_hash += hex_string
    return result_hash


def hamming_distance(hash1, hash2):
    bin1 = '{0:b}'.format(int(hash1, 16))
    bin2 = '{0:b}'.format(int(hash2, 16))
    return sum(c1 != c2 for c1, c2 in zip(bin1, bin2))
