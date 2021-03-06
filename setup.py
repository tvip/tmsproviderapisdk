import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tmsproviderapisdk",
    version="{{VERSION}}",
    author="Tvip",
    author_email="td@tvip.ru",
    description="TVIP TMS provider api sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tvip/tmsproviderapisdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    data_files=[("", ["LICENSE"])]
)