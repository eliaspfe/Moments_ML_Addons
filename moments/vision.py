from pathlib import Path
from typing import List

import requests
from flask import current_app


def detect_objects(image_path: str) -> List[str]:
   
    api_token = current_app.config.get('HF_API_KEY')
    if not api_token:
        current_app.logger.error('HF_TOKEN not set in configuration')
        return []
        
    API_URL_LABEL= "https://router.huggingface.co/hf-inference/models/google/vit-base-patch16-224"
    
    # Determine content type based on file extension
    file_ext = Path(image_path).suffix.lower()
    if file_ext == '.png':
        content_type = 'image/png'
    elif file_ext in ['.jpg', '.jpeg']:
        content_type = 'image/jpeg'
    else:
        content_type = 'image/jpeg'  # Default fallback
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": content_type
    }

    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            current_app.logger.info(f'Sending request to HuggingFace API (format: {content_type}) with token: {api_token[:10]}...')
            response = requests.post(API_URL_LABEL, headers=headers, data=image_bytes)
        
        if response.status_code != 200:
            current_app.logger.error(f'API Response: {response.text}')
        response.raise_for_status()
        
        results = response.json()
        current_app.logger.info(f'API Response: {results}') 
        # Filter results with confidence > 0.5 and get unique labels
        detected_objects = {item['label'].lower() for item in results if item['score'] >0.1}
        return list(detected_objects)
        
    except Exception as e:
        current_app.logger.error(f'Error in object detection: {str(e)}')
        return []
    