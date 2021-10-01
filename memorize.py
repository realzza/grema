import pandas as pd
import numpy as np
from utils.WordReader import WordReader
import argparse
import os
from time import localtime, strftime

def parse_args():
  desc = "parse args for memorizing gre words"
  parser = argparse.ArgumentParser(description=desc)
  parser.add_argument("--day", type=int, required=True, help="select from 1 to 12")
  parser.add_argument('--preview', type=int, default=10, help="peek words from list [default: 10]")
  parser.add_argument('--word-base', type=str, default="og", help="choose wordbase og/ynm [default: og]")
  # parser.add_argument('--count', type=int, default=300, help="number of words to memorize from current list")
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

  # check day in range
  thisDay = args.day 

  # load og/ynm 
  plan, planScope = selectBase(args.word_base)
  assert 0< thisDay <= planScope, "choose between day 1 and day %d"%planScope
  
  # load wordlist
  if args.word_base == "og":
    if thisDay < 12:
      wordListName = plan + "Day %d list%d-%d.xlsx"%(thisDay,3*thisDay-2,3*thisDay)
    elif thisDay == 12:
      wordListName = "OG/" + "Day 12 list34-35.xlsx"
  elif args.word_base == "ynm":
    wordListName = plan + "ynm_day%d.xlsx"%(thisDay)

  # check if preview/peek required
  preview = args.preview
  # print(wordListName)
  allWords = pd.read_excel(wordListName)
  print("... Wordlist %d loaded ..."%thisDay)
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
    htmlName = timeTag.split()[1]+"Day%d.html"%thisDay
    htmlScript = allWords.to_html().replace('<thead>','<meta http-equiv="content-Type" content="text/html; charset=UTF-8" /><thead>')

    # write to files
    with open(saveDir+timeTag.split()[0]+'/'+htmlName, 'w', encoding="UTF-8") as f:
      f.write(htmlScript.replace("\\n",""))
    print("... Updated! ...")
  print("... Done & Congrats ...")