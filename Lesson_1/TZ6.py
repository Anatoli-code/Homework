world = input("Enter your world: ")
if len(world) == len(set(world)):
    print("Это изограмма")
else:
    print("Это не изограмма")