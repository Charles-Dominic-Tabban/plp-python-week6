# PLP Python Week 6 - Error Handling

## Files

* `safe_tools.py` - Contains three functions that safely handle division by zero, invalid numbers, and missing dictionary fields.

* `unbreakable.py` - Demonstrates safe error handling so the program can continue running instead of crashing.

* `README.md` - Describes the files and explains the use of error handling.

## Why can the `if` check not catch `abc` on its own?

An `if` statement can check a condition, but `int("abc")` raises a `ValueError` when Python tries to convert the text. The conversion must be handled with `try` and `except` so the program can catch the exception and continue running.