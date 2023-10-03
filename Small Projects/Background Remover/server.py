from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/process', methods=['POST'])
def process():
    input_image = request.files['image']
    output_image = io.BytesIO()

    with input_image as img:
        remove(img, output_image)

    output_image.seek(0)
    return send_file(
        output_image,
        as_attachment=True,
        download_name='output_image.png',
        mimetype='image/png'
    )

if __name__ == '__main__':
    app.run(debug=True)