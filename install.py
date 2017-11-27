import os

packages = [
    'requests'
]

for item in packages:
    print("start intall "+item)
    cmd = 'pip install '+item
    print(os.system(cmd))
    print('finish intall '+item)
    print("\r\n")