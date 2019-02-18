# Python File Renamer

## Parse and rename multiple files in Python

The py file must point to the target directory as the current working directory.

```py
import os

# set current working directory (cwd)
data = os.getcwd() + r'\data'
os.chdir(data)

# check cwd is correct
print(os.getcwd())

# list all files in target directory
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    file_prefix, file_body = file_name.split('-')
    new_file_name = f'{file_body}{file_ext}'
    # print(f, new_file_name)

    # after formatting to taste
    # run os.rename method
    os.rename(f, new_file_name)

```
