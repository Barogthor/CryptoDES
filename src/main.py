from src.constante import *
import array

KEY = [0, 1, 0, 1, 1, 1, 1, 0,
       0, 1, 0, 1, 1, 0, 1, 1,
       0, 1, 0, 1, 0, 0, 1, 0,
       0, 1, 1, 1, 1, 1, 1, 1,
       0, 1, 0, 1, 0, 0, 0, 1,
       0, 0, 0, 1, 1, 0, 1, 0,
       1, 0, 1, 1, 1, 1, 0, 0,
       1, 0, 0, 1, 0, 0, 0, 1]


def remove_bit_control(key=None):
    if key is None:
        raise Exception("key is empty")
    new_key = []
    for i in range(0, len(key)):
        if i % 8 != 0 and i != 0:
            new_key.append(key[i])
    return new_key


def main():
    print("hello")
    print(KEY)
    print(remove_bit_control(KEY))


if __name__ == "__main__":
    main()
