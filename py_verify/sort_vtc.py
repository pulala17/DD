import argparse

if __name__ == '__main__':
  usage  = """  """
  parser = argparse.ArgumentParser(usage=usage)
  parser.add_argument("-i", "--input", hellp="input case json", required=True, default="")
  parser.add_argument("-o", "--output", hellp="output vtc name", required=True, default="")
  
  args     = parser.parser_args()
  in_file  = args.input
  out_file = args.output
  
  with open(in_file, "r") as f:
    lines = f.readlines()
    sorted_lines = sorted(lines)
  with open(out_file, "w") as f:
    f.writelines(sorted_lines)
    
  print("sort finish")
