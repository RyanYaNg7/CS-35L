#!/usr/bin/python

"""
Output lines selected randomly from a file
Copyright 2005, 2007 Paul Eggert.
Copyright 2010 Darrell Benjamin Carbajal.
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
Please see <http://www.gnu.org/licenses/> for a copy of the license.
$Id: randline.py,v 1.4 2010/04/05 20:04:43 eggert Exp $
"""

import sys
from optparse import OptionParser

dlm = "        "
ept = ""

class comm:
    def __init__(self, args, opt1, opt2, commonP, unsortF):
        if args[0] == "-":
            self.lines1 = sys.stdin.readlines()
        else:
            file1 = open(args[0], 'r')
            self.lines1 = file1.readlines()
            file1.close()

        if args[1] == "-":
            self.lines2 = sys.stdin.readlines()
        else:
            file2 = open(args[1], 'r')
            self.lines2 = file2.readlines()
            file2.close()

        self.opt1 = opt1
        self.opt2 = opt2
        self.commonP = commonP
        self.unsorted = unsortF
        self.lines1 = self.outputS(self.lines1)
        self.lines2 = self.outputS(self.lines2)

    def outputS(self, file):
        if not len(file):
            file.append("\n")
        else:
            tmp = file[-1]
            newL = "\n"
            if newL not in tmp:
                tmp += newL
            file[-1] = tmp
        return file

    def optLines(self, line, optC):
        stream = ""
        if optC == 1:
            if not self.opt1:
                return
        elif optC == 2:
            if not self.opt2:
                return
            if self.opt1:
                stream += dlm
        elif optC == 3:
            if not self.commonP:
                return
            if self.opt1:
                stream += dlm
            if self.opt2:
                stream += dlm
        else:
            sys.stderr.write("incorrect argument for suppressing\n")
        sys.stdout.write(stream + line)

    def issorted(self):
        sorted_line1, sorted_line2 = sorted(self.lines1), sorted(self.lines2)
        Fsorted = True

        if sorted_line1 != self.lines1:
            Fsorted = False
            sys.stderr.write("FILE1 not sorted\n")

        if sorted_line2 != self.lines2:
            Fsorted = False
            sys.stderr.write("FILE2 not sorted\n")
        return Fsorted

    def make_compare(self):
        if self.unsorted:
            diff2 = self.lines2
            for line1 in self.lines1:
                if line1 not in self.lines2:
                    self.optLines(line1, int(1))
                else:
                    self.optLines(line1, int(3))
                    diff2.remove(line1)

            for line2 in diff2:
                self.optLines(line2, int(2))
            return

        if not self.issorted():
            return

        i, j = 0, 0
        len_line1, len_line2 = len(self.lines1), len(self.lines2)

        while i in range(len_line1) or j in range(len_line2):
            line1,line2 = ept, ept

            if i < len_line1:
                line1 = self.lines1[i]
            if j < len_line2:
                line2 = self.lines2[j]

            if line1 == ept or (line2 != ept and line1 > line2):
                self.optLines(line2, 2)
                j += 1
            elif line2 == ept or line1 < line2:
                self.optLines(line1, 1)
                i += 1
            else:
                self.optLines(line2, 3)
                i += 1
                j += 1
        return

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2
Compare files FILE1 and FILE2 line by line.
When FILE1 or FILE2 (not commonP) is -, read standard input.
"""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-1", "--nofile1",
                      action="store_false", dest="opt1", default=True,
                      help="suppress column 1 (lines unique to FILE1)")
    parser.add_option("-2", "--nofile2",
                      action="store_false", dest="opt2", default=True,
                      help="suppress column 2 (lines unique to FILE2)")
    parser.add_option("-3", "--nocommon",
                      action="store_false", dest="commonP", default=True, help=
                      "suppress column 3 (lines that appear in commonP files)")
    parser.add_option("-u", "--unsorted",
                      action="store_true", dest = "unsortF",
                      default=False, help="work with unsorted files")
    options, args = parser.parse_args(sys.argv[1:])

    try:
        opt1 = bool(options.opt1)
    except:
        parser.error("invalid argument for -1: {0}".
                     format(options.opt1))
    try:
        opt2 = bool(options.opt2)
    except:
        parser.error("invalid argument for -2: {0}".
                     format(options.opt2))
    try:
        commonP = bool(options.commonP)
    except:
        parser.error("invalid argument for -3: {0}".
                     format(options.commonP))
    try:
        unsortF = bool(options.unsortF)
    except:
        parser.error("invalid argument for -u --unsorted: {0}".
                     format(options.unsortF))

    if len(args) != 2:
        parser.error("missing operand")

    if args[0] == "-" and args[0] == args[1]:
        parser.error("only one file can be read from standard input")

    try:
        generator = comm(args, opt1, opt2, commonP, unsortF)
    except OSError as err:
        parser.error("OS Error: {0}".format(err))
    try:
        generator.make_compare()
    except:
        parser.error("error")

if __name__ == "__main__":
    main()
