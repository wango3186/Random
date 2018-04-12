import time

def timer(main):
    def wrapper():
        start = time.time()
        main()
        print('awkward')
        end = time.time()
        print("Time:",(end - start)*1000,'ms')
    return wrapper

@timer
def hello():
    b = 0
    for i in range(500):
        b=b**i
    print(b)
hello()
        


nums = set([
    38199, 49602, 40691, 48958, 54383, 56420, 28952, 55293, 32501, 25900,
    65611, 10486, 29288, 22610, 62328, 56420, 6692, 5068, 51527, 45374, 48097,
    6328, 1771, 61460, 1232, 57260, 42420, 49651, 63448, 37049, 7826, 5166,
    54502, 23436, 46382, 60676, 28210, 21210, 12719, 33257, 57645, 67431,
    22232, 13013, 27041, 36218, 8666, 9856, 17458, 42182
])
start = time.time()

multiples = set()
primes = set()
for i in range(2, 70000):

  if i not in multiples:
	  primes.add(i)
	  for j in range(i * i, 70000, i):
		  multiples.add(j)
end = time.time()
print("Time:",(end - start)*1000,'ms')
for i in primes & nums:
	print(i)
