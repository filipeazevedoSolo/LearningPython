reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""

print(reply)

values= {'name':'Bob', 'age':40}

print(reply % values)

