from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import fitz  # PyMuPDF
from PIL import Image
import os

app = FastAPI()

# Directory to store generated images
OUTPUT_DIR = "output_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def pdf_to_images(pdf_file):
    pdf_document = fitz.open(pdf_file)
    images = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save the image to the output directory as PNG
        img_path = os.path.join(OUTPUT_DIR, f"page_{page_num+1}.png")
        img.save(img_path, "PNG")
        
        images.append(img_path)
    
    pdf_document.close()
    return images

@app.post("/convert-pdf-to-images/")
async def convert_pdf_to_images(file: UploadFile = File(...)):
    # Save the uploaded PDF file to a temporary location
    pdf_path = f"{file.filename}"
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # Convert the PDF to images
    images = pdf_to_images(pdf_path)

    # Optionally clean up the PDF file
    os.remove(pdf_path)

    # Generate download links for each image
    download_links = [f"/download-image/{os.path.basename(img_path)}" for img_path in images]

    return {"download_links": download_links}


