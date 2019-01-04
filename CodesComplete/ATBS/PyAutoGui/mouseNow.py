""" After pressed enter, the program retrieve the position of the mouse."""

from gui import PyGuiAutomation


def main():
    print('Press Ctrl+C to quit.')
    input()
    auto = PyGuiAutomation()
    try:
        while True:
            x, y = auto.position()
            print(f"X:{x} Y:{y}")
    except KeyboardInterrupt:
        print('\nDone')



if __name__ == '__main__':
    main()
