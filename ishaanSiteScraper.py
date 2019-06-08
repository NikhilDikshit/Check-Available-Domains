#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:53:05 2019

@author: nikhildikshit
"""

import whois
import enchant
from itertools import product
from string import ascii_lowercase
from time import sleep
print("\n")

def generateAllWords(n):
    listy = [''.join(i) for i in product(ascii_lowercase, repeat = n)]
    print("Total number of words are:", len(listy))
    return listy

def extractOnlyEnglishWords(listy):
    d = enchant.Dict("en_US")
    legitWords = []
    for i in range(len(listy)):
        if d.check(listy[i]) == True:
            legitWords.append(listy[i])
    print("\nTotal words with english meaning:", len(legitWords), "\n")
    return legitWords
        
def desiredTopLevelDomain(legitWords):
    for i in range(len(legitWords)):
        legitWords[i] += ".com"
        finalURLs = legitWords
    return finalURLs
    
def checkForAvailableDomains(finalURLs):
    for domain in finalURLs:
        timeout = 20.0 
        whois.socket.setdefaulttimeout(timeout)
        sleep(2)
        try: 
            site = whois.whois(domain)
            print("Not Available:", site.domain_name)
        except Exception:
            print("Available:", domain)
            f = open('Available Domains.txt', 'a')
            f.write(domain + '\n')
            f.close()
    print("\nCompleted. Check the output file.")

n = 3

listy = generateAllWords(n)
legitWords = extractOnlyEnglishWords(listy)
finalURLs = desiredTopLevelDomain(legitWords)
checkForAvailableDomains(finalURLs)
