document.addEventListener('DOMContentLoaded', function() {
    const removeButton = document.getElementById('remove-button');
    const outputImage = document.getElementById('output-image');

    removeButton.addEventListener('click', function() {
        console.log('Remove Background button clicked!');
        const formData = new FormData();
        formData.append('image', document.querySelector('input[type="file"]').files[0]);

        fetch('https://bg-remover-2-0.onrender.com/process', {
            method: 'POST',
            body: formData,
            // add cors mode
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            mode: 'no-cors'
        })
        .then(response => response.blob())
        .then(blob => {
            outputImage.src = URL.createObjectURL(blob);
            outputImage.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});