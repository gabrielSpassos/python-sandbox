#!/usr/bin/python

import uuid
import shortuuid
import string
import random


def random_string(length):
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return res


uuid1 = uuid.uuid1()
print(uuid1)
print(len(str(uuid1)))


uuid4 = uuid.uuid4()
print(uuid4)
print(len(str(uuid4)))


uuidHex = uuid.uuid4().hex
print(uuidHex)
print(len(str(uuidHex)))


shortuuid = shortuuid.uuid()
print(shortuuid)
print(len(str(shortuuid)))


random_string = random_string(36)
print(random_string)
print(len(str(random_string)))
