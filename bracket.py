from stack import Stack
from darray import DArray
# Bracket matching
def checkBracketSequence(input):
    assert len(input) > 0, "Please provide input string"

    stack = Stack()
    reverse = Stack()
    bracketClose = {
        '[': ']', 
        '{': '}', 
        '(': ')'
        }
    array = DArray()

    for char in input:
        if char not in bracketClose.keys() and char not in bracketClose.values():
            raise Exception('Invalid input')
        else:
            array.add(char)

    for i in range(array.length()):
        if array.get(i) in bracketClose.keys():
            stack.push(array.get(i))
            reverse.push(bracketClose[array.get(i)])
        elif array.get(i) in bracketClose.values():
            if stack.isEmpty(): 
                return False
            else:
                stack.pop()
                top = reverse.pop()
                if top != array.get(i):
                    return False
    return stack.isEmpty()
