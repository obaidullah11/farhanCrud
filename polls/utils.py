from PIL import Image
import io
from django.core.files.base import ContentFile

def compress_image(image, max_size_mb=5):
    """
    Compress the image to be less than max_size_mb in size.
    """
    # Convert to a PIL Image object
    img = Image.open(image)
    
    # Initialize variables
    quality = 100
    size = max_size_mb * 1024 * 1024  # Convert MB to bytes

    # Check and reduce quality until the image is below the size limit
    while True:
        img_io = io.BytesIO()
        img.save(img_io, format='JPEG', quality=quality)
        
        # If the image is less than the max size, break
        if img_io.tell() <= size:
            break

        # Reduce the quality
        quality -= 10
        if quality < 10:
            raise Exception("Cannot compress image to the desired size")

    # Create a ContentFile to be saved in Django's FileField
    return ContentFile(img_io.getvalue(), name=image.name)
