from google.cloud import vision, storage
from PIL import Image, ImageDraw

# Create client instance
client = vision.ImageAnnotatorClient()


def mark_text():
    storage_client = storage.Client()
    bucket_name = ''
    bucket = storage_client.bucket(bucket_name)

    dl_blob = bucket.blob('test.webp')
    filepath = 'dl/test.webp'
    dl_blob.download_to_filename(filepath)

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
    # todo upload to bucket
    # https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python

    source_file_path = f'output/test.webp'
    destination_blob_name = 'test-marked.webp'


    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path, if_generation_match=0)



images = ['test.webp', 'test2.webp', 'test3.jpg']

if __name__ == '__main__':
    for img in images:
        mark_text(f'./images/{img}')
