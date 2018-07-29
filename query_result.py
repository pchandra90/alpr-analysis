import json
import os
import sys

country = ['au', 'br', 'br2', 'eu', 'in', 'kr2', 'us', 'vn2', 'bh']


def filter_from_candidate(candidate):
    matched_patterns = []
    for x in candidate:
        if x['matches_template'] == 1:
            matched_patterns.append((x['plate'], x['confidence']))
    if len(matched_patterns) > 0:
        matched_patterns.sort(reverse=True, key=lambda i: i[1])
    if len(matched_patterns) > 5:
        matched_patterns = matched_patterns[:5]
    x = list()
    for i in matched_patterns:
        x.append((i[0].encode('ascii', 'ignore'), i[1]))

    return x


def print_results(country, results):
    print('----------------------{}----------------------'.format(country))
    for i, x in enumerate(results):
        l = []
        matched_patterns = filter_from_candidate(x['candidates'])
        if len(matched_patterns) == 0:
            l.append((x['plate'].encode('ascii', 'ignore'), x['confidence']))
        else:
            l = matched_patterns
        print('Plate {0}: {1}'.format(i, l))
    return


def get_result(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    for c in country:
        x = data[c]
        if len(x['results']) > 0:
            print_results(country=c, results=x['results'])
    return


def get_result_by_iamge_num(img_num):
    alpr_json = '/home/prakash/pc/alpr-analysis/alpr_json/'
    json_file = os.path.join(alpr_json, '{}.json'.format(str(img_num).zfill(3)))
    get_result(json_file=json_file)
    return


get_result_by_iamge_num(int(sys.argv[1]))




