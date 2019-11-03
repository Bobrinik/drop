from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Drop',
    version='1.0',
    author='Maksim Bober',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['drop'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'drop = drop:cli',
        ],
    },
    packages=find_packages(),
)
