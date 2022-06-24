import sys

with open("somebinary", mode="rb") as file:
    e = file.read()
    sys.stdout.buffer.write(e)
    sys.stderr.write("error: there is no error")