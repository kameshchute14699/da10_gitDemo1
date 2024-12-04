class firstClass:

    def __init__(self,a,b,c,d,e):
       print ('this is constructor')
       self.val1 = a
       self.val2 = b
       self.val3 = c
       self.val4 = d
       self.val5 = e
        
    
    def addValue(self):
        print(f'Addition: ',self.val1+self.val2+self.val3+self.val4+self.val5)
        
    def subValue(self):
        print(f'substract = {self.val1 - self.val2 - self.val3 - self.val4 - self.val5}')

    def mulValue(self):
        print(f'multiply = {self.val1 * self.val2 * self.val3 * self.val4 * self.val5}')

    def divValue(self):
        print(f'division = {self.val1 / self.val2 / self.val3 / self.val4 / self.val5}')

    def modValue(self):
        print(f'modulus = {self.val1 // self.val2 // self.val3 // self.val4 // self.val5}')

    def minValue(self):
       print( f'minimum = {min(self.val1 , self.val2 , self.val3 , self.val4 , self.val5)}')
   
    def maxValue(self):
        print(f'maximum = {max(self.val1 , self.val2 , self.val3 , self.val4 , self.val5)}')

    def meanValue(self):
        print(f'mean = {(self.val1 + self.val2 + self.val3 + self.val4 + self.val5) / (5) }')

    def modeValue(self):
        values = [self.val1, self.val2, self.val3, self.val4, self.val5]
        mode_value = max(set(values), key=values.count)
        print(f'Mode = {mode_value}')

    def medianValue(self):
        values = [self.val1, self.val2, self.val3, self.val4, self.val5]
        values.sort()  
        median_value = values[2]
        print(f'Median = {median_value}')

    def per_75_50_25(self):
        print(f'75_percent_add = {(75*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}')
        print(f'50_percent_add = {(50*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}')
        print(f'25_percent_add = {(25*(self.val1 + self.val2 + self.val3 + self.val4 + self.val5))/100}\n')
        
        print(f'75_percent_sub = {(75*(self.val1 - self.val2 - self.val3 - self.val4 - self.val5))/100}')
        print(f'50_percent_sub = {(50*(self.val1 - self.val2 - self.val3 - self.val4 - self.val5))/100}')
        print(f'25_percent_sub = {(25*(self.val1 - self.val2 - self.val3 - self.val4 - self.val5))/100}\n')
        
        print(f'75_percent_mul = {(75*(self.val1 * self.val2 * self.val3 * self.val4 * self.val5))/100}')
        print(f'50_percent_mul = {(50*(self.val1 * self.val2 * self.val3 * self.val4 * self.val5))/100}')
        print(f'25_percent_mul = {(25*(self.val1 * self.val2 * self.val3 * self.val4 * self.val5))/100}\n')
        
        print(f'75_percent_div = {(75*(self.val1 / self.val2 / self.val3 / self.val4 / self.val5))/100}')
        print(f'50_percent_div = {(50*(self.val1 / self.val2 / self.val3 / self.val4 / self.val5))/100}')
        print(f'25_percent_div = {(25*(self.val1 / self.val2 / self.val3 / self.val4 / self.val5))/100}\n')
        
        print(f'75_percent_mod = {(75*(self.val1 % self.val2 % self.val3 % self.val4 % self.val5))/100}')
        print(f'50_percent_mod = {(50*(self.val1 % self.val2 % self.val3 % self.val4 % self.val5))/100}')
        print(f'25_percent_mod = {(25*(self.val1 % self.val2 % self.val3 % self.val4 % self.val5))/100}')


f1 = firstClass(2 , 3 , 4 , 5 , 6 )

print('f1.val1 = ',f1.val1)
print('f1.val2 = ',f1.val2)
print('f1.val3 = ',f1.val3)
print('f1.val4 = ',f1.val4)
print('f1.val5 = ',f1.val5)

f1.addValue()
f1.subValue()
f1.mulValue()
f1.divValue()
f1.modValue()
f1.meanValue()
f1.modeValue()
f1.medianValue()
f1.maxValue()
f1.minValue()
f1.per_75_50_25()