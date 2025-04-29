import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    
    regex = r"\b(um|Um)\b"
    
    x = re.findall(regex, s)
    
    # print(x)
    # print(len(x))
    
    return len(x)


if __name__ == "__main__":
    main()
