import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strut",
    version="1.0.1",
    author="trevor grayson",
    author_email="trevor@ipsumllc.com",
    description="Define HTTP APIs easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevorgrayson/strut",
    scripts=['strut', 'strut-server'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
    ],
)
