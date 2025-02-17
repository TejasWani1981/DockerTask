from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
   return "Hello, welcome to Flask Server by TejasWani for docker task!Changes done for pull request"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
