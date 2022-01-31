# from Pillow import Image
from os import listdir, path
import pathlib

from PIL import Image


def get_full_paths(directory):
    full_paths = []
    for file in pathlib.Path(directory).glob('**/*'):
        full_path = pathlib.Path(file).absolute()
        print(full_path)
        if 'DS_Store' in str(full_path):
            continue
        full_paths.append(pathlib.Path(file).absolute())
    return full_paths


backgrounds = get_full_paths('../img/background')
base_images: list[pathlib.Path] = get_full_paths('../img/base_images')
hats = get_full_paths('../img/hats')
shades = get_full_paths('../img/shades')
capes = get_full_paths('../img/capes')
mouths = get_full_paths('../img/mouth')
nfts_to_make = 0


def create_image(background_counter, base_counter, hats_counter, shades_counter, capes_counter, mouth_counter, nft_counter):
    background_layer = backgrounds[background_counter]
    base_layer = base_images[base_counter]
    hats_layer = hats[hats_counter]
    shades_layer = shades[shades_counter]
    capes_layer = capes[capes_counter]
    mouth_layer = mouths[mouth_counter]
    bg = Image.open(background_layer).convert("RGBA")
    base = Image.open(base_layer).convert("RGBA")
    hat = Image.open(hats_layer).convert("RGBA")
    shade = Image.open(shades_layer).convert("RGBA")
    cape = Image.open(capes_layer).convert("RGBA")
    mouth = Image.open(mouth_layer).convert("RGBA")
    intermediate0 = Image.alpha_composite(bg, base)
    intermediate = Image.alpha_composite(intermediate0, hat)
    intermediate2 = Image.alpha_composite(intermediate, shade)
    intermediate3 = Image.alpha_composite(intermediate2, cape)
    intermediate4 = Image.alpha_composite(intermediate3, mouth)

    name = "./Hippos" + str(nft_counter) + ".png"
    intermediate4.save(name)


for background in range(len(backgrounds)):
    for base_image in range(len(base_images)):
        for ht in range(len(hats)):
            for shd in range(len(shades)):
                for cp in range(len(capes)):
                    for mth in range(len(mouths)):
                        create_image(background, base_image, ht, shd, cp, mth, nfts_to_make)
                        nfts_to_make += 1

# bg = Image.open(backgrounds[0])
# hippo = Image.open(base_images[0])
# hippo.putalpha(128)
# hat = Image.open(hats[0])
# shades = Image.open(shades[0])
#
# bg.paste(hippo)
# # bg.paste(hat)
# bg.save('./result.png')