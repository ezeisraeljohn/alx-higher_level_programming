#!/usr/bin/python3

""" The module that handle command line"""

path = __import__('os').path
argv = __import__('sys').argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
json_list = [argv[i] for i in range(len(argv)) if i != 0]

if path.isfile(filename):
    if path.getsize(filename) == 0:
        save_to_json_file(json_list, filename)
    else:
        line = load_from_json_file(filename)
        for item in json_list:
            line.append(item)
        save_to_json_file(line, filename)
