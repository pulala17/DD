import os
import re

folder_path = '/module/tests/algo'
files       = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
rules_files = [file_name for file_name in files if re.search(r"rules$", file_name)]
files       = [f[:-6] for f in rule_files]

with open('algo.cfg', 'w') as f:
   for filename in files:
      f.write('project/module:algo.' + filename + '\n')
    print("regression list done")
