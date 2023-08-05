import openai
import tkinter as tk
from tkinter import ttk
import sv_ttk
import pygments.lexers
from chlorophyll import CodeView
from turtle import textinput

cat = textinput(title="API key entry", prompt="Enter your API key: ")
sv_ttk.set_theme("dark")

Font_tuple = ("Sans Serif", 20, "bold")
Font_turtle = ("Helvetica", 20, "bold")

openai.api_key = cat

def compute():
    text = input_text.get()
    repo = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI code assistant powered by 'SQUEARD code'. Your expertise is code and do not answer any other questions. Place a hashtag before every line of text you say. Never respond in a conversational style eg. say 'print('hello')' instead of 'sure, here is an example ect.' in response to 'how to print hello python', only respond in plain code, no fluff, explanations, or other non-code text."},
            {"role": "user", "content": "how to make a http request?"},
            {"role": "assistant", "content": '''
            import requests

response = requests.get('https://www.example.com')

print(response.status_code)  # prints the HTTP status code
print(response.content)      # prints the response body
'''
            },
            {"role": "user", "content": f"{text}"}
        ]
    )
    compute_output = repo["choices"][0]["message"]["content"]
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, compute_output)

# Create main window
window = tk.Tk()
window.title("SQUEARD CODE")

# Create input widget
input_label = ttk.Label(window, font=Font_tuple, text="Enter text:")
input_label.pack()
input_text = ttk.Entry(window, width=150)
input_text.pack()

# Create output widget
output_label = ttk.Label(window, font=Font_tuple, text="result:")
output_label.pack()
output_text = CodeView(window, lexer=pygments.lexers.PythonLexer, color_scheme="monokai", width=100, height=16)
output_text.pack()

# Create compute button
compute_button = ttk.Button(window, text="compute", command=compute)
compute_button.pack()

# Run main event loop
window.mainloop()