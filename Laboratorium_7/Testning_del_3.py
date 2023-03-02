
from hashtable import Hashtable
from sys import stdin

def main():
    hashtable = Hashtable(150001)

    for line in stdin:
        line = line.strip()
        key, *value = line.split()
        if key == '#':
            break
        elif len(value) != 0:
            hashtable.store(key, value[0])
        else:
            try:
                value = hashtable.search(key)
                print(value)
            except KeyError:
                print('None')


if __name__ == "__main__":
    main()