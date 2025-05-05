from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI()

MODULES_DIR = os.path.join(os.path.dirname(__file__), 'modules')

def load_all_module_metadata():
    metadata_list = []
    for root, _, files in os.walk(MODULES_DIR):
        for file in files:
            if file == 'meta.json':
                json_path = os.path.join(root, file)
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        metadata_list.append(data)
                except Exception as e:
                    metadata_list.append({"error": f"Erreur dans {json_path}: {str(e)}"})
    return metadata_list

@app.get("/modules", response_class=JSONResponse)
def get_modules():
    metadata = load_all_module_metadata()
    return metadata
