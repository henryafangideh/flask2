from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return ('Welcome to Flask')

@app.route('/calc', methods = ["GET"])
def math_opp():
    operation = request.json["operation"] #requesting from postman JSON
    number1 = request.json["number1"]
    number2 = request.json["number2"]
    
    if operation == 'add':
        result = int(number1)+int(number2)
    elif operation == 'multiply':
        result = int(number1)*int(number2)
    elif operation == 'division':
        result = int(number1)/int(number2) 
    else:
        result = int(number1)-int(number2)
    
    return  "The operation is {} and the result is {}".format(operation, result)

print(__name__)

if __name__ == '__main__':
    app.run()