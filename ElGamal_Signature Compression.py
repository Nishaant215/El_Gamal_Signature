#Nishaant Goswamy


import collections
from CompressDecompress import Text_Encoding,Letter_Decoding
import cryptAlg as crypt


print("This is ElGamal Signature")
p = int(input("Enter a prime value p: "))

if not crypt.primeCheck(p): quit()

g = crypt.Generator((p-1), p)
print("Generator g:", g )

r = int(input("Select secret key int r: "))

K = crypt.Square_And_Multiply(g,r,p)
print("K value K=(g**r)%p:", K)

R = crypt.Coprime(p-1)
print("R value GCD(R,p-1)=1:", R)

X = crypt.Square_And_Multiply(g,R, p)
print("X value X=(g**R)%p:", X)


M = (input("Enter the message string: ")).lower()
MsgNumList= Text_Encoding(M)

A1_List = []
A2_List = []

for M in MsgNumList:
    M = int(M)
    print("Msg Num (M):", M)

    inv_R = crypt.Inverse_Mod(R,p-1)
    print("inverse mod (R^-1(mod p)):", inv_R)
    Y = ((M - r*X)*inv_R)% (p-1)
    print("Signature Y = ((M - r*X)*inv_R)% (p-1)")
    print("Y value:", Y)


    print("***Verfification***")

    A1 = (crypt.Square_And_Multiply(K,X,p) * crypt.Square_And_Multiply(X,Y,p)) % p
    # A1 = ((K**X)*(X**Y))%p
    print("A1 value is:", A1)
    A1_List.append(A1)

    A2 = crypt.Square_And_Multiply(g,M, p)
    print("A2 value is:", A2, "\n")
    A2_List.append(A2)

    if A1 == A2:
        print("Success!! Signature a element of A1 and A2 match\n")


if collections.Counter(A1_List) == collections.Counter(A2_List):
    print("Success!! Signature A1 and A2 match for all elements")
    print("A1's List", A1_List)
    print("A2's List", A2_List)
    print("Encoded Message:", MsgNumList)
    verifyEncodedMsg = int(''.join([str(x) for x in MsgNumList]))
    print("Encoded Message:", verifyEncodedMsg)


