# Test the working environment and the python version

import sys
import platform

PYTHON_VERSION = f'python{platform.python_version_tuple()[0]}'


def config():
    system_version = sys.version_info.major
    print(f"{'='*60} Checking the working environment {'='*60}")
    if PYTHON_VERSION == 'python':
        required_major = 2
    elif PYTHON_VERSION == 'python3':
        required_major = 3
    else:
        raise ValueError(f"Unrecognized python interpreter: {PYTHON_VERSION}")

    if system_version != required_major:
        raise TypeError(f"This project requires Python {required_major}. But found Python {sys.version}")
    else:
        print("The development environment passes all the test ! \nThe program has started running, please do not stop"
              " it. \n")


if __name__ == '__main__':
    config()
