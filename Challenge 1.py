
def is_balanced(s: str) -> bool:
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


# Test cases
print(is_balanced("(a[b]{c})"))  # True
print(is_balanced("(])"))        # False
print(is_balanced("(("))         # False
print(is_balanced(""))           # True
