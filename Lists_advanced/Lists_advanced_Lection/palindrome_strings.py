strings = input().split()
palindrome = input()
list_of_palindrome = [word for word in strings if word == word[::-1]]

print(list_of_palindrome)
palindrome_count = strings.count(palindrome)

print(f'Found palindrome {palindrome_count} times')