from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eyetracking', methods=['POST'])
def eyetracking():
    data = request.json
    print(data)
    return jsonify({"status": "success", "received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
