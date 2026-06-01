from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route('/api/info')
def info():
    return jsonify({
        "app": "Jenkins Pipeline Demo",
        "author": "DevOps Team",
        "pipeline": ["Build", "Test", "Deploy"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
