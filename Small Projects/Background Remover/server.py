from flask import Flask, request, send_file
from rembg import remove
import tempfile
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize a global variable to store the processed image data
processed_image_data = None

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/process', methods=['POST'])
def process():
    global processed_image_data

    input_image = request.files['image']

    if input_image.filename == '':
        return 'No selected file'

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_input, \
         tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_output:

        input_image.save(temp_input.name)

        temp_input_path = temp_input.name  # Get the file path from the temporary file object

        with open(temp_input_path, 'rb') as input_file:
            input_bytes = input_file.read()

        # Process the image
        output_bytes = remove(input_bytes)

        # Store the processed image data in the global variable
        processed_image_data = output_bytes

        # Create a BytesIO object to store the processed image
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

    # You can generate a unique filename for the downloaded image or use a fixed name
    download_name = 'processed_image.png'

    # Send the processed image for download
    return send_file(
        BytesIO(processed_image_data),  # Use BytesIO to create a file-like object
        as_attachment=True,
        download_name=download_name,
        mimetype='image/png'
    )

if __name__ == '__main__':
    app.run(debug=True)
