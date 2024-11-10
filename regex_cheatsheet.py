# Regex Cheat Sheet
#
# ### Basic Matching
# - `.` : Matches any character except line terminators.
# - `^` : Matches the start of a string.
# - `$` : Matches the end of a string.
#
# ### Quantifiers
# - `*` : Matches 0 or more times, e.g., `a*` matches `aaa`.
# - `+` : Matches 1 or more times, e.g., `a+` matches `a` or `aaa`.
# - `?` : Matches 0 or 1 time, e.g., `a?` matches `a` or nothing.
# - `{m,n}` : Matches from m to n times, e.g., `a{2,3}` matches `aa` or `aaa`.
#
# ### Character Classes
# - `\d` : Digits `[0-9]`
# - `\D` : Non-digits `[^0-9]`
# - `\w` : Word characters `[a-zA-Z0-9_]`
# - `\s` : Whitespace `[\t\n\r ]`
#
# ### Assertions
# - `(?=A)`: Lookahead, matches if followed by A.
# - `(?!A)`: Negative lookahead, matches if NOT followed by A.
# - `(?<=A)`: Lookbehind, matches if preceded by A.
# - `(?<!A)`: Negative lookbehind, matches if NOT preceded by A.
#
# ### Groups
# - `(A)` : Captures A as a group.
# - `(?:A)` : Matches A but does not capture it.
# - `(?P<name>A)` : Names a capturing group as “name”.
#
# ### Functions
# - `re.findall()` : Finds all matches in a string.
# - `re.search()` : Searches for the first match.
# - `re.sub(A, B, C)` : Substitutes A with B in C.
#
# ### Examples
# - Basic match: `r"hello"` matches `"hello"` in text.
# - Case-insensitive search: `re.search(r"hello", text, re.IGNORECASE)`
# - Find all words: `re.findall(r"\w+", text)`
