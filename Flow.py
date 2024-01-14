################################################################################################
## 2. Advanced Python
################################################################################################

##----------------------------------------------------------------------------------------------
## 2.1 Flow structures
##----------------------------------------------------------------------------------------------

## 2.1.1 The 'continue' keyword

values = 0
for num in lst:
    if num < 0 or num % 2: continue
    values += num

## 2.1.2 The 'break-else' pair

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        # Extra: N is prime ⟺ ∄i∈[2,int(sqrt(N))] : N%i=0
        if n % i == 0:
            print(f"{n} is not prime.")
            break
    else:
        # Activates if the 'break' hasn't
        print(f"{n} is prime.")