from PIL import Image, ImageFilter

img = Image.open('pokedex/charmander.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png','png')


print(img)