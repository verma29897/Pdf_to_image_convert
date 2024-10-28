import fitz  
from PIL import Image

def pdf_to_images(pdf_file):
    
    pdf_document = fitz.open(pdf_file)
    
    images = []
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        
        pix = page.get_pixmap()
        
       
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        
        images.append(img)
        img.save(f"page_{page_num+1}.png", "PNG")
    
    pdf_document.close()
    return images


pdf_to_images("krishna_kumar.pdf")
