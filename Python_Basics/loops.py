count=1
totalsum=0

while(count<=5):
    totalsum+=count
    print(f"Iteration {count}: Current Total = {totalsum}")
    count+=1

print("Loop finished Final sum is ", totalsum)

a=1
for r in range(1, 5, 2):
    a=a*r
    print(a)