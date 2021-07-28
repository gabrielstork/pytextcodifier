import numpy as np
import cv2 as cv


CHARS = [chr(i) for i in range(256)]
ZEROS = np.zeros(8, dtype=np.uint8)


class Encoder:
    def __init__(self, path):
        with open(path, 'r') as file:
            self.text = file.read()

    def encode(self, size=(250, 250), private=False):
        identifier = ZEROS.copy()

        idx_list = [CHARS.index(char) for char in self.text]
        image = np.array(np.random.randint(0, 256, size), dtype=np.uint8)
        
        ravel = image.ravel()[8:]
        factor = str(int(ravel.shape[0] / len(idx_list)))

        for i in range(-1, -identifier.shape[0] - 1, -1):
            try:
                identifier[i] = int(factor[i])
            except IndexError:
                break

        if len(ravel) < len(idx_list):
            raise ValueError('image size is too small')
        else:
            if private:
                print('The generated image is private.\n'
                      'You can get the correct text knowing the identifier '
                      'while decoding it.\n'
                      f"Identifier: {''.join([str(n) for n in identifier])}")
                ravel = np.insert(ravel, 0, ZEROS)
            else:
                ravel = np.insert(ravel, 0, identifier)

            for pixel, char in zip(range(8, len(ravel) - int(factor),
                                         int(factor)), idx_list):
                ravel[pixel] = char

            self.image = ravel.reshape(size)

    def show(self):
        cv.imshow('Encoded Image', self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, path):
        cv.imwrite(path, self.image)


class Decoder:
    def __init__(self, path):
        self.image = cv.imread(path, cv.IMREAD_GRAYSCALE)
        self.text = ''

    def decode(self):
        ravel = self.image.ravel()
        identifier = ravel[:8]

        if (identifier == ZEROS).all():
            idf = str(input('This image is private.\n'
                            'Enter the identifier to get the text correctly.\n'
                            'Identifier: '))
            factor = int(idf)
        else:
            factors = [str(n) for n in identifier]
            factor = int(''.join(factors))

        for pos in range(8, len(ravel) - factor, factor):
            self.text += CHARS[ravel[pos]]

    def show(self):
        print(self.text)

    def save(self, path):
        with open(path, 'w') as file:
            file.write(self.text)
