import json
import os


country = ['au', 'br', 'br2', 'eu', 'in', 'kr2', 'us', 'vn2', 'bh']


def run_alpr(image, json_dir='alpr_json'):
    x = os.path.basename(image)
    x = os.path.splitext(x)[0]
    json_file = os.path.join(json_dir, '{}.json'.format(x))

    dic = dict()
    for c in country:
        x = os.popen('alpr -c {0} -p base {1} -n 40 -j\n'.format(c, image)).read()
        j = json.loads(x)
        dic[c] = j

    with open(json_file, 'w') as f:
        json.dump(dic, f)
    return


# run_alpr(image='/home/prakash/pc/numberplate_720p/001.png')

def run_for_all_images_in_dir(dir):
    extensions = ['.png', '.jpg', '.jpeg']
    x = os.listdir(dir)
    for i in x:
        e = os.path.splitext(i)[1]
        if e in extensions:
            img_path = os.path.join(dir, i)
            run_alpr(image=img_path)
    return


run_for_all_images_in_dir(dir='/home/prakash/pc/numberplate_720p/')


