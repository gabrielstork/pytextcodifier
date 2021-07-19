# text-codifier

Turn your text files into codified images or your codified images into text files.

`decenc.py` comes from **dec**oder and **enc**oder.

```python
from decenc import *
```

## Encoding a Text File

```python
# Instantiating the class
# The example.txt file contains the text: "This is an example!"
text = Encoder("example.txt")

# Encoding the text (Note: by default the generated image size is 250x250,
# you can change it to any value you want)
text.encode(size=(250, 250))

# Seeing the generated image
text.show()
```

*Output:*

![Example](https://github.com/gabrielstork/text-codifier/blob/main/images/example.png)

```python
# Saving the image
image.save("example.png")
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

*Output:*

```
This is an example!
```

```python
# Saving the text
image.save("example.txt")
```