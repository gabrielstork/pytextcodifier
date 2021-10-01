import numpy as np
import cv2 as cv
import pathlib

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
        self._image = ZEROS.copy()
        self._private = None

    def _set_identifier(self, factor: str):
        for i in range(-1, -self.identifier.shape[0] - 1, -1):
            try:
                self.identifier[i] = int(factor[i])
            except IndexError:
                break
        
    def _insert_identifier(self, ravel: np.ndarray) -> np.ndarray:
        if self._private:
            joined_ravel = np.insert(ravel, 0, ZEROS)
        else:
            joined_ravel = np.insert(ravel, 0, self.identifier)

        return joined_ravel

    def encode(self, size: tuple = (250, 250), private: bool = False) -> None:
        self._private = private

        image = np.array(np.random.randint(0, 256, size), dtype=np.uint8)
        partial_ravel = image.ravel()[8:]

        idx_list = [CHARS.index(char) for char in self.text]
        factor = str(int(partial_ravel.shape[0] / len(idx_list)))

        self._set_identifier(factor)

        if len(partial_ravel) < len(idx_list):
            raise ValueError('image size is too small')

        ravel = self._insert_identifier(partial_ravel)

        pos = zip(range(8, len(ravel) - int(factor), int(factor)), idx_list)

        for pixel, char in pos:
            ravel[pixel] = char

        self._image = ravel.reshape(size)

    def show(self) -> None:
        cv.imshow('Encoded Image', self._image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, path: str) -> None:
        if self._private:
            image_path = pathlib.Path(path)
            cv.imwrite(
                str(image_path.parent.resolve() / f'key_{image_path.name}'),
                self.identifier,
            )

        cv.imwrite(path, self._image)


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
