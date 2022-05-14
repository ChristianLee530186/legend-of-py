from src import *

def main():
    while True:
        map = os.path.abspath('maps/debug.py')
        startUp(map)

        while True:
            timer.start()

            update(getInputs())

            render()

            timer.delay(60)

if __name__ == '__main__':
    main()
