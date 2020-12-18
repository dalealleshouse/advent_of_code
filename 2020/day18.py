from math import prod

# This is particularly ugly, but I'm pressed for time today. Perhaps I'll go
# back and clean it up later...

PATH = 'day18_input.txt'

OPERATORS = {
    '+': lambda stack, value: stack.append(stack.pop() + value),
    '*': lambda stack, value: stack.append(stack.pop() * value),
    '(': lambda stack, value: stack.append(value)
}

PRED_OPERATORS = {
    '+': lambda stack, value: stack.append(stack.pop() + value),
    '*': lambda stack, value: stack.append(value),
}


def precedence_evaluator(raw: str):
    value_stack = []
    op_stack = []
    raw_n = len(raw)
    cur = 0

    def process_value(value):
        if len(op_stack) == 0:
            value_stack.append(value)
        else:
            PRED_OPERATORS[op_stack.pop()](value_stack, value)

    while cur < raw_n:
        token = raw[cur]
        cur += 1

        if token.isnumeric():
            process_value(int(token))
            continue

        if token == '(':
            result, proc_count = precedence_evaluator(raw[cur:])
            process_value(result)
            cur += proc_count
            continue

        if token == ')':
            if len(op_stack) > 0:
                PRED_OPERATORS[op_stack.pop()](value_stack, value_stack.pop())

            return prod(value_stack), cur

        if token in OPERATORS:
            op_stack.append(token)

    return prod(value_stack), cur


def simple_evaluator(raw: str):
    value_stack = []
    op_stack = []

    for token in raw:
        if token.isnumeric():
            if len(op_stack) == 0:
                value_stack.append(int(token))
            else:
                OPERATORS[op_stack.pop()](value_stack, int(token))

            continue

        if token == ')':
            if len(op_stack) > 0:
                OPERATORS[op_stack.pop()](value_stack, value_stack.pop())

        if token in OPERATORS:
            op_stack.append(token)
            continue

    return value_stack.pop()


def parse_file(path, evaluator):
    with open(path) as file_handle:
        for line in (line.rstrip() for line in file_handle):
            yield evaluator(line)


def main():
    simple_sum = sum(x for x in parse_file(PATH, simple_evaluator))
    print(f'Sum using left to right evaluator = {simple_sum}')
    assert simple_sum == 12918250417632
    # 12918250417632

    simple_sum = sum(x[0] for x in parse_file(PATH, precedence_evaluator))
    print(f'Sum using precedence evaluator = {simple_sum}')
    assert simple_sum == 171259538712010
    # 171259538712010


if __name__ == '__main__':
    main()
