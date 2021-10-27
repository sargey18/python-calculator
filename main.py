# 1 
class Calculator:
    
    #2 
    def __init__(self, number_1, number_2):
        #3 
        self.number_1 = number_1
        self.number_2 = number_2
    
    #4 
    def add(self):
        return self.number_1 + self.number_2
    
    #7 
    def minus(self):
        return self.number_1 - self.number_2
    
    #8
    def times(self):
        return self.number_1 * self.number_2
    
    # 9 
    def divide(self):
        return self.number_1 / self.number_2
    
    # 10
    def decision(self, user_decision):
        #11
        if user_decision == '+':
            return self.add()
        #12 
        elif user_decision == '-':
            return self.minus()
        #13 
        elif user_decision == '*':
            return self.times()
        #14 
        elif user_decision == '/':
            return self.divide()
# 24      
while True:
    #16     
    user_input = input("please type in your calculation: ")
    #17
    user_input = user_input.strip().split(" ")
    # 18
    #print(user_input)


    #19
    user_number_1 = int(user_input[0])
    #20
    user_number_2 = int(user_input[2])
    #21
    decision = user_input[1]


            
    # 5               #22      #23
    calc = Calculator(user_number_1, user_number_2)
    # 6
    #15
    result = calc.decision(decision)
    #print(result)

    print(result)
    #25
    further_calculations = input("Do you want to make any further calculations: ")
    #26
    if further_calculations.lower()[0] == 'y':
        continue
    else:
        break