import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='platelets',  
    version='0.2',
    scripts=['python3/platelets'] ,
    author="Adam Jordan",
    author_email="adamyordan@gmail.com",
    description="Supply your daily platelets intake directly from terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamyordan/platelets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
