
from . import stringutils


def loadList(inputFilePath):
    lines = []
    if not inputFilePath:
        return lines
    else:
        try:
            f = open(inputFilePath, "rU")

            for line in f:
                lines.append(stringutils.formatString(line))

        except Exception as e:
            print(e)

        finally:
            f.close()


        return lines

def loadListFile(fileName, encodings="utf-8"):
    lines = []
    data = ""
    try:
        f = open(fileName, "rU")

        for line in f:
            line = line.strip("\n")
            if line:
                lines.append(line)

    except Exception as e:
        print(e)


    return lines
