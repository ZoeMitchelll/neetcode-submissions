class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+','-','/','*'} #[10,2,/,5,+] [5,5]
        for rpn in tokens:
            if rpn not in operations:
                stack.append(rpn)
            else:
                num1 = str(stack.pop())
                num2 = str(stack.pop())
                print(type(num1),type(num2), type(rpn))
                print(num1,num2,rpn)
                num3 = eval(num2+rpn+num1)
                stack.append(int(num3))
        ret = stack.pop()
        print(ret)
        return int(ret)
        #["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        #[10,6,9,3] -> [10,6,12,-11]-> [10,6,-132]-> [10,-22]->[-122,17]->[-100]