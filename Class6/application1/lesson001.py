print("How do we open a file again?")

import json

json_file = 'death.data'

print("Contents of File:")
print(open(json_file,'r').read())

raw_input("Continue...")