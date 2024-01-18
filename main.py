class EvenNumbers:

    def __init__(self, n, start=0, end=1):
        self.i = 0
        self.a = start
        self.b = end
        self.n = n

    def __iter__(self):
        self.i = self.i
        self.a, self.b = self.a, self.b
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration
            self.a, self.b = self.b, self.a + self.b
        return self.a


evenNum = EvenNumbers(n=10)
for i in evenNum:
    print(i)

evenNum2 = EvenNumbers(start=10, end=25, n=10)
listNum = list(map(int, evenNum2))
print(listNum)
