from tkinter import *
from main import *

window = Tk()
window.title("Chatbot")
window.geometry("820x540")



input_field = Entry(window, width=70)
output_field = Text(window, width=100)



def handle_input():
    user_input = input_field.get()
    chatbot_response =response(user_input)
    # Pass user_input to your chatbot implementation and get the chatbot's response
    # chatbot_response = "Hello, I am a chatbot"
    output_field.insert(END, f"You: {user_input}\n")
    output_field.insert(END, f"Chatbot: {chatbot_response}\n")
    input_field.delete(0, END)
    
    
button = Button(window, text="Send", command=handle_input)

input_field.grid(row=0, column=0)
button.grid(row=0, column=1)
output_field.grid(row=1, column=0, columnspan=2)
window.mainloop()