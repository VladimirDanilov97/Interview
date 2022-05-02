from stack import Stack

def is_brackets_balanced(brackets: str) -> str:
    stack = Stack()
    opens = "([{"
    closers = ")]}"

    index = 0
    balanced = True

    while index < len(brackets) and balanced:
        s = brackets[index]
        if s in opens:
            stack.push(s)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack_top = stack.pop()
                if opens.index(stack_top) != closers.index(s):
                    balanced = False
        index += 1
   
    if balanced and stack.isEmpty():
        return True
    else:
        return False


        


if __name__ == '__main__':
    s = '(((([])))'
    print(is_brackets_balanced(s))