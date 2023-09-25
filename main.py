from flask import Flask, render_template, request
from certiGen import createCertificate as CGI
# the line above will import the function that generates certificate
'''
Note for Args:
when the user enters the details in the form(which has not been made yet), a certificate 
will be generated and stored in the folder named likewise. 

Implement this in flask and also the NFT part required.
'''

app = Flask(__name__)

@app.route("/")
def render():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port = 8000)
