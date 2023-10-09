from flask import Flask, render_template_string, request
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        data = request.form.get('data')
    
    img_io = None
    if data:
        img = qrcode.make(data)
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
    
    return render_template_string('''
    <form method="post">
        Data: <input type="text" name="data">
        <input type="submit" value="Generate QR">
    </form>
    {% if img_io %}
        <h2>Your QR Code:</h2>
        <img src="data:image/png;base64,{{ img_io.getvalue() | b64encode }}">
    {% endif %}
    ''', img_io=img_io)

@app.template_filter('b64encode')
def b64encode(s):
    import base64
    return base64.b64encode(s).decode('utf-8')  # Here, we're encoding the bytes directly

if __name__ == '__main__':
    app.run(debug=True)