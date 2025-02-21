p=17
q=23
e=5
P="Oanh"
P=P.lower()
n=p*q
for i in P:
    a=ord(i)-96
    print(i," ",a**e%n)
