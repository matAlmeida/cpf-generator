# CPF-Generator

![License](https://img.shields.io/pypi/l/cpf-generator.svg?style=flat)
![PyPI](https://img.shields.io/pypi/v/cpf-generator.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cpf-generator.svg)
[![Downloads](https://pepy.tech/badge/cpf-generator)](https://pepy.tech/project/cpf-generator)

## Installing

```sh
$ pip install cpf-generator
```

## Usage

```py
from cpf_generator import CPF

cpf = CPF.generate() # Will generate a random CPF # EX: 46064927240
formatedCpf = CPF.formater(cpf) # Will format the CPF to be printed in some place # EX: 460.649.272-40
CPF.validate(cpf) # Will return True if the CPF is valid or False if not # EX: True
CPF.validate(formatedCPF) # Works with formated CPF # EX: True
```

## by [Matheus Almeida](https://twitter.com/mat_almeida)

Work with braziian CPF easily

# MIT License
