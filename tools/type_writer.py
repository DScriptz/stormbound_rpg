import sys
import time

def type_writer(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

    print()


print("\n[----------------------------------------------------------]")
type_writer("                    -{ STORMBOUND HAVEN }-                      ")
print("\n[----------------------------------------------------------]")