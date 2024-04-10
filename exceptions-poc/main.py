#!/usr/bin/python

class HttpException(Exception):
    def __init__(self, message=None, status_code=None, response_body=None):
        super(HttpException, self).__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_body = response_body


def raise_http_error():
    raise HttpException("Http Exception Error", 404, {"error": "Not Found"})


def raise_error():
    raise Exception("Common Exception Error")


def catcher(func):
    try:
        func()
    except Exception as e:
        print("Caught Exception", e)


def http_catcher(func):
    try:
        func()
    except HttpException as e:
        print("Caught HttpException", e.message, "Status Code:", e.status_code, "Response Body:", e.response_body)
    except Exception as e:
        print("Caught Exception", e)


def main():
    catcher(raise_error)
    catcher(raise_http_error)
    http_catcher(raise_http_error)
    http_catcher(raise_error)


main()