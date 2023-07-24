import os

def findIndexes(folder, content = ''):
    for root, dirs, files in os.walk(folder):
        path = root.split(os.sep)
        for name in files:
            if name == 'index.md':
                if os.path.basename(root) != '.':
                    content += "* [" + os.path.basename(root) + "](" + os.path.join(root,name) + ")\n"
    return content

content = findIndexes(".")

print("CONTENT:")
print(content)

f = open("index.md", "w")
f.write(content)
f.close()
