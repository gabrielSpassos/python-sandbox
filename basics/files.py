file = open("file.txt")

print(file.readlines())

writer = open("file.txt", "a")

writer.write("\nGabriel Passos")

writer.close()
