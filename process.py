from __future__ import print_function
import sys
from nltk.tokenize.moses import MosesTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer

# The MosesTokenizer converts e.g. ampersands to &amp;, and other symbols to HMLT tags
# tokenizer = MosesTokenizer()

# we use the TreebankWordTokenizer instead but that one follows the Penn way of converting
# quotes to `` or '' or parentheses to things like -LRB- 
# We change the regexps to avoid this:
tokenizer = TreebankWordTokenizer()
tokenizer.CONVERT_PARENTHESES = []
tokenizer.ENDING_QUOTES = []
tokenizer.STARTING_QUOTES=[]

## replace a line which only contains </doc> with <SEP_DOC/>
## remove a line which starts with "<doc"
## replace empty lines with "<SEP_SENT/>"
## remove non-empty lines with 0 or one spaces (one or two tokens) 
n = 0
hadsep = False
for line in sys.stdin:
    n = n + 1
    if n % 10000 == 0:
        print("Lines processed: ",n,file=sys.stderr)
    line = line.strip()
    if len(line) == 0:
        if not hadsep: print("\n<SEP_SENT/>")
        hadsep = True
    elif line.startswith("<doc"):
        pass
    elif line.startswith("</doc"):
        print("\n<SEP_DOC/>")
    elif line.count(" ") < 2:
        pass
    else:
        ## do some additional tokenisation 
        line = " ".join(tokenizer.tokenize(text=line))
        print(line.lower(),sep='',end='')
        hadsep = False
