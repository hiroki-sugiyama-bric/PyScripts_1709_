import json
import os

SRC_LABELS_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10/labels_update_modified_171013.json'
DEST_LABELS_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10/labels_update_modified_171013_part_10.json'
WEBSITE_DIRS_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10'

def get_websites():
    files = os.listdir(WEBSITE_DIRS_PATH)
    websites = [d for d in files if os.path.isdir(os.path.join(WEBSITE_DIRS_PATH, d))]

    return websites

def pickup_from_file(websites):
    with open(SRC_LABELS_PATH, mode='r') as f:
        labels = json.load(f)

        return {k: v for k, v in labels.items() if k in websites}

def copy_to_file(labels):
    with open(DEST_LABELS_PATH, mode='w') as f:
        json.dump(labels, f, indent=4)

def pickup_labels():
    websites = get_websites()
    labels = pickup_from_file(websites)
    copy_to_file(labels)

if __name__ == '__main__':
    pickup_labels()


