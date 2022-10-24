from utils import trace_decorator

path = r"C:\Project"
name = "file.txt"

@trace_decorator(path, name)
def summator(a, b):
    return a + b

if __name__ == '__main__':
    summator(1, 1)