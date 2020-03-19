def codechef(f_arr,p_arr):
    #cook your dish here
    dic = dict()
    zippy = list(zip(f_arr,p_arr))
    for f,p in zippy:
        if f in dic:
            dic[f]+=p
        else:
            dic[f]=p
    return min(dic.values())
    
    
    
    

if __name__ == "__main__":
    t = int(input())
    while t>0:
        n,m = list(map(int,input().split()))
        f_arr = list(map(int,input().split()))
        p_arr = list(map(int,input().split()))
        print(codechef(f_arr,p_arr))
        t = t-1
    
    
                
            
        
    
    # arr.remove(suma)
    # arr.remove(suma)
    
    
    
    