#!/usr/bin/env python3
# This line tells the system that this script should be run using the Python 3 interpreter.

from flask import Flask
# Import the Flask class from the flask module. Flask is a micro web framework written in Python.

app = Flask(__name__)
# Create an instance of the Flask class. This instance will be our WSGI application.

@app.route('/')
# Define a route for the home page. The route decorator binds the URL '/' to the index function.
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
    # The index function returns a string that will be displayed as HTML. 
    # In this case, it returns a header with the title of the application.

@app.route('/print/<parameter>')
# Define a route that accepts a dynamic parameter in the URL. The <parameter> part is a variable section.
def print_string(parameter):
    print(f'{parameter}')
    # Print the parameter to the console. Useful for debugging or logging.
    return f'{parameter}'
    # Return the parameter as a plain text response in the web browser.

@app.route('/count/<int:parameter>')
# Define a route that accepts an integer parameter in the URL.
def count(parameter):
    count = f''
    # Initialize an empty string to hold the count result.
    for x in range(parameter):
        count += f'{x}\n'
        # Loop from 0 to the value of parameter, appending each number followed by a newline to the count string.
    
    return f'{count}'
    # Return the count string as a plain text response in the web browser.

@app.route('/math/<num1>/<operation>/<num2>')
# Define a route that accepts two numbers and an operation in the URL.
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    # Convert the num1 and num2 parameters to integers for mathematical operations.

    if operation == '+':
        return f'{num1 + num2}'
    # If the operation is '+', return the sum of num1 and num2.
    elif operation == '-':
        return f'{num1 - num2}'
    # If the operation is '-', return the difference between num1 and num2.
    elif operation == '*':
        return f'{num1 * num2}'
    # If the operation is '*', return the product of num1 and num2.
    elif operation == 'div':
        return f'{num1 / num2}'
    # If the operation is 'div', return the division of num1 by num2.
    elif operation == '%':
        return f'{num1 % num2}'
    # If the operation is '%', return the modulus of num1 and num2.

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    # Run the application on port 5555 in debug mode. Debug mode will restart the server automatically when code changes are detected.
