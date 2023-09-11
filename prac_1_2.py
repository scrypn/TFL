def prior(operation):
    return 1 if operation == "(" else (
        2 if operation == "+" or operation == "-" else (3 if operation == "*" or operation == "/" else 0))


formula = input()
enable_operations = ["+", "-", "*", "/", "("]
stack = []
output = []
for item in formula.split():
    if item.isalnum():
        output.append(item)
    elif item in enable_operations:
        if item == "(":
            stack.append(item)
        else:
            for stack_item in list(reversed(stack)):
                if prior(item) <= prior(stack_item):
                    output.append(stack.pop())
                else:
                    break
            stack.append(item)
    elif item == ")":
        for stack_item in list(reversed(stack)):
            if stack_item == "(":
                stack.pop()
                break
            else:
                output.append(stack.pop())

output.extend(list(reversed(stack)))
print(" ".join(output))

stack = []
if not any(c.isalpha() for c in output):
    first_elem = ""
    second_elem = ""
    for item in output:
        if item.isalnum():
            stack.append(item)
        elif item in enable_operations:
            second_elem = stack.pop()
            first_elem = stack.pop()
            stack.append(str(eval(first_elem + item + second_elem)))

    print(stack[0])
