import os
import string
import cv2 as cv


CHARS = list(string.printable)


class Image:
    def __init__(self, path):
        self.image = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.text = ""

        name = os.path.basename(path)
        self.name = ".".join(name.split(".")[:-1])

    def decode(self):
        ravel = self.image.ravel()
        identifier = ravel[:8]

        factors = [str(n) for n in identifier]
        factor = int("".join(factors))

        for pos in range(8, len(ravel) - factor, factor):
            self.text += CHARS[ravel[pos]]

    def show(self):
        print(self.text)

    def save(self, path):
        with open(path, "w") as file:
            file.write(self.text)
