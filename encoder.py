import os
import string
import numpy as np
import cv2 as cv


CHARS = list(string.printable)


class Text:
    def __init__(self, path):
        with open(path, "r") as file:
            self.text = file.read()
        self.name = os.path.basename(path)

    def encode(self, size=(250, 250)):
        idx_list = [CHARS.index(char) for char in self.text]
        image = np.array(np.random.randint(0, 255, size), dtype=np.uint8)
        ravel = image.ravel()[8:]

        identifier = np.zeros(8, dtype=np.uint8)

        factor = str(int(ravel.shape[0] / len(idx_list)))

        for i in range(-1, -identifier.shape[0] - 1, -1):
            try:
                identifier[i] = int(factor[i])
            except IndexError:
                break

        ravel = np.insert(ravel, 0, identifier)

        if ravel.shape[0] < len(idx_list):
            raise ValueError("image size too small")

        for pixel, char in zip(range(8, len(ravel), int(factor)), idx_list):
            ravel[pixel] = char

        self.image = ravel.reshape(size)

    def save(self, extension="png"):
        name = self.name.split(".")[0]
        cv.imwrite(f"{name}.{extension}", self.image)

    def show(self):
        cv.imshow("Image", self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()
