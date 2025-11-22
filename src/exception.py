from pathlib import Path
from src.logs import logging
import sys


class CustomException(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

    def __str__(self):
        return f"CustomException: {self.args[0]}, Errors: {self.errors}"
    
    
internet_error = CustomException("This is a custom exception", errors={"code": 500, "detail": "Internal Server Error"})
logging.error(internet_error)

code_error = CustomException("This is a custom exception", errors={"code": 404, "detail": "Not Found"})
logging.error(code_error)