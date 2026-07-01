
import datetime


# Chatbot Memory
user_memory = {}


# Knowledge Base

responses = {

    "hello": "Hi 😊 Welcome! How can I help you?",

    "hi": "Hello 😊 Nice to meet you",

    "how are you": 
    "I am good 🤖 Thanks for asking. How can I help you?",

    "who are you":
    "I am your Personal AI Assistant created using Python and Flask",

    "your name":
    "You can call me AI Assistant 🤖",

    "what can you do":
    "I can answer your questions, help with Python, coding and basic information",

    "python":
    "Python is a high level programming language used in AI, web development and automation",

    "flask":
    "Flask is a lightweight Python framework used to create web applications",

    "html":
    "HTML is used to create the structure of web pages",

    "css":
    "CSS is used to design and style websites",

    "javascript":
    "JavaScript makes websites interactive",

    "react":
    "React is a JavaScript library used for building user interfaces",

    "bca":
    "BCA is a Bachelor degree related to computer applications and software development",

    "dsa":
    "DSA means Data Structures and Algorithms. It helps in problem solving",

    "ai":
    "AI means Artificial Intelligence. It enables machines to think and learn",

    "machine learning":
    "Machine Learning is a branch of AI where machines learn from data",

    "motivate me":
    "Keep learning 🚀 Every error makes you a better developer",

    "happy":
    "Great to hear that 😊 Keep smiling",

    "sad":
    "Don't worry. Keep improving and believe in yourself 💙",

    "thank you":
    "You are welcome 😊",

    "bye":
    "Goodbye 👋 Have a great day",

    "date":
    "Today is " + str(datetime.date.today()),

}


def getResponseOfBot(userQuestion):


    userQuestion = userQuestion.lower()



    # Remember Name

    if "my name is" in userQuestion:

        name = userQuestion.replace("my name is","").strip()

        user_memory["name"] = name

        return "Nice to meet you " + name + " 😊"



    # Greeting with saved name

    if "my name" in userQuestion:

        if "name" in user_memory:

            return "Your name is " + user_memory["name"]

        else:

            return "I don't know your name yet"



    # Find answer

    for key in responses:

        if key in userQuestion:

            return responses[key]



    return "Sorry 😅 I am still learning. Try asking something else."
    
