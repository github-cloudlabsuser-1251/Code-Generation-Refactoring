# Calculator Application

This is a simple calculator application implemented in Python. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

You can use the `Calculator` class from the `src/calculator.py` file to perform arithmetic operations. Here is a quick example:

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
```

## Running Tests

To run the unit tests for the calculator, navigate to the `tests` directory and run:

```
python -m unittest test_calculator.py
```

## License

This project is licensed under the MIT License.