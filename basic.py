from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/chatbot', methods=['GET'])
def chatbot():
    return "Chatbot service"

@app.route('/api/v1/chatbot/service1', methods=['GET'])
def service1():
    return "Hello, world! - Service 1"

@app.route('/api/v1/chatbot/service2', methods=['GET'])
def service2():
    return "Hello, world! - Service 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
