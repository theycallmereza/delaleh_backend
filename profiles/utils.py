import os
from datetime import datetime


def custom_image_upload_to(instance, filename):
    """
    Generate a custom filename for the uploaded image.
    """
    # Get the file extension
    ext = filename.split(".")[-1]

    # Generate a unique filename with UUID and current timestamp
    unique_filename = f"{instance.user.pk}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"

    # Define the upload path
    upload_path = os.path.join("profile_images", unique_filename)

    return upload_path
