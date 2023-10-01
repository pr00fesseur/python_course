from kitchen import cook

# import sys
# print(sys.argv[0])

print(__name__)


def bar():
    print("I am bar from core file")


def main():
    cook()
    bar()


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module can not be imported")
