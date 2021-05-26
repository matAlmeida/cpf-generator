import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cpf_generator",
    version="2.0.1",
    author="Matheus Almeida",
    author_email="mat.almeida@live.com",
    description="Generate, Validate and Format brazilian CPF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matalmeida/cpf-generator",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    license="MIT"
)
