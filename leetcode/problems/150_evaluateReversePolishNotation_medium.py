# neetcode roadmap stacks


# time and space complexity is o(n) each, which is the most efficient possible solution, but the conversions 
# in my solution are a bit hacky, and can be cleaned up more. too lazy to fix them tho. 


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # essentially postfix notation
        # yeah we did this in ATDS


        

        '''

        Use a stack

        iterate through the array, if we see a number, push onto the stack. 

        if we see an operator, pop two elements from the stack, treat them as operands and solve the 
        eqn using the currenrt operator.

        THEN PUSH THE RESULT BACK ON TO THE STACK!!!!


        '''

        from collections import deque

        validOperators = "+-*/"

        mystack = deque()

        for token in tokens: 
            if token in validOperators: 
                # pop two elements from the stack. and operate on them

                if not mystack: 
                    print("edge case, this shouldnt happen if input is valid")

                op1 = mystack.pop()
                op2 = mystack.pop() if mystack else 0 # is this a valid assumption? 
                res = None

                if token == "+":
                    res = float(op2) + float(op1)

                if token =="-": 
                    res = float(op2) - float(op1)

                if token =="*":
                    res = float(op1) * float(op2)

                if token =="/": 
                    res = int(float(op2) / float(op1))

                if res != None: 
                    mystack.append(res)

            else: 
                mystack.append(token)

        
        if mystack: 
             return int(mystack.pop())

        return None

