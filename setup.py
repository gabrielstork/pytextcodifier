import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='pytextcodifier',
    version='1.0.0',
    description='Codify your text files or Python strings.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/pytextcodifier',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='text encoder decoder strings codification',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'opencv-python'],
    python_requires='>=3',
)
