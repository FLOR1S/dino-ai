import random
x=2 #number of inputs & weights
weights = [0]*x #list of weights
a=int(input())
b=int(input())
inputs = [a, b] #how do I create a list with x items?
#TODO: create input list w/ x placeholders and iterate through list for user inputs?
#how to automate input?

#activation function
def sign(n):
    if n >= 0:
        return 1
    if n < 0:
        return -1

class Perceptron:
    for i in range(x):
        #assign random starting values to weights
        weights[i] = random.uniform(-1, 1)
    
#make a guess based on input and weight
    def guess(inputs):
        Sum = 0
        for i in range(x):
            Sum += inputs[i]*weights[i]
        output = sign(Sum)
        print(output)
        
    guess(inputs)
            




