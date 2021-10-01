<!-- ![GREMA LOGO](images/grema_logo.png) -->
<p align="center"><img src="images/grema_logo_light.png" alt="GREMA logo" width="70%" height="auto"></p>

## Overview

What is GREMA, you may be curious. GREMA is actually short for GRE Master. The reason that I wrote this is because I had a hard time memorizing GRE words. I tried tons of methods to memorize words but I just keep forgetting.

I tried using apps like Quizlet, etc. I got easily distracted when I was using the phone. And the least place that anyone could get distracted is the place with the poorest interface - the terminal.

By installing GREMA, you can simply started memorizing GRE words, including OG words and YNM words. These are considered most needed for any GRE tests. For now, the OG words is based on a 12 day scale, and the YNM words are based on a 10 day scale.

There is a suggested plan to arrange your words-memo schedule [link here]. Should you have any questions in using GREMA, please file an issue under this repo, I will get back to you asap.

For now, GREMA supports only Chinese meaning. But it should be easy enough for non-Chinese speakers to customize GREMA and apply different wordlist.

Love yall and best luck in your GRE tests.

## Install and Get started

Install a simple environment to make sure everything is on the same page.

```bash
pip install -r requirements.txt
```

## Usage

You can start memorizing GRE words by simply running the `memorize.py` script. Check out the properties that may help to get you started.

```shell
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

- **Accumulative History**: No need to specify the date and each memorizing event. Every memorizing history will be automatically stored in the location that you specified. It will be automatically archived by dates and time.
- **Automatic Ranking** Unlike many other apps that requires manual starring words, or manually increase the importance of every word, GREMA free you from counting how many times you have forgotten the word. It offers an automatic way to analyze your memorizing history and rank the order of words accordingly for the next memorizing experience.
- **Automatic Reorganization:** The order of each memorizing event will be based on your previous memorizing history. The words of each list will be organized in the order of difficulty, which is automatically calculated from user's memorizing history.

## To do

- [x] unify ynm and OG memo script
- [ ] add `clear` operation check for macOS.
- [ ] unify words to a single file. Make the number of each list customizable.
- [ ] Create an API for the `.csv/.xslx` wordlist that can be applied to the memorizing script. Thus can support all languages.
