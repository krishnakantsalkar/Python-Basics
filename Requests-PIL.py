import requests
from PIL import Image
from io import BytesIO


r = requests.get(
    "https://krishnakantsalkar.github.io/My-App/assets/images/fb-cover.jpg")

print(r.url)
print("Status Code:", r.status_code)
print(r.text)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./test-image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("couldn't save Image")
