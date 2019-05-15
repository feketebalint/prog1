import ast

def elemzo(file):
    with open(file) as f:
        lines = f.read()
    try:
        ast.parse(lines)
        return True
    except SyntaxError:
        return False
print(elemzo(input("File: ")))