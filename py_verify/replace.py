import os
import re

folder_path = 'project/module/tests'
file_name   = os.listdir(folder_path)
rules_fules = [file_name for file_name in file_names if re.search(r"rules$", file_name)] 

for file_name in rule_files:
  file_path = os.path.join(folder_path, file_name)
  with open(file_path, "r") as f:
    content = f.read()
  new_content = re.sub(r"12", "20", content)
  with open(file_path, "w") as f:
    f.write(new_content)
    
  print(file_name + "replace finish")
