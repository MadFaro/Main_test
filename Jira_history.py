from flask import Flask, request
from pywebio import start_server
from pywebio.output import put_text

app = Flask(__name__)

@app.route('/get_ip')
def get_ip():
    user_ip = request.remote_addr
    return f'Your IP address is: {user_ip}'

def main():
    put_text("Check your IP address:").append(put_text('/get_ip'))

if __name__ == '__main__':
    start_server([main], port=8080, debug=True)
