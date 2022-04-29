import pathlib
import setuptools


def read(file: str) -> list:
    with open(file, encoding="utf-8") as r:
        return [i.strip() for i in r]


file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setuptools.setup(
    name="pytube",
    version="1.2.1",
    author="mrlokaman&AlexGmd",
    author_email="ln0technical@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
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
