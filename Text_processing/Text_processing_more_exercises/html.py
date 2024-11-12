print(f"<h1>\n    {input()}\n</h1>")
print(f"<article>\n    {input()}\n</article>")
comment = input()

while comment != "end of comments":
    print(f"<div>\n    {comment}\n</div>")
    comment = input()