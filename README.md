<p align="center"><img src="images/grema_logo_light.png" alt="GREMA logo" width="55%" height="auto"></p>

## Overview

GREMA is short for **GRE MA**ster. It is a succint CLI that excludes extra distractions and helps users better concentrate.

GREMA currently supports OG/YNM words. For now, the OG words are based on a **12** day scale, and the YNM words are based on a **10** day scale. GREMA supports only Chinese meaning. But it should be easy enough for non-Chinese speakers to customize GREMA and apply different wordlist.

## Install and Get started

Clone this repo to local.

```
git clone git@github.com:ziangzhou-duke/grema.git -b release
```

Install a simple environment to make sure everything is on the same page.

```bash
pip install -r requirements.txt
```

After setting up the environment, you are ready to go! Tryout the demo script and get familiar with how this tool works.

```
cd demo/
python demo.py
```

It should pop up following in the terminal for **preview** purpose

```
... demo wordlist loaded ...
   count        word                    mean
0      0   beleaguer          v. 困扰，骚扰；围困，围攻
1      0     abysmal  adj. 极坏的；糟透的；深重\n的；无边的
2      0     arduous      adj. 艰巨的，费力的；困难\n的
3      0     absolve     v. 免除…的过失;解除…的\n责任：
4      0      anoint                v. 选定，指定
5      0     agility              adj. 敏捷；灵活
6      0  ascendancy            n. 上升统治地位，优势
7      0   avocation                n. 副业，嗜好
8      0     belated            adj. 迟到的，误期的
9      0  abstinence         n. 节制，禁绝（食物或酒精）
... memorizing 18 words ...
0:  beleaguer
```

The first word is _beleaguer_, if you recognize it, type in _yes_ the hit _enter_. If not, hit _enter_ and move on to the next word.

```
... memorizing 18 words ...
0:  beleaguer  yes
v. 困扰，骚扰；围困，围攻

1:  abysmal  yes
adj. 极坏的；糟透的；深重
的；无边的

2:  befuddle
v. 使迷惑；使困惑

3:  balky
adj. 固执的，不听使唤的

4:  aphorism  yes
n.格言；警语
```

After finished memorizing all the words, an ending notice will pop up.

```
Excel update done!
... Updated! ...
... Done & Congrats ...
```

And you will find your memorizing history is ready to be reviewed in the future.

```
notes/someday/xxxxxx.html
```

## Usage

You can start memorizing GRE words by simply running the `memorize.py` script. Check out the properties that may help to get you started.

```
usage: memorize.py [-h] --day DAY [--preview PREVIEW] [--word-base WORD_BASE]
                   [--reset] [--update] [--log LOG]

parse args for memorizing gre words

optional arguments:
  -h, --help            show this help message and exit
  --day DAY             select from 1 to 12
  --preview PREVIEW     peek words from list [default: 10]
  --word-base WORD_BASE
                        choose wordbase og/ynm [default: og]
  --reset               reset learning history with CAUTION [default: False]
  --update              Want the learning history to be updated or not?
                        [default: True]
  --log LOG             directory to restore generated learning notes
                        [default: ./notes/]
```

To start you first memorizing event, use the following command:

```shell
python memorize.py --day 1 --word-base og --log ./notes/
```

## Highlights

- **Accumulative History**: No need to specify the date and each memorizing event. Every memorizing history will be automatically stored in the location that you specified. It will be automatically archived by dates and times.
- **Automatic Ranking**: Unlike many other apps that require manual starring words, or manually increase the importance of every word, GREMA frees you from counting how many times you have forgotten the word. It offers an automatic way to analyze your memorizing history and rank the order of words accordingly for the next memorizing experience.
- **Auto Wordlist Reordering**: The order of each memorizing event will be based on your previous memorizing history. The words of each list will be organized in the order of difficulty, which is automatically calculated from the user's memorizing history.
- **Auto Screen Cleaning**: Clean up the screen automatically to keep your eyesight from keep staring at the bottom of the screen.

## To do

- [x] unify ynm and OG memo script
- [x] add demo file
- [ ] add suggested memo plan to this site.
- [ ] add `clear` operation check for macOS.
- [ ] unify words to a single file. Make the number of each list customizable.
- [ ] Create an API for the `.csv/.xslx` wordlist that can be applied to the memorizing script. Thus can support all languages.
