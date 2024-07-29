import time
t = time.time()

record = []
for a in range(2,101):
    for b in range(2,101):
        x = a**b
        if x not in record:
            record.append(x)
print(len(record))
print("time taken : ",time.time()-t)