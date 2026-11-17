import threading

class HiloNo(threading.Thread):
    def run(self):
        for i in range(30):
            print("NO ", end="")

if __name__ == "__main__":
    print("INICIO")

    t = HiloNo()
    t.start()

    for i in range(30):
        print("YES ", end="")

    t.join()