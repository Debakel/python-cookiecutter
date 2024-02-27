import sys

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import fib

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 0

    result = fib(n)

    print(f"fib({n}) = {result}")
