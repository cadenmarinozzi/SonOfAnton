"""
Different methods for receiving inputs for queries
"""

from IO.tts import speak

# Input

def textInput(head):
    return input(f'{head}: ');

def inp():
    query = textInput('Query');

    return query;

# Output

def textOutput(head, text):
    print(f'{head}: {text}');

def voiceOutput(text):
    speak(text);

def out(text):
    textOutput('Response', text);
    voiceOutput(text);