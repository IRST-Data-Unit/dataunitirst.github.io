import os

def findIndexes(folder, indent=1, content = ''):

    indentChar = ' '
    exclusion = ['assets', '.', '..', 'venv', '.git', '.github', '.idea', 'src']

    ind = {}
    for d in filter(os.path.isdir,[os.path.join(folder,x) for x in os.listdir(folder)]):
        if not os.path.basename(d) in exclusion:
            if os.path.exists(os.path.join(d, 'index.md')):
                content += (indentChar*indent + "* [" + os.path.basename(d) + "](" + d + ")" + "\n")
            else:
                content += (indentChar*indent + "* " + os.path.basename(d) + "\n")
            content += findIndexes(os.path.join(d),indent+2)

    return content

content = findIndexes(".")
print(content)


f = open("index.md", "w")
f.write(content)
f.close()
