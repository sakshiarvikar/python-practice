class calculator:
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2= num2
    def addition(self):
         result = self.num1 + self.num2
         print(f"{self.num1} + {self.num2} = {result}")
        
        
    def substraction(self,num1, num2):
         print(f"{num1 } - {num2} =",(num1-num2))


    def multiply(self):
         result = self.num1 * self.num2
         print(f"{self.num1} * {self.num2} = {result}")
         
    def divide(self):
         result = self.num1 / self.num2
         print(f"{self.num1} / {self.num2} = {result}")

class scalculator:
      def __init__(self , a):
        self.a= a
        

      def square(self):
         result = self.a * self.a
         print(f"{self.a} * {self.a} = {result}")       

cal = calculator(2 , 4)
cal.addition()
cal.divide()
cal.multiply()  
cal.substraction(5,6)

scal = scalculator(5)
scal.square()
       
            
    
    
                
                




