import unittest
from wc import getLinecount,getWordcount,getBytecount,output,error
#--------------------------------------define class---------------------------------------------------#
class Line:
    def count(self, file):
        result = getLinecount(file)
        return result
class Word:
    def count(self, file):
        result = getWordcount(file)
        return result
class Byte:
    def count(self, file):
        result = getBytecount(file)
        return result
class Output:
    def count(self, l, w, c, linecount, wordcount, bytecount, filename):
        result = output(l, w, c, linecount, wordcount, bytecount, filename)
        return result
class Error:
    def count(self, type,message):
        result = error(type,message)
        return result

#--------------------------------------test case---------------------------------------------------#
class TestLine(unittest.TestCase):
    def setUp(self):
        self.line = Line()

    def tearDown(self):
        self.line = None

    def test_line_with_blank(self):
        self.assertEqual(self.line.count('testinputs/blank.txt'), 0)

    def test_line_with_chinese(self):
        self.assertEqual(self.line.count('testinputs/chinese.txt'), 21)

    def test_line_with_html(self):
        self.assertEqual(self.line.count('testinputs/htmlTest.html'), 15)

    def test_line_with_java(self):
        self.assertEqual(self.line.count('testinputs/die.java'), 126)

    def test_line_with_arabic(self):
        self.assertEqual(self.line.count('testinputs/arabic.txt'), 19)

    def test_line_with_py(self):
        self.assertEqual(self.line.count('testinputs/miniwc.py'), 39)


class TestWord(unittest.TestCase):
    def setUp(self):
        self.word = Word()

    def tearDown(self):
        self.word = None

    def test_word_with_blank(self):
        self.assertEqual(self.word.count('testinputs/blank.txt'), 0)

    def test_word_with_chinese(self):
        self.assertEqual(self.word.count('testinputs/chinese.txt'), 1127)

    def test_word_with_html(self):
        self.assertEqual(self.word.count('testinputs/htmlTest.html'), 229)

    def test_word_with_java(self):
        self.assertEqual(self.word.count('testinputs/die.java'), 533)

    def test_word_with_arabic(self):
        self.assertEqual(self.word.count('testinputs/arabic.txt'), 485)

    def test_word_with_py(self):
        self.assertEqual(self.word.count('testinputs/miniwc.py'), 109)


class TestByte(unittest.TestCase):
    def setUp(self):
        self.byte = Byte()

    def tearDown(self):
        self.byte = None

    def test_byte_with_blank(self):
        self.assertEqual(self.byte.count('testinputs/blank.txt'), 0)

    def test_byte_with_chinese(self):
        self.assertEqual(self.byte.count('testinputs/chinese.txt'), 8483)

    def test_byte_with_html(self):
        self.assertEqual(self.byte.count('testinputs/htmlTest.html'), 2488)

    def test_byte_with_java(self):
        self.assertEqual(self.byte.count('testinputs/die.java'), 3608)

    def test_byte_with_arabic(self):
        self.assertEqual(self.byte.count('testinputs/arabic.txt'), 4898)

    def test_byte_with_py(self):
        self.assertEqual(self.byte.count('testinputs/miniwc.py'), 1036)



class TestOutput(unittest.TestCase):
    def setUp(self):
        self.output = Output()

    def tearDown(self):
        self.output = None

    def test_output_with_blank(self):
        self.assertEqual(self.output.count(True, True, True, 0, 0, 0, 'testinputs/blank.txt'), '\t0\t0\t0\ttestinputs/blank.txt')

    def test_output_with_py_T(self):
        self.assertEqual(self.output.count(True, True, True, 39, 109, 1036, 'testinputs/miniwc.py'), '\t39\t109\t1036\ttestinputs/miniwc.py')

    def test_output_with_py_F(self):
        self.assertEqual(self.output.count(False, False, False, 39, 109, 1036, 'testinputs/miniwc.py'), '\t39\t109\t1036\ttestinputs/miniwc.py')

    def test_output_with_py_l(self):
        self.assertEqual(self.output.count(True, False, False, 39, 109, 1036, 'testinputs/miniwc.py'), '\t39\ttestinputs/miniwc.py')

    def test_output_with_py_w(self):
        self.assertEqual(self.output.count(False, True, False, 39, 109, 1036, 'testinputs/miniwc.py'), '\t109\ttestinputs/miniwc.py')

    def test_output_with_py_c(self):
        self.assertEqual(self.output.count(False, False, True, 39, 109, 1036, 'testinputs/miniwc.py'), '\t1036\ttestinputs/miniwc.py')

    def test_output_with_py_lc(self):
        self.assertEqual(self.output.count(True, False, True, 39, 109, 1036, 'testinputs/miniwc.py'), '\t39\t1036\ttestinputs/miniwc.py')


class TestError(unittest.TestCase):
    def setUp(self):
        self.error = Error()

    def tearDown(self):
        self.error = None

    def test_error_with_invalid(self):
        self.assertEqual(self.error.count('invalid',"'a'"), "wc: invalid option -- 'a'\nTry 'wc --help' for more information.")

    def test_error_with_noFile_d(self):
        self.assertEqual(self.error.count('noFile','d'), 'wc: d: No such file or directory')

    def test_error_with_noFile_dash(self):
        self.assertEqual(self.error.count('noFile','-'), 'wc: -: No such file or directory')

    def test_error_with_noFile_empty(self):
        self.assertEqual(self.error.count('noFile',''), 'wc: No such file or directory')




if __name__ == "__main__":
    unittest.main()
