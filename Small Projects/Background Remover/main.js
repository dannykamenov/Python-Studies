document.addEventListener('DOMContentLoaded', function() {
    const removeButton = document.getElementById('remove-button');
    const outputImage = document.getElementById('output-image');

    // Add an event listener to the Remove Background button
    removeButton.addEventListener('click', function() {
        console.log('Remove Background button clicked!');
        const formData = new FormData();
        formData.append('image', document.querySelector('input[type="file"]').files[0]);

        // Send a POST request to the /process endpoint using Fetch API
        fetch('https://bg-remover-bggp.onrender.com/process', {
            method: 'POST',
            body: formData,
            mode: 'no-cors'
        })
        .then(response => response.blob())
        .then(blob => {
            // Display the processed image in the preview container
            outputImage.src = URL.createObjectURL(blob);
            outputImage.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});