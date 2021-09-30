import numpy as np
import cv2 as cv

CHARS = [chr(i) for i in range(256)]
ZEROS = np.zeros(8, dtype=np.uint8)


class Encoder:
    def __init__(self, text: str, is_file: bool = False) -> None:
        if is_file:
            with open(text, 'r') as file:
                self.text = file.read()
        else:
            self.text = text

        self.identifier = ZEROS.copy()

    def _set_identifier(self, factor: str):
        for i in range(-1, -self.identifier.shape[0] - 1, -1):
            try:
                self.identifier[i] = int(factor[i])
            except IndexError:
                break

    def _insert_identifier(self, ravel, private: bool):
        if private:
            ravel = np.insert(ravel, 0, ZEROS)
            print(f'Identifier: {"".join([str(n) for n in self.identifier])}')
        else:
            ravel = np.insert(ravel, 0, self.identifier)

        return ravel

    def encode(self, size: tuple = (250, 250), private: bool = False) -> None:
        idx_list = [CHARS.index(char) for char in self.text]
        image = np.array(np.random.randint(0, 256, size), dtype=np.uint8)

        ravel = image.ravel()[8:]
        factor = str(int(ravel.shape[0] / len(idx_list)))

        self._set_identifier(factor)

        if len(ravel) < len(idx_list):
            raise ValueError('image size is too small')

        ravel = self._insert_identifier(ravel, private)

        for pixel, char in zip(range(8, len(ravel) - int(factor), int(factor)), idx_list):
            ravel[pixel] = char

        self.image = ravel.reshape(size)

    def show(self) -> None:
        cv.imshow('Encoded Image', self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, path: str) -> None:
        cv.imwrite(path, self.image)


class Decoder:
    def __init__(self, path: str) -> None:
        self.image = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.text = ''

    def decode(self) -> None:
        ravel = self.image.ravel()
        identifier = ravel[:8]

        if (identifier == ZEROS).all():
            idf = str(input('Identifier: '))
            factor = int(idf)
        else:
            factors = [str(n) for n in identifier]
            factor = int(''.join(factors))

        for pos in range(8, len(ravel) - factor, factor):
            self.text += CHARS[ravel[pos]]

    def show(self) -> None:
        print(self.text)

    def save(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(self.text)
