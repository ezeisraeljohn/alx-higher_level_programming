#!/usr/bin/python3

""" The module that handle command line"""


argv = __import__('sys').argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


json_list = [argv[i] for i in range(len(argv)) if i != 0]

filename = 'add_item.json'

save_to_json_file(json_list, filename)

result = load_from_json_file(filename)
