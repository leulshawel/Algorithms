import time

a = int(input("Num1: "))
b = int(input("Num2: "))
result = 0

def sft_mul(a, b):
    k, r = 0, 0
    m = a
    while m > 1:
       m = m >> 1
       k += 1
        
    r = a - (1 << k)
    return r, b << k

s = time.time()
while a > 0:
    a, temp = sft_mul(a, b)
    result += temp
    
t = time.time() - s


print(f"result: {result}")
print("finished in: ", round(t*1000, 4), "ks")

