from google.cloud import vision
from PIL import Image, ImageDraw

# Create client instance
client = vision.ImageAnnotatorClient()


def mark_text(filepath: str):
    fname = filepath.split('/')[-1]

    with open(filepath, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    out_img = Image.open(filepath)
    draw = ImageDraw.Draw(out_img)

    for text in texts:
        box = [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#0000aa')

    out_img.save(f'./output/{fname}')


images = ['test.webp', 'test2.webp', 'test2_processed.webp', 'test3.jpg']

if __name__ == '__main__':
    for img in images:
        mark_text(f'./images/{img}')
