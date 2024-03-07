## app.py
import streamlit as st
from PIL import Image
from io import BytesIO

# Define the classes as per the design specifications
class StreamlitApp:
    def run(self):
        """Main method to run the Streamlit app."""
        st.title("Image Converter App")
        image_uploader = ImageUploader()
        image_converter = ImageConverter()
        image_downloader = ImageDownloader()

        input_image = image_uploader.upload_image()
        if input_image is not None:
            output_image = image_converter.convert_image(input_image)
            image_downloader.download_image(output_image)

class ImageUploader:
    def upload_image(self):
        """Method to upload an image through Streamlit interface."""
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            return Image.open(uploaded_file)
        return None

class ImageConverter:
    def convert_image(self, input_image: Image) -> Image:
        """Method to convert the uploaded image. Currently, it just returns the input image."""
        # This method can be extended to apply various image processing techniques
        return input_image

class ImageDownloader:
    def download_image(self, output_image: Image):
        """Method to download the converted image through Streamlit interface."""
        buffered = BytesIO()
        output_image.save(buffered, format="JPEG")
        st.download_button(
            label="Download Image",
            data=buffered.getvalue(),
            file_name="converted_image.jpg",
            mime="image/jpeg",
        )

# Run the Streamlit app
if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
