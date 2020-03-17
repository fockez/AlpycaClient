"""Setup Alpyca for distribution."""
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="AlpycaClient",
    description="Python interface for ASCOM Alpaca with ASCOM API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fockez Zhang",
    url="",
    version="1.1.0",
    license="LICENSE.txt",
    py_modules=["alpycaclient"],
    install_requires=["requests", "python-dateutil"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: Apache Software License",
    ],
)
