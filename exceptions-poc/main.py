#!/usr/bin/python

class CustomException(Exception):
    def __init__(self, message=None, business_error_code=None):
        super(CustomException, self).__init__(message)
        self.message = message
        self.business_error_code = business_error_code


def raise_custom_error():
    raise CustomException("Custom Exception Error", "BUSINESS_ERROR_001")


def raise_error():
    raise Exception("Common Exception Error")


def catcher(func):
    try:
        func()
    except Exception as e:
        print("Caught Exception", e)


def custom_catcher(func):
    try:
        func()
    except CustomException as e:
        print("Caught CustomException", e.message, "Error Code:", e.business_error_code)
    except Exception as e:
        print("Caught Exception", e)


def main():
    catcher(raise_error)
    catcher(raise_custom_error)
    custom_catcher(raise_custom_error)
    custom_catcher(raise_error)


main()