import _thread
from time import sleep


def test_thread():
    while True:
        input_test = input()
        print("hello")
        sleep(0.5)
        if input_test != 00000000:

second_thread = _thread.start_new_thread(test_thread, ())