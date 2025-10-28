import gradio as gr
from PIL import Image
import numpy as np
import os

# --- CORE ENCRYPTION / DECRYPTION LOGIC (Functions) ---

def process_image(img, key_int, operation):
    """
    Encrypts or Decrypts the PIL Image object based on user input.
    """
    if img is None:
        return None, "Error: Please upload an image."

    try:
        # Convert key to integer and validate
        key = int(key_int)
        if not 0 <= key <= 255:
            return None, "Error: Key must be between 0 and 255."
            
        img = img.convert("RGB")
        width, height = img.size
        pixels = img.load()

        # Determine the factor: +key for encrypt, -key for decrypt
        factor = key if operation == "Encrypt" else -key

        # 1. Mathematical Operation
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                new_r = (r + factor) % 256
                new_g = (g + factor) % 256
                new_b = (b + factor) % 256
                pixels[x, y] = (new_r, new_g, new_b)

        # 2. Pixel Swapping (Diagonal Reflection) - Only done for square images
        if width == height:
            swapped_img = Image.new('RGB', (width, height))
            swapped_pixels = swapped_img.load()
            for y in range(height):
                for x in range(width):
                    swapped_pixels[y, x] = pixels[x, y]
            img = swapped_img 
            message = f"✅ Successfully {operation}ed image. (Diagonal reflection applied)."
        else:
            message = f"✅ Successfully {operation}ed image. (Diagonal reflection skipped)."
            
        return img, message

    except ValueError:
        return None, "❌ Error: Invalid key. Please enter a number."
    except Exception as e:
        return None, f"❌ An unexpected error occurred: {e}"


# --- GRADIO INTERFACE SETUP (Simplified and Stable) ---

# Use the Monochronic theme as it is generally stable and attractive
custom_theme = gr.themes.Monochrome()

with gr.Blocks(theme=custom_theme, title="Image Processor") as interface:
    gr.Markdown(
        """
        # 🔐 Secure Image Processor
        ### Simple Pixel Encryption/Decryption Tool
        """
    )

    with gr.Row(): 
        # LEFT COLUMN (Inputs)
        with gr.Column(scale=1):
            image_input = gr.Image(type="pil", label="1. Upload Image")
            
            operation_radio = gr.Radio(
                ["Encrypt", "Decrypt"], 
                label="3. Choose Operation", 
                value="Encrypt",
            )
            
            # Using gr.Number is the correct component and avoids the Textbox errors
            key_input = gr.Number(
                label="2. Encryption Key (0-255)", 
                value=50,
                minimum=0, 
                maximum=255, 
                precision=0 # Ensures no decimals
            )

            # Define the button separate from the function
            process_btn = gr.Button("🚀 Process Image", variant="primary")
            
        # RIGHT COLUMN (Outputs)
        with gr.Column(scale=1):
            image_output = gr.Image(type="pil", label="Processed Image (Download)")
            status_box = gr.Textbox(label="Status Message", interactive=False)

    # Define the action when the button is clicked
    process_btn.click(
        fn=process_image,
        inputs=[image_input, key_input, operation_radio],
        outputs=[image_output, status_box]
    )

# --- LAUNCH THE APP ---
if __name__ == "__main__":
    interface.launch(inbrowser=True)