import pandas as pd
import os
import time
class WordReader(object):
    
    def __init__(self, excel_path, is_random=False):
        self.excel_path = excel_path
        self.all_words = pd.read_excel(self.excel_path)
        self.words_sorted = self.all_words.sort_values(by=['count'], axis=0, ascending=False)
        self.is_random = is_random
        self.len = len(self.all_words)            
        
    def memorize(self, word_num):
        if word_num > self.len:
            word_num = self.len
        clear_count = 0
        for i in range(word_num):
            if clear_count % 21 == 20:
                time.sleep(1.5)
                os.system('cls')
            clear_count += 1
            word = self.words_sorted.iloc[i,1]
            mean = self.words_sorted.iloc[i,2]
            flag = input(str(i) +':  '+ word + '  ')
            if flag == 'yes':
                print(mean+'\n')
                continue
            elif flag == '':
                print(mean+'\n')
                self.words_sorted.iloc[i,0] += 1
                
    def sorting(self, top=100):
        sorted_ver = self.words_sorted.sort_values(by=['count'], axis=0, ascending=False)
        return sorted_ver.iloc[:top,:]
    
    def update_excel(self):
        sorted_ver = self.words_sorted.sort_values(by=['count'], axis=0, ascending=False)
        sorted_ver.to_excel(self.excel_path, index=False)
        print('Excel update done!')