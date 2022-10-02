import sys
import clipboard
import json


def main():
    data = clipboard.paste()
    print(data)
    print(sys.argv)


if __name__ == '__main__':
    main()
