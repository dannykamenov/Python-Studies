document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const downloadLink = document.getElementById('download-link');
    const outputImage = document.getElementById('output-image');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('/process', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const blob = await response.blob();
                const objectURL = URL.createObjectURL(blob);

                // Display the processed image and download link
                outputImage.src = objectURL;
                outputImage.style.display = 'block';
                downloadLink.href = objectURL;
                downloadLink.style.display = 'block';
            } else {
                console.error('Error processing image.');
            }
        } catch (error) {
            console.error('Error processing image:', error);
        }
    });
});