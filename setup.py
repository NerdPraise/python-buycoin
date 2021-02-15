from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = "0.0.1"
DESCRIPTION = "BUYCOINS SDK"

# Setting up
setup(
    # the name must match the folder name "verysimplemodule"
    name="verysimplemodule",
    version=VERSION,
    author="Praise Ajayi",
    author_email="praiseajayi2@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    packages=find_packages(),
    url="https://github.com/NerdPraise/python-buycoin",
    license="MIT",
    install_requires=["python-graphql-client", "requests", "python-decouple"],  # add any additional packages that
    # needs to be installed along with your package. Eg: "caer"

    keywords=["python", "SDK", "Buycoins"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.0"
)
