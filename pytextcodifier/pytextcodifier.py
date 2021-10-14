import numpy as np
import cv2 as cv
import pathlib
import typing

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
        self.stop = ZEROS.copy()
        self.image = np.zeros((250, 250), dtype=np.uint8)

    def _set_identifier(self, factor: str):
        for i in range(-1, -self.identifier.shape[0] - 1, -1):
            try:
                self.identifier[i] = int(factor[i])
            except IndexError:
                break

    def _set_stop(self, pixel: str):
        for i in range(-1, -self.stop.shape[0] - 1, -1):
            try:
                self.stop[i] = int(pixel[i])
            except IndexError:
                break

    def _insert_arrays(self, ravel: np.ndarray) -> np.ndarray:
        identifier_insert = np.insert(
            ravel, 0, ZEROS if self._private else self.identifier
        )
        stop_insert = np.insert(identifier_insert, 0, self.stop)
        return stop_insert

    def encode(self, size: tuple = (250, 250), private: bool = False) -> None:
        self._private = private

        image = np.array(np.random.randint(0, 256, size), dtype=np.uint8)
        partial_ravel = image.ravel()[16:]
        index_list = [CHARS.index(char) for char in self.text]

        if len(partial_ravel) < len(index_list):
            raise ValueError('image size is too small')

        factor = int(partial_ravel.shape[0] / len(index_list))

        pixels_factor = zip(range(0, len(partial_ravel), factor), index_list)

        for pixel, char in pixels_factor:
            partial_ravel[pixel] = char

        if (pixel + factor) < len(partial_ravel):
            self._set_stop(str(pixel + factor + 16))

        self._set_identifier(str(factor))
        ravel = self._insert_arrays(partial_ravel)
        self.image = ravel.reshape(size)

    def show(self) -> None:
        cv.imshow('Encoded Image', self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, path: str) -> None:
        if self._private:
            image_path = pathlib.Path(path)
            cv.imwrite(
                str(image_path.parent.resolve() / f'key_{image_path.name}'),
                np.concatenate((self.stop, self.identifier)),
            )

        cv.imwrite(path, self.image)


class Decoder:
    def __init__(self, path: str) -> None:
        self.image = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.text = ''

    def _get_identifier(self, key: str) -> np.ndarray:
        key_array = cv.imread(key, cv.IMREAD_GRAYSCALE)
        identifier = key_array.ravel()[8:]
        return identifier

    def _get_factor(self, identifier: np.ndarray) -> int:
        factor = [str(n) for n in identifier]
        factor = int(''.join(factor))
        return factor

    def _get_index(self, stop: np.ndarray) -> int:
        index = [str(n) for n in stop]
        index = int(''.join(index))
        return index

    def decode(self, key: typing.Optional[str] = None) -> None:
        ravel = self.image.ravel()
        stop = ravel[:8]
        identifier = ravel[8:16]

        if (identifier == ZEROS).all():
            identifier = self._get_identifier(key)

        factor = self._get_factor(identifier)
        index = self._get_index(stop)

        for pos in range(16, len(ravel) if index == 0 else index, factor):
            self.text += CHARS[ravel[pos]]

    def show(self) -> None:
        print(self.text)

    def save(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(self.text)
