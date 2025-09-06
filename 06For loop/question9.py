n = int(input("Enter a number: "))
sum_factors = 0

for i in range(1, n):
    if n % i == 0:
        sum_factors += i

if sum_factors == n:
    print(n, "is a Perfect Number")
    
else:
    print(n, "is NOT a Perfect Number")
