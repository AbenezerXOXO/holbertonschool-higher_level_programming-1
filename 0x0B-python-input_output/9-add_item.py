#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
with open("add_item.json", 'w') as f:
    f.write("")
obj = load_from_json_file("add_item.json")
l = []
for i in sys.argv:
    l.append(i)
obj = obj + l
save_to_json_file(obj, "add_item.json")
