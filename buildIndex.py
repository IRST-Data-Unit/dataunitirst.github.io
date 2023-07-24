import os

def findIndexes(folder, content = ''):

    ind = {}

    for root, dirs, files in os.walk(folder):
        path = root.split(os.sep)
        for name in files:
            if name == 'index.md':
                if os.path.basename(root) != '.':
                    tmpInd = ind
                    for p in path:
                        if(p!='.'):
                            tmpInd[p] = {}
                            tmpInd = tmpInd[p]
                    tmpInd['file'] = "[" + os.path.join(root) + "](" + os.path.join(root) + ")"

    def createContent(ind, prefixLength=0, content=''):
        for d in ind:
            if (type(ind[d]) is dict):
                if (d != 'file'):
                    content += ' ' * prefixLength + '* ' + d + "\n"
                content = createContent(ind[d], prefixLength+2, content)
            else:
                if d=='file':
                    content += ' '*prefixLength + '* ' + ind[d] + "\n"

        return content

    return createContent(ind)

content = findIndexes(".")

f = open("index.md", "w")
f.write(content)
f.close()
