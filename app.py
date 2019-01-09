import os

data = os.getcwd() + r'\data'
os.chdir(data)
print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_prefix, file_body = file_name.split('-')
    new_file_name = f'{file_body}{file_ext}'
    os.rename(f, new_file_name)
