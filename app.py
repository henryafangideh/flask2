from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return ('Welcome to Flask')

@app.route('/calc', methods = ["GET"])
def math_opp():
    number1 = request.json("number1")
    number2 = request.json("number2")
    operation = request.json("operation") #requesting from postman JSON

    if operation == 'add':
        result = number1 + number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'division':
        result = number1/number2 
    else:
        result = number1 - number2
    
    return  result

print(__name__)

if __name__ == '__main__':
    app.run()