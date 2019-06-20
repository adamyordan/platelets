import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='platelets',  
    version='0.3',
    scripts=['python2/platelets'] ,
    author="Adam Jordan",
    author_email="adamyordan@gmail.com",
    description="Supply your daily platelets intake directly from terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamyordan/platelets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
