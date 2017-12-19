from PIL import Image

src_file = r"C:\Users\keks\Dropbox\Programieren\pritzFoto\oldFotos\Zebra (2).png"

img = Image.open(src_file)

back = Image.new("RGB", [img.size[0],img.size[1]+100], "white")
back.paste(img,[0,100])

back.save(r"C:\Users\keks\Dropbox\Programieren\pritzFoto\oldFotos\Zebra (2)_out.png") 