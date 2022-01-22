"""
Different methods for receiving inputs for queries
"""

# Input

def textInput(head):
    return input(f'{head}: ');

def inp():
    query = textInput('Query');

    return query;

# Output

def out(text):
    print(text);