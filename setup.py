# from distutils.core import setup
from setuptools import setup

setup(
    name='img_utils',
    version='0.0.5',
    packages=['images', 'files', 'colors'],
    url='https://github.com/DewMaple/image_utils',
    description='Convenient functions that help to process images',
    author='dew.maple',
    author_email='dew.maple@gmail.com',
    license='MIT',
    keywords=['computer vision', 'image processing', 'opencv', 'numpy'],
    classifiers=['Programming Language :: Python :: 3.6'],
    project_urls={
        'Bug Reports': 'https://github.com/DewMaple/image_utils/issues',
        'Source': 'https://github.com/DewMaple/image_utils',
    }
)
