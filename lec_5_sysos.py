import sys
import os

print(os.getcwd())

os.system("echo hi!")

'os.system("python3 lec_5_sysos.py")'

print("Python version:", sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))
print(dir(os))
print(sys)