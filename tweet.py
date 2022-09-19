"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet('ABCDEFGHIJKLMNOPQRSTUVWXYZ'* 2) 
    False

    """
    return len(text) >= 1 and len(text) <= MAX_TWEET_LENGTH


def compare_tweet_lengths(text1: str, text2: str) -> int:
    """Returns 1 if text1 is longer than text2. Returns -1 if text2 is longer
    than text1. Returns 0 if both texts have same length.
    
    Precondition: text1 and text2 are both valid tweets
    
    >>> compare_tweet_lengths('hi', 'hello')
    -1
    >>> compare_tweet_lengths('cat', 'dog')
    0
    """
    if len(text1) == len(text2):
        return 0
    elif len(text1) > len(text2):
        return 1
    else:
        return -1

#do we still add hashtag if there is a # in tweet?
def add_hashtag(tweet: str, tweet_word: str) -> str:
    """ Return potential tweet appended a space, hash symbol, and the tweet word
    if the potential tweet is a valid tweet. Otherwise, return original tweet.
    
    Precondition: tweet and tweet_word are both valid tweets.
    
    >>> add_hashtag ('I like', 'kendo')
    ' like #kendo'
    >>> add_hashtag ('Never give up'*5, 'Shuai')
    'Never give upNever give upNever give upNever give upNever give up'
    """
    potential_tweet = tweet + SPACE + HASHTAG_SYMBOL + tweet_word
    
    if is_valid_tweet(potential_tweet):
        return potential_tweet
    else:
        return tweet


def contains_symbol(tweet: str, tweet_word: str, symbol: str) -> bool:
    """Returns true iff tweet contains exactly the tweet_word with symbol before 
    exactly the tweet_word
    
    Precondition: tweet and tweet_word are both valid tweets.
    
    >>> contains_symbol('My lastname Zhu sounds like #zoo', 'zoo', '#')
    True
    >>> contains_symbol('My lastname Zhu sounds like @zoo', 'zo', '@')
    False
    """
    
    #In order for a string to be a valid hashtag or mention, #/@ must begin 
    #with #/@ and contains all alphanumeric characters and underscores up to
    #the following non-alphanumeric character(excluded).
    #Cleaning the tweet removes all non-alphanumeric characters and adding a
    #space to get all the alphanumeric characters after the symbols
    
    tweet = clean(tweet) + SPACE
    tweet_word = symbol + tweet_word + SPACE
    return tweet_word in tweet


def contains_hashtag(tweet: str, tweet_word: str) -> bool:
    """Returns true iff tweet contains exactly the tweet_word with hashtag 
    symbol before exactly the tweet_word
    
    Precondition: tweet and tweet_word are both valid tweets.
    
    >>> contains_hashtag('My lastname Zhu sounds like #zoo', 'zoo')
    True
    >>> contains_hashtag('My lastname,./,./. Zhu sounds like #zoo', 'zoo~')
    False
    """
    return contains_symbol(tweet, tweet_word, HASHTAG_SYMBOL)
    
    
def is_mentioned(tweet: str, tweet_word: str) -> bool:
    """Returns true iff tweet contains exactly the tweet_word with mention 
    symbol before exactly the tweet_word
    
    Precondition: tweet and tweet_word are both valid tweets.
    
    >>> is_mentioned('My lastname Zhu sounds like @zoo', 'zoo')
    True
    >>> is_mentioned('My lastname,./,./. Zhu sounds like @zoo', 'zoo~')
    False
    """
    return contains_symbol(tweet, tweet_word, MENTION_SYMBOL)    


def add_mention_exclusive(tweet: str, tweet_word: str) -> str:
    """Return the potential_tweet iff mention symbol is not already contained
    in tweet and the tweet_word is contained in tweet
    
    Precondition: tweet and tweet_word are both valid tweets.
    
    >>> add_mention_exclusive('@shuai zhu', 'shuai')
    '@shuai zhu'
    >>> add_mention_exclusive('shuai zhu', 'zoo')
    'shuai zhu'
    >>> add_mention_exclusive('shuai zhu', 'zhu')
    'shuai zhu @zhu'
    """
    
    # what if tweet contains many punctuations? any requirements?
    potential_tweet = clean(tweet) + SPACE + MENTION_SYMBOL + tweet_word
    
    # If mention symbold is already in tweet, no need to add the mention symbol
    if MENTION_SYMBOL in tweet:
        return tweet
    # only return potential_tweet when potential_tweet  is a valid tweet
    # and if tweet_word is in tweet
    elif is_valid_tweet(potential_tweet) and tweet_word in tweet:
        return potential_tweet   
    else:
        return tweet
    
    
def num_tweets_required(tweet: str) -> int:
    """Return the minimum number of tweets required to post the entire message
    
    Precondition: tweet is a valid tweet.
    
    >>> num_tweets_required('I like python')
    1
    >>> num_tweets_required('I like python'*100)
    26
    """
    return math.ceil(len(tweet)/MAX_TWEET_LENGTH)

    
def get_nth_tweet(message: str, n: int) -> str:
    """ Return tweet with index n
    Precondition: message is a valid tweet and n >= 0
    
    >>> get_nth_tweet('ABCDE' * 100, 0)
    'ABCDE'*10
    >>> get_nth_tweet('ABCDE' * 10, 100)
    ''
    """
    return message[MAX_TWEET_LENGTH * n:MAX_TWEET_LENGTH * (n + 1)]  
    

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
