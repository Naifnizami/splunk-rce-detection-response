from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/block', methods=['POST'])
def block_ip():
    data = request.json
    ip = data.get('attacker_ip')
    if ip:
        os.system(f"iptables -A INPUT -s {ip} -j DROP")
        return f"Blocked IP: {ip}", 200
    return "Invalid payload", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
