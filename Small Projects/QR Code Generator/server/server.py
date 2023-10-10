from flask import Flask, render_template_string, request, jsonify
import qrcode
from io import BytesIO
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    
    img_io = BytesIO()
    img = qrcode.make(data)
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    return jsonify({"qr_code": img_base64})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)