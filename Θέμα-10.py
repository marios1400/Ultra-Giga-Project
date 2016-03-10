import hashlib
import mmh3

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in xrange(self.hash_count):
            result =int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
            self.bit_array[result] = 1

    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "Wrong"
            return "Maybe"


BF = BloomFilter(500000, 7)

lines = open("Users/MARIOS/Dekstop/dict.txt").read().splitlines()
for line in lines:
    BF.add(line)

d = open("Users/MARIOS/Dekstop/patata.txt","r")
newtext = d.read().replace(' \n ', ' ').split()

for i in newtext:
    print (i, BF.lookup(i).split())
