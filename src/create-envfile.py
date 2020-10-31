import os

print('wowza')

env_keys = list(dict(os.environ).keys())

out_file = ""

for key in env_keys:
    print('yes',key)
    # if key.startswith("INPUT_ENVKEY_"):
    #     out_file += key.split("INPUT_ENVKEY_")[1] + "=" + os.environ.get(key) + "\n"
    out_file += key + "=" + os.environ.get(key) + "\n"

with open("/github/workspace/" + str(os.environ.get("INPUT_FILE_NAME")), "w") as text_file:
    text_file.write(out_file)