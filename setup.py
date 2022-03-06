import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md","r") as fh:
    long_description=fh.read()

setuptools.setup(
    name="aqdataextractor-AD",
    version="0.0.1",
    author="Adhithya",
    author_email="adhithyasrinivasan@gmail.com",
    description="Air Quality data transformer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    license="MIT License"
)