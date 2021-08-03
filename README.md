# text-codifier

Turn your text files into codified images or your codified images into text files.

Steps to use:

1. Clone the repository to your local machine.
2. Enter the directory.
3. Download necessary modules/libraries.

```sh
git clone https://github.com/gabrielstork/text-codifier.git
cd text-codifier
pip install -r requirements.txt
```

## About

The `decenc.py` allows you transform text files (check `example.txt` and see the text file used to generate the image below) into encoded images like this:

![Example](https://github.com/gabrielstork/text-codifier/blob/main/images/example.png)

Every image has an 8-digit identifier attached in it (to be precise, the first 8 pixel values in the flattened image matrix). This identifier tells how the code should read the image. A private image requires the user to input the identifier to correctly extract the text in it, in other side, if it is a non-private image, the text is extracted directly.

## Encoding

```python
from decenc import Encoder

# Instantiating the class
# The example.txt file contains the text: "This is an example!"
text = Encoder('example.txt')

# Encoding the text (Note: by default the generated image size is 250x250,
# and it is not private).
text.encode(size=(250, 250), private=False)

# Seeing the generated image
text.show()

# Saving the image
text.save('example.png')
```

## Decoding

```python
from decenc import Decoder

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

## Private Encoding

```python
from decenc import Encoder

# Instantiating the class
# The example.txt file contains the text: "This is an example!"
text = Encoder('example.txt')

# Encoding the text
text.encode(size=(250, 250), private=True)
```

You will get this message:

```text
The generated image is private.
You can get the correct text knowing the identifier while decoding it.
Identifier: 00003289
```

## Private Decoding

```python
from decenc import Decoder

# Instantiating the class
# The example.png file contains the text: "This is an example!"
image = Decoder('example.png')

# Decoding the image
image.decode()
```

You will get this, and you need to input the identifier.

```text
This image is private.
Enter the identifier to get the text correctly.
Identifier: 
```
