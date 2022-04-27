import setuptools
import pathlib


def read(file: str) -> list:
    with open(file, encoding="utf-8") as r:
        return [i.strip() for i in r]


file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setuptools.setup(
    name="pytube",
    version="0.2.2",
    author="AlexGmB",
    author_email="None",
    description="Python library Get YouTube Video Data",
    license="MIT",
    url="https://github.com/alex006-cloud/pytube",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires = read(""),
    python_requires=">=3.6"
)
