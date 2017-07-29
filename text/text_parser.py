from nltk import word_tokenize

def vocab_maker(sentences):
  '''
  This function makes the entire vocabulary of the sentences given along with converting
  all the sentences in tokens.
  Args:
    sentences: a list of sentences that need to be processed.
  Returns:
    vocab: a list of all the words in sorted order
    sent_all: a list of all the tokenized sentences
  '''
  vocab = []
  sent_all = []
  for sentence in sentences:
    tokens = word_tokenize(sentence)
    vocab.extend(tokens)
    sent_all.append(tokens)
  
  # making the vocab
  vocab = sorted(list(set(tokens_all)))
  
  return vocab, sent_all

def make_vector(sentences, word2id):
  '''
  A function which converts the input sentences into vectors according to the dictionary
  Args:
    sentences: a list of sentences which are tokenized
    word2id: a dictionary which has the values assigned to each word
  Returns:
    tot_line: a list of all the sentences in which words are converted to corresponding values
  '''
  
  tot_line = []
  for s in sentences:
    # s already tokenized
    line = []
    for t in s:
      line.append(word2id(t))
    tot_line.append(line)
    
  return tot_line

def padding_(input_, maxlen = None, pad_val = 0):
  '''
  This function pads the input to the maxlen and fills with pad_val
  Args:
    input_: the input sentences
    maxlen: the length to which the sentence are to be padded
    pad_val: the value to the filled in padding
  Returns:
    sent_: a list of sentences which have been padded with
      pad_val upto length maxlen
  '''
  lenlist = []
  for s in input_:
    lenlist.append(len(s))
  maxlen_ = max(lenlist)
  
  if maxlen == None:
    maxlen = maxlen_
  elif maxlen < maxlen_:
    raise ValueError("Padding Length Error: should be: {0}, given length: {1}".format(maxlen_, maxlen))
    
  sent_ = []
  for line in input_:
    s = line
    linelen = len(line)
    for _ in range(maxlen - linelen):
      # add padding value
      s.insert(0, pad_val)
    sent_.append(s)
  
  return sent_
  
def get_data(path, padding = True, maxlen_pad = None, pad_val = 0):
  '''
  This function will process the data in path
  Args:
    path: the path to the file
    padding: whether to do padding
    maxlen_pad: maximum length to pad with
    pad_val: the value to be padded with
  Returns:
    sentences: the processed sentences
    word2id: dictionary which has ID for every word
    id2word: dicitonary which has word for every ID
  '''
  # get sentences
  sentences = open(path)
  sentences = sentences.readlines()
  
  # make the vocabulary and convert sentences to tokens
  vocab, sentences = vocab_maker(sentences)
  
  # Adding PAD value as the first element in vocabulary
  vocab.insert(0, '$$_PAD')
  
  # making a word2id and id2word dictionaries
  word2id = dict((c, i) for i, c in enumerate(vocab))
  id2word = dict((i, c) for i, c in enumerate(vocab))
  
  # converting the sentences to vectors
  sentences = make_vector(sentences, word2id)
  
  # if padding is required
  if padding == True:
    sentences = padding_(input_ = sentences, maxlen = maxlen_pad, pad_val = pad_val)
    return sentences, word2id, id2word
  
  return sentences, word2id, id2word
