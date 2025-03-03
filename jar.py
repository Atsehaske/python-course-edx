import emoji

def main():
    ''' main function '''
    jar = Jar()
    jar.deposit(4)
    print(str(jar))
    jar.withdraw(2)
    print(str(jar))

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ''
        for i in range (self.size):
            cookies +=emoji.emojize(':cookie:',language='alias')
        return cookies

    def deposit(self, n):
        if self.size+n <= self.capacity:
            self.size = self.size+n
        else:
            raise ValueError("Not enough capacity")

    def withdraw(self, n):
        if self.size-n >= 0:
            self.size = self.size-n
        else:
            raise ValueError("Not enough cookies")

    ''' properties '''
    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

    ''' setters '''
    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Invalid size")
        self._size = size

if __name__=="__main__":
    main()
