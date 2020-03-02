# cook your dish here
def fun(n,k,protein_buy):
    total_protein = 0
    for i in range(n):
        total_protein += protein_buy[i]
        total_protein -= k
        if total_protein < 0:
            print("NO "+str(i+1))
            return
    print("YES")

a = int(input())
while a>0:
    n,k = map(int,input().split())
    protein_buy = [int(i) for i in input().split()]
    fun(n,k,protein_buy)
    a = a-1        
        