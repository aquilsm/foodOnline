from django.core.exceptions import ValidationError
import os


def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extensions = ['.png', 'jpeg', '.jfif', 'pjp', '.pjpeg', '.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Upload a valid image. The file you uploaded was either not an image or a corrupted image. Allowed extension:' +str(valid_extensions))