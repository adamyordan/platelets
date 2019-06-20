import setuptools
from pip._internal.req import parse_requirements


with open("README.md", "r") as fh:
    long_description = fh.read()


def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]


setuptools.setup(
    name='platelets',  
    version='0.4',
    scripts=['platelets/platelets'] ,
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
    ],
    install_requires=load_requirements('requirements.txt'),
)
