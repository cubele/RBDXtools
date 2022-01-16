header = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
"""

start = """    <dict>
		<key>LIST</key>
		<array>
"""

end = """        </array>
		<key>NAME</key>
		<string>{}</string>
		<key>PLID</key>
		<string>{}</string>
	</dict>
"""

footer = """</array>
</plist>
"""

import random, string
def createList(name, ids, cstr) -> str:
    cstr += start
    for id in ids:
        cstr += "            <integer>{}</integer>\n".format(str(id))
    cstr += end.format(name, ''.join(random.sample(string.ascii_lowercase + string.digits, 32)))
    return cstr

def printList(content):
    with open("./output/playlist", "w") as f:
        f.write(header)
        f.write(content)
        f.write(footer)