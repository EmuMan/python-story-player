import time

def dprint(string):
    length = len(string)
    for i in range(length):
        if string[i] == "~":
            time.sleep(0.5)
        elif string[i] == "^":
            print("\n", end ="", flush=True)
        else:
            print(string[i], end ="", flush=True)
            time.sleep(0.015)
    return
