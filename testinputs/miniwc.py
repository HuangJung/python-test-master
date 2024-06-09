# using subprocess
"""
if __name__ == "__main__":
    import sys,subprocess
    if len(sys.argv) != 2:
        print("Please add 'one' filepath.") 
    else:
        result = subprocess.call(['wc', sys.argv[1]])
        print(result)
"""

#not using subprocess
def miniwc(filepath):
    linecount = 0
    wordcount = 0
    bytecount = 0
    try:
        with open(filepath,'r',encoding='utf-8',errors='ignore') as file:
            result = file.readlines()
            linecount = len(result)
        
            for line in result:
                word = line.split()
                wordcount = wordcount + len(word)
                byte = line
                bytecount = bytecount + len(byte)

        return str(linecount) + '\t' + str(wordcount) + '\t' + str(bytecount) + '\t' + file.name
    except:
        return 'miniwc: '+filepath+': No such file or directory'

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Please add 'one' filepath.") 
    else:
        print(miniwc(sys.argv[1]))


