from pathlib import Path

path = Path("ecomerce")
print(path.exists())

path = Path("email")
#print(path.mkdir())
print(path.rmdir())

for file in path.glob('*.py'):
    print(file)