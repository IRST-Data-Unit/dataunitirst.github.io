import os

def findIndexes(folder, content = ''):

    ind = {}

    for root, dirs, files in os.walk(folder):
        path = root.split(os.sep)
        for name in files:
            if name == 'index.md':
                if os.path.basename(root) != '.':
                    tmpInd = ind
                    last = len(path)-1
                    for p in path:
                        if(p!='.'):
                            if last == 1:
                                tmpInd[p] = "[" + p + "](" + os.path.join(root) + ")"
                            else:
                                tmpInd[p] = {}
                                tmpInd = tmpInd[p]
                                last -= 1

    print(ind)
    def createContent(ind, prefixLength=0, content=''):
        for d in ind:
            if (type(ind[d]) is dict):
                content += ' ' * prefixLength + '* ' + d + "\n"
                content = createContent(ind[d], prefixLength+2, content)
            else:
                content += ' '*prefixLength + '* ' + ind[d] + "\n"

        return content

    return createContent(ind)

content = findIndexes(".")
print(content)


f = open("index.md", "w")
f.write(content)
f.close()
