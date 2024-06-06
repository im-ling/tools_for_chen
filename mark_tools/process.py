import json
import copy
import string
import random


def random_string(length):
    # result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    result = ''.join(random.choices(string.ascii_letters, k=length))
    return result


def process_json(target_file_path, output_file_path, target_len):

    dic = {}

    # Opening JSON file
    with open(target_file_path, 'r') as f:
        # Reading from json file
        dic = json.load(f)

    metadata = dic['metadata']
    new_metadata = {}
    # print(metadata)

    for key in metadata.keys():
        if ("1_" in key):
            new_metadata[key] = metadata[key]
            for i in range(2, target_len):
                new_item = copy.deepcopy(metadata[key])
                new_item['vid'] = i
                new_key = str(i) + "_" + random_string(8)
                new_metadata[new_key] = new_item
    
    dic['metadata'] = new_metadata
    # Writing to sample.json
    with open(output_file_path, 'w') as f:
        json.dump(dic, f, indent=4)

target_file_path = 'via_project_06Jun2024_13h32m05s.json'
output_file_path = 'via_project_06Jun2024_13h32m05s_processed.json'
target_len = 27
# target_file_path = os.path.join(os.getcwd(), target_file_path)
# output_file_path = os.path.join(os.getcwd(), output_file_path)
process_json(target_file_path, output_file_path, target_len)

