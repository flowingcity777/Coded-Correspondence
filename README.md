# Coded Correspondence

A Python project that implements two classic cryptographic algorithms:

- Caesar Cipher
- Vigenère Cipher

This project was created as part of my Python learning journey. It demonstrates how to encrypt and decrypt messages while practicing fundamental Python programming concepts such as functions, loops, conditionals, modular arithmetic, and string manipulation.

---

## Features

### Caesar Cipher

- Encrypt messages using any shift value
- Decrypt encrypted messages
- Preserves:
  - Uppercase letters
  - Lowercase letters
  - Spaces
  - Punctuation
  - Numbers

### Vigenère Cipher

Supports both:

- Standard Vigenère Cipher
- Codecademy's reverse Vigenère implementation

The reverse implementation uses:

Encryption:
```
cipher = plaintext - keyword
```

Decryption:
```
plaintext = cipher + keyword
```

---

## Project Structure

```
coded_correspondence.py

├── Caesar Cipher
├── Vigenère Cipher
├── Sample Messages
└── Test Cases
```

---

## Example

### Caesar Cipher

```python
print(caesar_cipher(secret_message, 7, decrypt=True))
```

### Vigenère Cipher

```python
decoded = vigenere_cipher(
    vigenere_message,
    "friends",
    encrypt=False,
    reverse=True
)

print(decoded)
```

---

## Skills Practiced

This project helped reinforce:

- Python functions
- Parameters and return values
- Boolean flags
- String manipulation
- Character encoding with `ord()` and `chr()`
- Modular arithmetic (`%`)
- Loops
- Conditional statements
- Clean code organization
- Writing reusable functions

---

## Future Improvements

Possible enhancements include:

- Command-line interface (CLI)
- User input for custom messages
- File encryption/decryption
- Graphical user interface (GUI)
- Support for additional classical ciphers
- Automated unit tests using `pytest`

---

## Technologies

- Python 3

---

## Acknowledgments

This project was inspired by the **Codecademy Coded Correspondence** project and expanded with additional functionality, code organization improvements, and support for multiple Vigenère cipher variants.


## What I Learned

While building this project, I gained hands-on experience with:

- Designing reusable Python functions
- Refactoring duplicate code into cleaner implementations
- Organizing code into logical sections
- Using modular arithmetic for encryption algorithms
- Working with ASCII values using `ord()` and `chr()`
- Implementing both Caesar and Vigenère ciphers
- Applying Python best practices to improve readability and maintainability
