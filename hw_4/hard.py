import codecs
import time
from datetime import datetime
from multiprocessing import Queue, Process


def process_a(main_to_a, a_to_b):
    while True:
        a_to_b.put(main_to_a.get().lower())
        time.sleep(5)


def process_b(a_to_b, b_to_main):
    while True:
        b_to_main.put(codecs.encode(a_to_b.get(), "rot_13"))


if __name__ == '__main__':
    with open("artifacts/hard.txt", "w") as file:
        main_to_a = Queue()
        a_to_b = Queue()
        b_to_main = Queue()

        Process(target=process_a, args=(main_to_a, a_to_b), daemon=True).start()
        Process(target=process_a, args=(a_to_b, b_to_main), daemon=True).start()

        messages = []

        while True:
            in_str = "Time is " + datetime.now().strftime("%H:%M:%S") + ", In: "
            message = input(in_str)
            messages.append(in_str + message)
            if message == "exit":
                messages.append("Terminated!!!")
                break
            while not b_to_main.empty():
                out_str = "Time is " + datetime.now().strftime("%H:%M:%S") + \
                         ", Out: " + b_to_main.get()
                print(out_str)
                messages.append(out_str)
            main_to_a.put(message)
        file.write("\n".join(messages))
