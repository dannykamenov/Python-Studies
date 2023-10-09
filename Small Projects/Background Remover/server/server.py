from flask import Flask, request, send_file
from rembg import remove
import tempfile
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


processed_image_data = None

@app.route('/process', methods=['POST'])
def process():
    global processed_image_data

    input_image = request.files['image']

    if input_image.filename == '':
        return 'No selected file'

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_input, \
         tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_output:

        input_image.save(temp_input.name)

        temp_input_path = temp_input.name  

        with open(temp_input_path, 'rb') as input_file:
            input_bytes = input_file.read()

        output_bytes = remove(input_bytes)

        processed_image_data = output_bytes

        output_buffer = BytesIO()
        output_buffer.write(output_bytes)
        output_buffer.seek(0)

        return send_file(
            output_buffer,
            mimetype='image/png'
        )

@app.route('/download')
def download():
    global processed_image_data

    if processed_image_data is None:
        return 'No processed image data available'

    download_name = 'processed_image.png'

    return send_file(
        BytesIO(processed_image_data), 
        as_attachment=True,
        download_name=download_name,
        mimetype='image/png'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
