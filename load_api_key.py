
import os
import sys

def main():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'API_key.secret')) as f:
        key = f.readline()
        os.environ["QXToken"] = key
    return

if __name__ == '__main__':
    main()