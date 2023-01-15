from PIL import Image

with Image.open("explosion.png") as im:
    # Resize the image
    im_resized = im.resize((50, 50))
    # Save the resized image
    im_resized.save("resizeexplosion.png")