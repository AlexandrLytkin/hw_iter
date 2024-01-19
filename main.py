class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.cont = 0

    def __iter__(self):
        self.cont = 0
        self.start, self.end = self.start, self.end
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        elif self.start % 2 == 0:
            self.cont = self.start
            self.start += 1
        self.start += 1
        return self.cont


en = EvenNumbers(start=10, end=25)
for i in en:
    print(i)
