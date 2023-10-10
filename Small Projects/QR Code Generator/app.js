document.getElementById('qrForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const dataInput = document.getElementById('dataInput');
    const qrImage = document.getElementById('qrImage');
    if (qrImage) {
        qrImage.remove();
    }

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
            const body = document.querySelector('body');
            const qrImage = document.createElement('img');
            qrImage.setAttribute('id', 'qrImage');
            qrImage.src = 'data:image/png;base64,' + data.qr_code;
            body.appendChild(qrImage);
        })
        .catch(error => {
            console.error('Error generating QR code:', error);
        });
    }else {
        alert('Please enter a valid link!');
    }

    dataInput.value = '';

});