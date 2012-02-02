## procedural programming
last = 0
second = 0 

def next_fib():
    global last
    global second

    if last == 0:
        last = 1
        return 0

    current = last
    last = second + last
    second = current
    return current

## OOP
class Fib(object):
    def __init__(self):
        self.last == 0
        self.second == 0

    def next_fib(self):
        if self.last == 0:
            self.last = 1
            return 0

        current = self.last
        self.last = self.second + self.last
        self.second = current
        return current

# import this script, then
# make it do things...
if __name__ == "__main__":
    Fib()
