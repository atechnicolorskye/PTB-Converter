"""
Tree_Words.py

Description
-----------
Concatenates words processed by pennconverter.jar into sentences

Usage:

Concatenate
-----------
Concatenate('Test.txt')

Si Kai Lee 06/03/2015

"""


import re

def Concatenate(filename):
    F = open(filename, "r")
    Input = F.readlines()
    # print Input
    F.close

    filename =  re.sub('.txt', '', filename)
    G = open(filename+'_p.txt', 'w')

    y = ''
    for z in Input:
        if z == '\n':
            G.write(y + z)
            y = ''
        else:
            y = re.sub('\{|`|\}|\'\'', '', y)
            y += re.search('\\t(.*?)\\t', z).group(1) + ' '

    # for z in Input:
    #     y = re.findall('\s([A-Za-z\.-]*|\W[a-z]{1,}|\d[^A-Za-z)]+|n\'t)\)', z)
    #     G.write(' '.join(y) + '\n')

    G.close()
