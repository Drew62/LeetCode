# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
#
# Return true if s is a valid string, and false otherwise.

class Node():

    def __init__(self, value: str):
        self.value = value
        self.next = None 

class Stack():

    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.top == None:
            self.top = newNode
            self.length = 1
        else:
            newNode.next = self.top
            self.top = newNode
            self.length += 1

    def pop(self):
        if self.top == None:
            return None
        else:
            node = self.top
            self.top = node.next
            self.length -= 1
            return node

    def peek(self):
        if self.top == None:
            return None
        else:
            node = self.top
            return node.value

    def iterate(self):
        node = self.top
        while node.next != None:
            print(node.value)
            node = node.next
        print(node.value)

class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0: # Every open must have a close
            return False
       
        stack = Stack()
        map = {
            "{": "}",
            "[": "]",
            "(": ")",
            None: ''
        }

        for char in s:
            if char in map.keys():
                stack.push(char)
            else:
                if char == map[stack.peek()]:
                    stack.pop()
                else:
                    return False
        if stack.length != 0: # If all opening 
            return False
        return True

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("(("))
print(solution.isValid("({])"))
print(solution.isValid("([{}])"))
