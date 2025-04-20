from PIL import Image
import requests
from io import BytesIO

# Direct image URL
image_url = 'https://static1.moviewebimages.com/wordpress/wp-content/uploads/movie/i0DBDLhuWiY4ue0we5ebwb0W6gxRJF.jpg'

# Fetch the image from the URL
response = requests.get(image_url)

# Check if the request was successful
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))  # Open the image with PIL
    img.show()  # Display the image using PIL
else:
    print("Failed to retrieve the image.")
