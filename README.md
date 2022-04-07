# pytextcodifier

Codify your text files or Python strings.

You can simply:

```shell
pip install pytextcodifier
```

Or you can also:

1. Clone the repository to your local machine.
2. Enter the directory.
3. Download necessary modules/libraries.

```sh
git clone https://github.com/gabrielstork/pytextcodifier.git
cd pytextcodifier
pip install -r requirements.txt
```

## About

**pytextcodifier** allows you transform Python strings or text files (check `example.txt` and see the text file used to generate the image below) into encoded images like this:

![Example](https://raw.githubusercontent.com/gabrielstork/pytextcodifier/main/images/public_example.png)

Every image matrix has two 8 digit arrays called *stop* and *identifier* (to be precise, the first 16 pixel values in the flattened image matrix). The identifier tells how the code should read the image, showing where the correct characters are located in the matrix. A private image requires a key to correctly extract the text in it, on the other side, if it is a non-private image, the text is extracted directly.

## Examples

### Public Encoding

Importing `Encoder` class.

```python
from pytextcodifier import Encoder
```

Using the content of `example.txt`.

```python
text = Encoder('example.txt', is_file=True)
```

Using `encode()` method with default arguments to actually encode it.

```python
text.encode(size=(250, 250), private=False)
```

Seeing the generated encoded image (a new window will pop up).

```python
text.show()
```

Saving it.

```python
text.save('images/public_example.png')
```

### Public Decoding

Importing `Decoder` class.

```python
from pytextcodifier import Decoder
```

Instantiating the class passing an image as argument.

```python
image = Decoder('example.png')
```

Decoding the image.

```python
image.decode()
```

Seeing the text.

```python
image.show()
```

Saving the text.

```python
image.save('example.txt')
```

### Private Encoding

Importing `Encoder` class.

```python
from pytextcodifier import Encoder
```

Using the content of `example.txt`.

```python
text = Encoder('example.txt', is_file=True)
```

Using `encode()` method setting the `private` parameter to `True`.

```python
text.encode(size=(250, 250), private=True)
```

Saving it. This will save an extra image named 'key_private_example.png', you must use this to
get the text correctly when decoding it.

```python
text.save('images/private_example.png')
```

### Private Decoding

Importing `Decoder` class.

```python
from pytextcodifier import Decoder
```

Instantiating the class passing an image as argument.

```python
image = Decoder('example.png')
```

Decoding the image.

```python
image.decode(key='key_private_example.png')
```

Seeing the text.

```python
image.show()
```

Saving the text.

```python
image.save('example.txt')
```

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/gabrielstork)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/gabrielstork)
