#!/usr/bin/env python


def printTable(table):
    colWidths = [len(max(row, key=lambda x: len(x))) for row in table]
    for j in range(len(table[0])):
        for i in range(len(table)):
            if i == 0:
                print(table[i][j].rjust(colWidths[i]), end=' ')
            else:
                print(table[i][j].ljust(colWidths[i]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
