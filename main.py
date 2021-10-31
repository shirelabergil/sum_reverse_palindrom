num=int(input("enter 4 digit positive num"))
if num>1000 or num<9999:
    print(num%10+num%100//10+num%1000//100+num%10000//1000)
    print(num%10*1000+num%100//10*100+num%1000//100*10+num%10000//1000)
    if num%10+num%100//10==num%1000//100+num%10000//1000:
        print("palindrom")
    else:
        print("no palindrom")
else:
    print("error! invalid value")
