numbers = open("filename.txt").read().split()
print(max([int(i) for i in numbers]))
