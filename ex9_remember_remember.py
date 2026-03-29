from PIL import Image




def decrypt_msg(path):
    img=Image.open(path)
    if img:
        width, height = img.size

        im=img.load()
        #if img.mode==1:   white and black image
        result = []
        for w in range(width):
            for h in range(height):
                if im[w,h] ==1:  # balck
                    result = result + [h]  #or directly result = result + chr(i)

        return "".join(map(chr,result))

print(decrypt_msg("./code.png"))
