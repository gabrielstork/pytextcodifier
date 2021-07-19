# text-codifier

Turn your text files into codified images or your codified images into text files.

## Encoding a Text File

`decenc.py` comes from **dec**oder and **enc**oder.

Let's suppose we have a text file with the following content:

```
This is an example!
```

If we want to make a encoded image for this, we need to follow these steps:

1. Import everything.

```python
from decenc import *
```

## Encoding a Text File

```python
# Instantiating the class
text = Encoder("example.png")

# Decoding the image
text.encode()

# Seeing the text
text.show()
```


```python
image.save("example.txt")
```

## Decoding an Image File

```python
# Instantiating the class
image = Decoder("example.png")

# Decoding the image
image.decode()

# Seeing the text
image.show()
```
```
This is an example!
```
```python
image.save("example.txt")
```