from gui import PyGuiAutomation
import random

def main():
    # TODO finish
    auto = PyGuiAutomation()
    print("Press CTRL + C to interrupt the program!!!")
    try:
        while True:
            random_x = random.randint(0, auto.width)
            random_y = random.randint(0, auto.height)
            auto.moveTo(random_x, random_y, 0.2)
    except KeyboardInterrupt:
        print("Done!!!")


if __name__ == '__main__':
    main()
