# subreddit_nlp

### Python tool: Parse and examine NLP diagnostics from subreddit titles

This tool allows users to retrieve the 'n' posts from a given subreddit's post titles in order to examine NLP metrics.  For example you can return a sentiment score for each title and plot the distribution of sentiment scores for all posts retrieved.  The user can also return the 'p' most common words or nouns from the retrieved posts.

**Arguments** <br>
`-id`
- The client id required by PRAW's OAUTH2 client   <br>

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
- *default: retrieve posts by top of all time* <br>

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


