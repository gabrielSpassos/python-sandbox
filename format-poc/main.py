import uuid

id = uuid.uuid4()

test1 = "test-{}".format(id)
test2 = "test-{}".format(str(id))

if (test1 == test2):
    print("Both strings are equal")
else:
    print("Not equals")
