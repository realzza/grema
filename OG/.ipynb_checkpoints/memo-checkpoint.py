import pandas as pd
import numpy as np
from WordReader import WordReader
import argparse
import os
from time import localtime, strftime 

def parse_args():
    desc = "parse args for the memorizing task"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--preview', type=int, default=10)
    parser.add_argument('--count', type=int, default=300)
    parser.add_argument('--reset', type=bool, default=False)
    parser.add_argument('--update', type=bool, default=True)
    parser.add_argument('--log', type=str, default='../2.新GRE官方词汇/分list Excel版 （每天300）/notes/')
    return parser.parse_args()
    
args = parse_args()
day = args.day
preview = args.preview
if day < 12:
    wordlist_name = "Day %d list%d-%d.xlsx"%(day,3*day-2,3*day)
elif day == 12:
    wordlist_name = "Day 12 list34-35.xlsx"
    
all_words = pd.read_excel(wordlist_name)
print("... Wordlist %d loaded ...")
print(all_words.head(preview))

words_count = args.count
reset = args.reset
if reset:
    make_sure = input('Are you sure to wipe memo history out? (Y/n)\n')
    if make_sure.lower() == 'y':
        all_words['count'].values[:] = 0
        all_words.to_excel(wordlist_name, index=False)
    else:
        pass
print('... memorizing %d words ...'%len(all_words))
words_container = WordReader(wordlist_name)
words_container.memorize(words_count)
update = args.update
if update:
    notes_dir = args.log
    if not os.path.isdir(notes_dir):
        os.mkdir(notes_dir)
    words_container.update_excel()
    all_words = pd.read_excel(wordlist_name)
    time_str = strftime("%Y-%m-%d %H%M%S-", localtime())
    if not os.path.isdir(notes_dir+time_str.split()[0]):
        os.mkdir(notes_dir+time_str.split()[0])
    html_name = time_str.split()[1]+'Day%d.html'%day
    html_script = all_words.to_html().replace('<thead>','<meta http-equiv="content-Type" content="text/html; charset=UTF-8" /><thead>')
    with open(notes_dir+time_str.split()[0]+'/'+html_name,'w',encoding="UTF-8") as f:
        f.write(html_script.replace('\\n',''))
#     all_words.to_html(notes_dir+html_name,encoding="utf-8")
    print('... Updated! ...')
print('... Done & Congrats ...')