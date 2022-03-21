OIL FACTORY(wipro coding qsn solution:-)
https://github.com/sudhir192311

a = int(input())
b = int(input())
l1 = []
for i in range(a, b+1):
     count = 0
if i < 0:
for j in range(i, 0):
     if i % j == 0:
          count += 1
          if count == 2:
              l1.append(i)
         break
if i > 0:
for j in range(1, i+1):
     if i % j == 0:
          count+=1
     if count == 2:
         l1.append(i)
         break
for i in range(b, a-1,-1):
       count = 0
if i < 0:
     for j in range(i, 0):
          if i % j == 0:
              count += 1
         if count == 2:
             l1.append(i)
             break
if i > 0:
       for j in range(1, i+1):
           if i % j == 0:
               count+=1
          if count == 2:
              l1.append(i)
             break
if sum(l1) < 0:
       print(-(sum(l1)))
else:
      print(sum(l1))