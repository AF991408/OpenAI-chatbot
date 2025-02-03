from flask import Flask, render_template, request, jsonify
import openai
openai.api_key = #insert your api key here

# Load the prompt from the file
with open('website_text.txt', 'r') as file:
    prompt = file.read()

# Define the hotel assistant template
hotel_assistant_template = prompt + """
You are the hotel manager of Landon Hotel, named "Mr. Landon".  
Your expertise is exclusively in providing information and advice about anything related to Landon Hotel.  
This includes any general Landon Hotel-related queries.  
You do not provide information outside of this scope.  
If a question is not about Landon Hotel, respond with, "I can't assist you with that, sorry!"  
Question: {question}  
Answer:
"""

def create_chat_completion(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": hotel_assistant_template},
            {"role": "user", "content": question}
        ],
        temperature=0.5,
        max_tokens=150
    )
    return response

def query_llm(question):
    response = create_chat_completion(question)
    return response.choices[0].message['content'].strip()

# Example usage
#while True:
#    question = input("Enter your question: ")
#    response = query_llm(question)
#    print(response)


app = Flask(__name__) 

@app.route("/") 
def index(): 
    return render_template("index.html") 

@app.route("/chatbot", methods=["POST"]) 
def chatbot(): 
    data = request.get_json() 
    question = data["question"] 
    response = query_llm(question) 
    return jsonify({"response": response}) 

if __name__ == "__main__": 
    app.run(debug=True)