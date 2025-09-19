from collections import deque

def is_palindrome(word):
    d = deque(word)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Example usage
words = input("Enter lowercase words separated by ', ': ").split(', ')

for word in words:
    result = "✅ Palindrome" if is_palindrome(word) else "❌ Not a palindrome"
    print(f"{word}: {result}")
