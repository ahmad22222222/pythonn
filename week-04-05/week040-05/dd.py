color = ['\033[91m','\033[92m', '\033[93m','\033[94m']
for i in range(10):
    print(color[i % 4] + "python is magic omg")

print('\033[0m') # reset color 