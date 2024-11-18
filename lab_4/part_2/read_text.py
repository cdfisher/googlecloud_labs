# Written referencing the following:
# https://cloud.google.com/vision/docs/ocr

from google.cloud import vision

# Create client instance
client = vision.ImageAnnotatorClient()


def get_text(filepath: str):
    with open(filepath, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform the label detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Print text found in file
    fname = filepath.split('/')[-1]
    print(f"Text in {fname}: ")
    for text in texts:
        print(text.description)


images = ['test.webp', 'test2.webp', 'test2_processed.webp', 'test3.jpg']

if __name__ == '__main__':
    for img in images:
        get_text(f'./images/{img}')
        print('\n')

