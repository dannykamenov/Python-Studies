from flask import Flask, request, send_file
from rembg import remove
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/process', methods=['POST'])
def process():
    input_image = request.files['image']

    if input_image.filename == '':
        return 'No selected file'

    with tempfile.NamedTemporaryFile(delete=False) as temp_input, \
         tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_output:

        input_image.save(temp_input)

        temp_input_path = temp_input.name  # Get the file path from the temporary file object

        with open(temp_input_path, 'rb') as input_file:
            input_bytes = input_file.read()
        
        output_bytes = remove(input_bytes)  # Pass the input image as bytes to remove function

        temp_output.write(output_bytes)
        temp_output.seek(0)

        return send_file(
            temp_output.name,
            as_attachment=True,
            download_name='output_image.png',
            mimetype='image/png'
        )



if __name__ == '__main__':
    app.run(debug=True)