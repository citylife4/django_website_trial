import argparse
import json

name_json_file = "proj_labels.json"
local_json_file = name_json_file

parser = argparse.ArgumentParser(description='Save label on file')
parser.add_argument('-m', '--macro', nargs=1, type=str, required=True,
                    help='Macro for the label')
parser.add_argument('-l', '--label', nargs=1, type=str, required=True,
                    help='Label to save on file')
parser.add_argument('-p', '--proj', nargs='+', default=["n214", "n212"], required=True,
                    help='Corresponding projects for label')

args = parser.parse_args()
macro = args.macro[0].upper()
label = args.label[0]

projects = json.load(open(local_json_file))

print("opening file")

for project in args.proj:
    projects[project][macro] = label

with open(local_json_file, 'w') as f:
    json.dump(projects, f, indent=4, sort_keys=True)
