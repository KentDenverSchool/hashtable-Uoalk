#Grant
#10/3/18
#The purpose of this lab is to create a hashtable


"""
Lab challenge #1:
A large prime number would be better because if there are any patterns in the
stored data a number with more factors is more likely to create collisions.
let m be a factor of n and let x be any positive integer. x*m % n will be 
limitid to multiples of m. So minimizing the number of
possibilities for m by choosing a number with less factors limits collisions.


Lab challenge #2:
This would be a bad hash function because char values summed would frequently
return the same value before the modulo operator is even used.
for example let f(x) be that hash functions:
f("ab")=f("ba")
f("ad")=f("bc")
f("abcdefg")=f("gefdcba")

There are many collisions when the inputs are similar




Lab challenge #3:
First it returns 0 if the object is null
otherwise it uses the object.hashCode() function then xor's it with the
object.hashCode() shifted over 16 bits

object.hashCode is a native method, so it's likely implemented in c and will
return a unique int for every unique object
"""

class HashTable:
    def __init__(self, capacity):

        self.dict=[None]*capacity
    def hashCode(self,key):
        sum=0;
        for i in range(len(key)):
            sum+=ord(key[i])*pow(2,i)
        return sum%len(self.dict)
    def put(self,key,value):
        h=self.hashCode(key)
        if(self.dict[h]==None):
            self.dict[h]=value;
        else:
            raise RuntimeError;
    def get(self,key):
        return self.dict[self.hashCode(key)]

h=HashTable(10)
h.put("a","a")
h.put("b","b")
h.put("c","c")
h.put("d","d")
h.put("eeee","hi")
h.put("key3","val")
try:
    h.put("a","hi")
except:
    print("succesfully failed")
print(h.get("a"))
print(h.get("eeee"))
print(h.get("not defined"))


import random,math
class HashCodeAnalyzer:
    def __init__(self):
        self.capacity=100;
        self.attempts=100000;
    def hashCode(self,key):
        sum=0;
        for i in range(len(key)):
            sum+=ord(key[i])*pow(2,i)
        return sum%self.capacity
    def genRandomKey(self):
        key=""
        for i in range(random.randint(10,20)):
            key+=random.choice("abcdefghijklmnopqrstuvwxyz")

        return key
    def analyze(self):
        outputs=[0]*self.capacity
        for i in range(self.attempts):
            outputs[self.hashCode(self.genRandomKey())]+=1;
        average=sum(outputs)/self.capacity


        rSquaredSum=0
        for i in range(self.capacity):
            rSquaredSum+=pow(average-outputs[i],2)

        rmse=math.sqrt(rSquaredSum/len(outputs))
        print("Average: "+str(average))
        print("RMSE:"+str(rmse))
        print("RMSE percent of average: "+str(rmse/average*100)+"%")
        valueRange=max(outputs)-min(outputs)
        print("range:"+str(valueRange))
        print("range percent of average: "+str(valueRange/average*100)+"%")
        print(outputs)

a=HashCodeAnalyzer()
a.analyze()
