
from django.core.exceptions import ValidationError

def validate_file_type(value):
    valid_mime_types = [
        'application/pdf',  # PDF
        'application/msword',  # DOC
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',  # DOCX
        'application/vnd.ms-excel',  # XLS
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',  # XLSX
        'application/vnd.ms-powerpoint',  # PPT
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',  # PPTX
        'text/plain',  # TXT
        'application/rtf',  # RTF
        'image/png',  # PNG (optional)
        'image/jpeg',  # JPEG (optional)
        'image/gif'  # GIF (optional)
    ]


    
    file_mime_type = value.file.content_type
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')


def validate_file_size(value):
    limit = 5 * 1024 * 1024  # 5MB limit
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')