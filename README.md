# SCT_CY_02
🔐 Secure Image Processor Web AppA full-stack image processor 
.
built with Python and deployed using Gradio on Hugging Face Spaces. This project demonstrates skills in image manipulation, basic cryptography, and modern MLOps deployment.
.
✨ Live ApplicationYou can access and test the deployed application directly here:$$\text{[https://huggingface.co/spaces/aleiah1skss/image-encryption-decryption-v1](https://huggingface.co/spaces/aleiah1skss/image-encryption-decryption-v1)}$$
.
🚀 How to Use the AppThe application uses the exact same key for encryption and decryption.
Select Image: Click the upload area and choose your original image (.jpg, .png).
Set Key: Enter a secret number between 0 and 255.
Operation: Select Encrypt or Decrypt.
Process: Click "Process Image." The resulting file will automatically download to your browser.
.
💡 Core Logic: Pixel Cryptography
>The application implements a simple, two-step symmetric encryption algorithm using direct pixel manipulation:
1. Substitution (Cipher): Each Red, Green, and Blue channel value ($P$) in every pixel is shifted by the secret key ($K$) using the mathematical formula:
        $$P_{encrypted} = (P_{original} + K) \pmod{256}$$
2. Transposition (Scramble): The structure of the image is scrambled by reflecting all pixels across the main diagonal (swapping coordinates $(x, y)$ with $(y, x)$).
>Note: This step is only applied to square images where $Width = Height$ to prevent image distortion.
.
⚙️ Project Setup and Tech Stack
This project is defined in a single Python file, simplifying deployment.

Required Dependencies (requirements.txt)
The application requires the following libraries:
gradio
Pillow
numpy
.
📁Files and Deployment
>app.p-----The main Python application file. Contains the encryption/decryption functions and the complete Gradio interface layout and styling.
>requirements.txt-------Defines the external Python dependencies needed for the Hugging Face server.
>README.m------This documentation file.
.
Deployment Platform: Hugging Face Spaces (using the Gradio SDK).
