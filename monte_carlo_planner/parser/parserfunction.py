def tokenize(expression):
    tokens = []
    token = ""
    for char in expression:
        if char == ' ':
            continue
        elif char in ['*', '/', '+', '-', ',', '(', ')']:
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
        else:
            token += char
    if token:
        tokens.append(token)
    return tokens

def parse_and_evaluate(tokens, variable_values):
    operands = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}

    for token in tokens:
        if token in variable_values:
            operands.append(variable_values[token])
        elif token in ['+', '-', '*', '/']:
            while operators and precedence[operators[-1]] >= precedence[token]:
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                if operator == '+':
                    operands.append(operand1 + operand2)
                elif operator == '-':
                    operands.append(operand1 - operand2)
                elif operator == '*':
                    operands.append(operand1 * operand2)
                elif operator == '/':
                    operands.append(operand1 / operand2)
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                if operator == '+':
                    operands.append(operand1 + operand2)
                elif operator == '-':
                    operands.append(operand1 - operand2)
                elif operator == '*':
                    operands.append(operand1 * operand2)
                elif operator == '/':
                    operands.append(operand1 / operand2)
            operators.pop()  # Remove the '(' from the stack
        elif token == ',':
            continue  # Assuming ',' is a separator, just ignore it for this case
        else:
            operands.append(float(token))

    while operators:
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        if operator == '+':
            operands.append(operand1 + operand2)
        elif operator == '-':
            operands.append(operand1 - operand2)
        elif operator == '*':
            operands.append(operand1 * operand2)
        elif operator == '/':
            operands.append(operand1 / operand2)
    
    return operands[0]  # The result should be the only element left in the operands list


def parser(expression, variable_values):
    tokens = tokenize(expression)
    result = parse_and_evaluate(tokens, variable_values)
    return result

# Example usage
expression = 'Variable1 + (Variable2 + Variable3) * Variable4 / Variable5'
variable_values = {'Variable1': 1, 'Variable2': 2, 'Variable3': 5, 'Variable4': 10, 'Variable5': 3}

# Tokenize the expression
tokens = tokenize(expression)
print("Tokens:", tokens)

# Parse and evaluate the expression
result = parse_and_evaluate(tokens, variable_values)
print("Result:", result)
