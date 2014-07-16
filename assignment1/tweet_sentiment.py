import sys
import json as JSON

scores = {}

def hw():
  print "hello world!"

def lines(fp):
  print str(len(fp.readlines()))

def parse_afinn(fp):
  fp.seek(0,0)
  for line in fp:
    term, score  = line.split("\t")
    scores[term] = int(score)

def tweet_score(tweet):
  tweetid = tweet.get('id', 'NULL')
  tweet_text = tweet.get('text', '')
  wscores = [scores.get(word, 0) for word in tweet_text.split()]
  tweet_score = sum(wscores)
  print tweetid, tweet_score

def main():
  afile = open(sys.argv[1])
  tfile = open(sys.argv[2])
  hw()
  lines(afile)
  lines(tfile)

  parse_afinn(afile)

  tfile.seek(0,0)
  for line in tfile:
    tweet = JSON.loads(line)
    tweet_score(tweet)

if __name__ == '__main__':
  main()
