import os

data = os.listdir(os.getcwd() + r'\data')

for f in data:
  file_name, file_ext = os.path.splitext(f)
  file_prefix, file_body = file_name.split('-')
  new_file_name = f'{file_body}{file_ext}'
  print(new_file_name)


