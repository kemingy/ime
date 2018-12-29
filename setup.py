import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    reqs = [lib for lib in f.read().splitlines() if lib]

setuptools.setup(
    name="ime",
    version="0.0.1",
    author="Keming Yang",
    author_email="kemingy94@gmail.com",
    description="Yet another Chinese input method engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kemingy/ime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs
)
