import os

try:
    who_am_i = os.environ['WHOAMI']
    print('Variable $WHOAMI:', who_am_i)
except KeyError:
    print('Error to get variable $WHOAMI')

os.environ["WHOAMI"] = "python-tester"
who_am_i = os.environ['WHOAMI']
print('Variable $WHOAMI:', who_am_i)

del os.environ['WHOAMI']
non_existent_variable = os.environ.get('WHOAMI')
print('Variable $WHOAMI:', non_existent_variable)

env = os.getenv('ENV', 'DEV')
print('Variable $ENV:', env)
os.environ["ENV"] = "PRD"
env = os.getenv('ENV', 'DEV')
print('Variable $ENV:', env)
