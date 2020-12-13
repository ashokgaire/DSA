'''
Algorithm 
1. Scan the infix expression from left to right. 
2. If the scanned character is an operand, output it. 
3. Else, 
      1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty           or the stack contains a ‘(‘ ), push it. 
      2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.) 
4. If the scanned character is an ‘(‘, push it to the stack. 
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis. 
6. Repeat steps 2-6 until infix expression is scanned. 
7. Print the output 
8. Pop and output from the stack until it is not empty.
'''

class Conversion:
      def __init__(self, capacity):
            self.top = -1
            self.capacity = capacity
            self.array = [] 
            self.output = []
            self.precendence = {'+':1,'-':1, '*':2, '/':2, '^':3}
      
      def isEmpty(self):
            return True if self.top == -1 else False
      
      def peek(self):
            return self.array[-1]
      
      def pop(self):
            if not self.isEmpty():
                  self.top -=1
                  return self.array.pop()
            else:
                  return "$"
      def push(self, op):
            self.top +=1
            self.array.append(op)
      
      def isOperand(self,ch):
            return ch.isalpha()
      
      def notGreater(self, i):
            try:
                  a = self.precendence[i]
                  b = self.precendence[self.peek()]
                  return True if a <= b else False
            except KeyError:
                  return False

      def infixToPostfix(self, exp):

            #iterate over the expression for conversion
            for i in exp:
                  if self.isOperand(i):
                        self.output.append(i)
                  
                  elif i == '(':
                        self.push(i)
                  
                  elif i == ')':
                        while( (not self.isEmpty()) and
                        self.peek() != '('):
                              a = self.pop()
                              self.output.append(a)

                        if (not self.isEmpty() and self.peek() != '('):
                              return -1
                        else: 
                              self.pop() 
  
                  # An operator is encountered 
                  else: 
                        while(not self.isEmpty() and self.notGreater(i)): 
                              self.output.append(self.pop()) 
                        self.push(i) 
      
            # pop all the operator from the stack 
            while not self.isEmpty(): 
                  self.output.append(self.pop()) 
      
            print("".join(self.output)) 
  
# Driver program to test above function 
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp)) 
obj.infixToPostfix(exp) 
            
