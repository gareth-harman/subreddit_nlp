# subreddit_nlp

### Python tool: Parse and examine NLP diagnostics from subreddit titles

**Arguments** <br>
`-id`
- The client id required by PRAW's OAUTH2 client <br>
`-secret` 
- The client secret required by PRAW's OAUTH2 client <br>
`-user_agent`
- The user agent id required by PRAW's OAUTH2 client <br>
`-username`
- Your reddit username <br>
`-subreddit`
- The subreddit you want to analyze
- *default: gradschool* <br>
`-sort_by_top`
- If 0 it will retrieve posts by 'new'
- *default: retrieve posts by **top of all time** * <br>
`-n_posts`
- The number of posts to retrieve
- *default: 100* 
- Max = 1000 <br>
`-en_path`
- Path the spacey NLP core library to create nlp objects <br>

**Required Python Libraries**
- [praw](https://praw.readthedocs.io/en/latest/index.html)
- [spacy](https://spacy.io)
- [afinn](https://github.com/fnielsen/afinn)
- numpy
- seaborn


'''
parser = argparse.ArgumentParser()

parser.add_argument('-id')
parser.add_argument('-secret')
parser.add_argument('-user_agent')
parser.add_argument('-username')
parser.add_argument('-subreddit', default = 'gradschool')
parser.add_argument('-sort_by_top', default = True)
parser.add_argument('-n_posts', default = 100)
parser.add_argument('-en_path', default = 'en_core')
'''
