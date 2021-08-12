import timeit

start = timeit.default_timer()


nterms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print(f"Fibonacci sequence up to {nterms}:")
   print(n1)
else:
    print(f"Prime Fibonacci sequence:")
    while count < nterms:
        if nterms > 1:
            # Prints only the prime numbers of the Fibonacci sequence
            for i in range(2, n1):
                if (n1 % i) == 0:
                    break
            else:
                print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


stop = timeit.default_timer()

print("Time: ", stop - start)  