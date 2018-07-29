import json
import os

country = ['au', 'br', 'br2', 'eu', 'in', 'kr2', 'us', 'vn2', 'bh']

plate_count = dict()
for c in country:
    plate_count[c] = 0


def update_plate_detection(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    for c in country:
        x = data[c]
        if len(x['results']) > 0:
            plate_count[c] += 1
    return


def count_detection(alpr_json_dir):
    extensions = ['.json']
    count = 0
    x = os.listdir(alpr_json_dir)
    for i in x:
        e = os.path.splitext(i)[1]
        if e in extensions:
            json_file = os.path.join(alpr_json_dir, i)
            update_plate_detection(json_file=json_file)
            count += 1
    print('Total count: {}'.format(count))
    for key in plate_count:
        print('{0}: {1} {2}'.format(key, plate_count[key], plate_count[key]*1.0/count))

    return


count_detection(alpr_json_dir='/home/prakash/pc/alpr-analysis/alpr_json/')