#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:09:25 2019

@author: nidhi rastogi
"""
import csv

term = []
label = []
narrower = []
broader = []
line_count = 0
allTokensDict = {}
allTokensList = []
        
def ingestor():

    file = '../data_ingestion/MeSH/output/mesh_labels_narrower_broader.csv'
    line_count = 0
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = '\n')

        
        for column in csv_reader:
            if line_count == 0:
                print(f'Column names are {"[, .]".join(column)}')
               
                line_count += 1
            elif line_count <30:
                for row in column:
                    if '|' in row:
                        lst = row.split("|")
                        stringcount = len(lst)
                        if stringcount == 4:
                            #print (row)
                            term.append(lst[0].strip())
                            #print(lst[0].strip())
                            #allTokens.add(lst[0].strip())
                            
                            label.append(lst[1].strip())
                            #print(lst[1].strip())
                            allTokensDict[lst[1].strip()] = lst[0].strip()
                            allTokensList.append(lst[1].strip())
                            
                            narrower.append(lst[2].strip())
                            #print(lst[2].strip())
                            allTokensDict[lst[2].strip()] = lst[0].strip()
                            allTokensList.append(lst[2].strip())
                            
                            broader.append(lst[3].strip())
                            #print(lst[3].strip())
                            allTokensDict[lst[3].strip()] = lst[0].strip()
                            allTokensList.append(lst[3].strip())
                            #print(line_count, f'\t{term} {label} {narrower} {broader}')
                #print(column)
                line_count += 1
 



def returnListMesh():
    ingestor()
    #print (allTokensList)
    return allTokensList

def returnDictMesh():
    ingestor()
    #print(allTokensDict)
    return allTokensDict
        
        #for key,val in allTokens.items():
         #   print (key,':', val)
    
    #for x in 
    #print(f'Processed {line_count} lines.')
    
returnListMesh()
#returnDictMesh()