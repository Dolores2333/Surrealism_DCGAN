from PIL import Image
import os

temp = os.getcwd()
data_dir=os.path.join(temp,'../data')
folder = data_dir+'/surrealism'
outpath = data_dir+'/surrealismCroped'
if not os.path.exists(outpath):
    os.makedirs(outpath)


def picProcess(image_dir):
    if os.path.isdir(image_dir):
        return
    image = Image.open(image_dir)
    imagename = image.filename
    canonical = imagename.split('.')[0]
    image_new = image.resize((128, 128))
    if image_new.mode != 'RGB':
        image_new = image_new.convert('RGB')
    image_new.save(os.path.join(outpath, '{}.png'.format(canonical)))


def runScript():
    os.chdir(folder)
    for image_dir in os.listdir(os.getcwd()):
        if image_dir == '.DS_Store':
            continue
        picProcess(image_dir)


if __name__ == '__main__':
    runScript()
