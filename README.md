# pytextcodifier

Turn your text files into codified images or your codified images into text files.

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

![Example](https://raw.githubusercontent.com/gabrielstork/text-codifier/main/images/example.png)

Every image has an 8-digit identifier (to be precise, the first 8 pixel values in the flattened image matrix). This identifier tells how the code should read the image, showing where the correct characters are located in the image matrix. A private image requires a key to correctly extract the text in it, in other side, if it is a non-private image, the text is extracted directly.

## Public

### Encoding

```python
from pytextcodifier import Encoder

# Instantiating the class
# The example.txt file contains the text: "This is an example!"
text = Encoder('example.txt', is_file=True)

# Encoding the text (Note: by default the generated image size is 250x250,
# and it is not private).
text.encode(size=(250, 250), private=False)

# Seeing the generated image
text.show()

# Saving the image
text.save('example.png')
```

### Decoding

```python
from pytextcodifier import Decoder

# Instantiating the class
# The example.png file contains the text: "This is an example!"
image = Decoder('example.png')

# Decoding the image
image.decode()

# Seeing the text
image.show()

# Saving the text
image.save('example.txt')
```

## Private

### Encoding

```python
from pytextcodifier import Encoder

# Instantiating the class
# The example.txt file contains the text: "This is an example!"
text = Encoder('example.txt', is_file=True)

# Encoding the text
text.encode(size=(250, 250), private=True)

# Saving the image
# This will save an extra image named 'key_example.png', you must use this to
# get the text correctly when decoding it
text.save('example.png')
```

### Decoding

```python
from pytextcodifier import Decoder

# Instantiating the class
# The example.png file contains the text: "This is an example!"
image = Decoder('example.png')

# Decoding the image
image.decode(key='key_example.png')

# Seeing the text
image.show()

# Saving the text
image.save('example.txt')
```

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/gabrielstork)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/gabrielstork)
