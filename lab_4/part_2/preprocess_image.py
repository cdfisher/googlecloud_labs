from PIL import Image, ImageFilter

inf = './images/test2.webp'

# Apply some pillow filters to the image to increase contrast between the edges and background
img = Image.open(inf).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.EDGE_ENHANCE_MORE)

img.save('./images/test2_processed.webp')

