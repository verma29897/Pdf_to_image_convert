from src import extract_text_from_image, pdf_to_images

# Use the functions
images = pdf_to_images("krishna_kumar.pdf")
text = extract_text_from_image(images[0])

print(images)
print(text)