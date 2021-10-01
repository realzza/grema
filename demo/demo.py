import sys
sys.path.append("..")
import pandas as pd
import numpy as np
from OG.WordReader import WordReader
import argparse
import os
from time import localtime, strftime

def parse_args():
  desc = "parse args for memorizing gre words"
  parser = argparse.ArgumentParser(description=desc)
  parser.add_argument('--preview', type=int, default=10, help="peek words from list [default: 10]")
  parser.add_argument('--reset', action='store_true', default=False, help="reset learning history with CAUTION [default: False]")
  parser.add_argument('--update', action='store_true', default=True, help="Want the learning history to be updated or not? [default: True]")
  parser.add_argument('--log', type=str, default="./notes/", help="directory to restore generated learning notes [default: ./notes/]")
  return parser.parse_args()

def regularizeDirectory(someDir):
  return someDir.rstrip("/")+'/'

def selectBase(base):
  if base == "og":
    return "OG/", 12
  else:
    return "ynm/", 10

if __name__ == "__main__":

  # parse args
  args = parse_args()

  # check if preview/peek required
  preview = args.preview
  wordListName = "demo.xlsx"
  allWords = pd.read_excel(wordListName)
  print("... demo wordlist loaded ...")
  print(allWords.head(preview))

  # check if reset requested
  isReset = args.reset
  if isReset:
    makeSureNotice = input('Are you sure to wipe memo history out? (Y/n)\n')
    if makeSureNotice.lower() == 'y':
      allWords['count'].values[:] = 0
      allWords.to_excel(wordListName, index=False)
    else:
      pass

  # notifying wordlist info 
  print('... memorizing %d words ...'%len(allWords))
  
  # start memorizing this wordlist
  wordsCount = len(allWords)
  wordsContainer = WordReader(wordListName, allWords)
  wordsContainer.memorize(wordsCount)

  # decide to update files that records learning history or not
  isUpdate = args.update
  if isUpdate:
    saveDir = regularizeDirectory(args.log)
    os.makedirs(saveDir, exist_ok=True)
    wordsContainer.update_excel()
    
    # output learning history to html file
    allWords = pd.read_excel(wordListName)
    timeTag = strftime("%Y-%m-%d %H%M%S-", localtime())

    # create a folder for each day, highligh
    os.makedirs(saveDir+timeTag.split()[0], exist_ok=True)
    htmlName = timeTag.split()[1]+"demo.html"
    htmlScript = allWords.to_html().replace('<thead>','<meta http-equiv="content-Type" content="text/html; charset=UTF-8" /><thead>')

    # write to files
    with open(saveDir+timeTag.split()[0]+'/'+htmlName, 'w', encoding="UTF-8") as f:
      f.write(htmlScript.replace("\\n",""))
    print("... Updated! ...")
  print("... Done & Congrats ...")