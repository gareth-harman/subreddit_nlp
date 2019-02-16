import praw
import spacy as sp
from collections import Counter
from afinn import Afinn
import numpy as np
import seaborn as sns
import argparse


###############################################################################
# Argparser
###############################################################################

def parse_args():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-id')
    parser.add_argument('-secret')
    parser.add_argument('-user_agent')
    parser.add_argument('-username')
    parser.add_argument('-subreddit', default = 'gradschool')
    parser.add_argument('-sort_by_top', default = True)
    parser.add_argument('-n_posts', default = 100)
    parser.add_argument('-en_path', default = 'en_core')
    
    args = parser.parse_args()
    
    return args

    
###############################################################################
# Scrape reddit
###############################################################################

def scrape_reddit(id_val,
                  secret_val,
                  user_agent_val,
                  username_val,
                  sub_reddit, 
                  lim_val, 
                  by_top):
    
    print('Scraping {} for {} posts...'.format(sub_reddit, lim_val))
    
    reddit = praw.Reddit(client_id = id_val,
                         client_secret = secret_val,
                         user_agent = user_agent_val,
                         username = username_val)
    
    lim_val = int(lim_val) # Recast as integer for use with bash scripting
    
    if by_top != 0:
        print('\tretrieving by top of all time')
        submissions = list(reddit.subreddit(sub_reddit).top(time_filter = 'all', limit=lim_val))

    else:
        print('\tretrieving by new')
        submissions = list(reddit.subreddit(sub_reddit).new(limit=lim_val))
    
    return submissions

###############################################################################
# Process reddit results    
###############################################################################    

def proc_text(submissions, do_freq=False):
    
    print('Processing reddit data...')
    
    titles = [(x.title).lower() for x in submissions]
    doc = [nlp(x) for x in titles]
    
    if do_freq:
        
        all_words = ''
        
        for ii in titles:
            all_words += ' ' + ii
            
        all_words = nlp(all_words)
        
        words = [token.text for token in all_words if token.is_stop != True and token.is_punct != True]
        nouns = [token.text for token in all_words if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]
    
        return titles, doc, words, nouns
    
    else:
        return titles, doc


###############################################################################
# Return most common words and nouns
###############################################################################    

def get_freqs(words, nouns, n_words):
    
    print('Returning frequent words...')
    
    word_freq = Counter(words)
    noun_freq = Counter(nouns)
     
    common_nouns = noun_freq.most_common(n_words)
    common_words = word_freq.most_common(n_words)

    return common_nouns, common_words

###############################################################################
# Compute sentiment analysis   
###############################################################################    

def sent_proc(titles):
    
    af = Afinn() # Load library
    
    # afinn sentiment scores
    sentiment_scores_af = [af.score(article) for article in titles]
    
    return np.array(sentiment_scores_af)

if __name__ == "__main__":

    ###########################################################################
    # Parse arguments
    ###########################################################################
    
    args = parse_args()
        
    ###########################################################################
    # Try and load the spacey core NLP library
    ###########################################################################
    
    try:
        nlp = sp.load(args.en_path)
    except:
        print('ERROR: Unable to load spacey core NLP library check "en_path" arg')
        print('\ten_path must be the name of the spacey core library or the path to this library folder')
    
    ###########################################################################
    # Scrape the subreddit 
    ###########################################################################
    
    submissions = scrape_reddit(args.id,
                                args.secret,
                                args.user_agent,
                                args.username,
                                args.subreddit, 
                                args.n_posts,
                                args.sort_by_top)
    
    ###########################################################################
    # Process the scraped data
    ###########################################################################
    
    titles, doc, words, nouns = proc_text(submissions, True)

    ###########################################################################
    # Process the word frequencies
    ###########################################################################
    
    cmn_nouns, cmn_words = get_freqs(words, nouns, 10)
    
    for ii in cmn_nouns:
        print(ii)
        
    ###########################################################################
    # Get sentiment analysis via afinn
    ###########################################################################
    
    sent_af = sent_proc(titles)
    sent_sum = [1 if score > 0 else -1 if score < 0 else 0 for score in sent_af]
    
    sns.distplot(np.array(sent_sum))
   
