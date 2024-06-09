# Everything is in a docstring!
"""
>>> from wc import getLinecount, getWordcount, getBytecount, output, error


>>> getLinecount('testinputs/blank.txt')
0
>>> getWordcount('testinputs/blank.txt')
0
>>> getBytecount('testinputs/blank.txt')
0
>>> output(True, True, True, 0, 0, 0, 'testinputs/blank.txt')
'\\t0\\t0\\t0\\ttestinputs/blank.txt'

>>> getLinecount('testinputs/chinese.txt')
21
>>> getWordcount('testinputs/chinese.txt')
1127
>>> getBytecount('testinputs/chinese.txt')
8483


>>> getLinecount('testinputs/miniwc.py')
39
>>> getWordcount('testinputs/miniwc.py')
109
>>> getBytecount('testinputs/miniwc.py')
1036


>>> getLinecount('testinputs/htmlTest.html')
15
>>> getWordcount('testinputs/htmlTest.html')
229
>>> getBytecount('testinputs/htmlTest.html')
2488


>>> getLinecount('testinputs/die.java')
126
>>> getWordcount('testinputs/die.java')
533
>>> getBytecount('testinputs/die.java')
3608


>>> getLinecount('testinputs/arabic.txt')
19
>>> getWordcount('testinputs/arabic.txt')
485
>>> getBytecount('testinputs/arabic.txt')
4898


>>> output(True, False, False, 39, 109, 1036, 'testinputs/miniwc.py')
'\\t39\\ttestinputs/miniwc.py'
>>> output(False, True, False, 39, 109, 1036, 'testinputs/miniwc.py')
'\\t109\\ttestinputs/miniwc.py'
>>> output(False, False, True, 39, 109, 1036, 'testinputs/miniwc.py')
'\\t1036\\ttestinputs/miniwc.py'
>>> output(True, False, True, 39, 109, 1036, 'testinputs/miniwc.py')
'\\t39\\t1036\\ttestinputs/miniwc.py'
>>> output(False, False, False, 39, 109, 1036, 'testinputs/miniwc.py')
'\\t39\\t109\\t1036\\ttestinputs/miniwc.py'
>>> output(True, True, True, 39, 109, 1036, 'testinputs/miniwc.py')
'\\t39\\t109\\t1036\\ttestinputs/miniwc.py'


>>> error('invalid',"'a'")
"wc: invalid option -- 'a'\\nTry 'wc --help' for more information."
>>> error('noFile','d')
'wc: d: No such file or directory'
>>> error('noFile','-')
'wc: -: No such file or directory'
>>> error('noFile','')
'wc: No such file or directory'

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest.testfile('testinputs/testcase.txt')
