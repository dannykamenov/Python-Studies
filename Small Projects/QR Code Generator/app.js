document.getElementById('qrForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const dataInput = document.getElementById('dataInput');
    const qrImage = document.getElementById('qrImage');

    // Check if input is link
    if (dataInput.value.includes('http') || dataInput.value.includes('https')) {
        fetch('https://qr-code-generator-hvve.onrender.com/generate_qr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: dataInput.value })
        })
        .then(response => response.json())
        .then(data => {
            qrImage.src = 'data:image/png;base64,' + data.qr_code;
        })
        .catch(error => {
            console.error('Error generating QR code:', error);
        });
    }else {
        alert('Please enter a valid link!');
    }

});