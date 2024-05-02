import time
import random
from termcolor import colored


redo = ""
words = [
    'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he',
    'was', 'for', 'on', 'are', 'with', 'as', 'his', 'they', 'be', 'at', 'one',
    'have', 'this', 'from', 'or', 'had', 'by', 'hot', 'but', 'some', 'what',
    'there', 'we', 'can', 'out', 'other', 'were', 'all', 'your', 'when', 'up',
    'use', 'word', 'how', 'said', 'an', 'each', 'she', 'which', 'do', 'their',
    'time', 'if', 'will', 'way', 'about', 'many', 'then', 'them', 'would',
    'write', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see',
    'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did',
    'my', 'sound', 'no', 'most', 'number', 'who', 'over', 'know', 'water',
    'than', 'call', 'first', 'people', 'may', 'down', 'side', 'been', 'now',
    'find', 'any', 'new', 'work', 'part', 'take', 'get', 'place', 'made',
    'live', 'where', 'after', 'back', 'little', 'only', 'round', 'man', 'year',
    'came', 'show', 'every', 'good', 'me', 'give', 'our', 'under', 'name',
    'very', 'through', 'just', 'form', 'much', 'great', 'think', 'say', 'help',
    'low', 'line', 'before', 'turn', 'cause', 'same', 'mean', 'differ', 'move',
    'right', 'boy', 'old', 'too', 'does', 'tell', 'sentence', 'set', 'three',
    'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home',
    'read', 'hand', 'port', 'large', 'spell', 'add', 'even', 'land', 'here',
    'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men',
    'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture',
    'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near',
    'build', 'self', 'earth', 'father', 'head', 'stand', 'own', 'page',
    'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still',
    'learn', 'plant', 'cover', 'food', 'sun', 'four', 'thought', 'let', 'keep',
    'eye', 'never', 'last', 'door', 'between', 'city', 'tree', 'cross',
    'since', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw',
    'left', 'late', 'run', 'while', 'press', 'close', 'night', 'real', 'life',
    'few', 'stop', 'open', 'seem', 'together', 'next', 'white', 'children',
    'begin', 'got', 'walk', 'example', 'ease', 'paper', 'often', 'always',
    'music', 'those', 'both', 'mark', 'book', 'letter', 'until', 'mile',
    'river', 'car', 'feet', 'care', 'second', 'group', 'carry', 'took', 'rain',
    'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'north',
    'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face',
    'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready',
    'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon',
    'body', 'dog', 'family', 'direct', 'pose', 'leave', 'song', 'measure',
    'state', 'product', 'black', 'short', 'numeral', 'class', 'wind',
    'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order',
    'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass', 'farm', 'top',
    'whole', 'king', 'size', 'heard', 'best', 'hour', 'better', 'during',
    'hundred', 'am', 'remember', 'step', 'early', 'hold', 'west', 'ground',
    'interest', 'reach', 'fast', 'five', 'sing', 'listen', 'six', 'table',
    'travel', 'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward',
    'war', 'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person',
    'money', 'serve', 'appear', 'road', 'map', 'science', 'rule', 'govern',
    'pull', 'cold', 'notice', 'voice', 'fall', 'power', 'town', 'fine',
    'certain', 'fly', 'unit', 'lead', 'cry', 'dark', 'machine', 'note', 'wait',
    'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'correct',
    'able', 'pound', 'done', 'beauty', 'drive', 'stood', 'contain', 'front',
    'teach', 'week', 'final', 'gave', 'green', 'oh', 'quick', 'develop',
    'sleep', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind',
    'clear', 'tail', 'produce', 'fact', 'street', 'inch', 'lot', 'nothing',
    'course', 'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide',
    'surface', 'deep', 'moon', 'island', 'foot', 'yet', 'busy', 'test',
    'record', 'boat', 'common', 'gold', 'possible', 'plane', 'age', 'dry',
    'wonder', 'laugh', 'thousand', 'ago', 'ran', 'check', 'game', 'shape',
    'yes', 'hot', 'miss', 'brought', 'heat', 'snow', 'bed', 'bring', 'sit',
    'perhaps', 'fill', 'east', 'weight', 'language', 'among'
]
words_set = set(words)


def mode_select():
  mode = input("Input 'words' or 'zen': ")
  return (mode)


def make_length():
  length = int(input("Input the length: "))
  return (length)


def make_text(length):
  text = []
  characters = 0
  for i in range(length):
    random_int = random.randint(0, (len(words)) - 1)
    text.append(words[random_int])
  for i in range(len(text)):
    for x in range(len(text[i])):
      characters += 1
  return (text, characters)


def mode_words(text, characters):
  errors = 0
  proceed = input("Timer will commence immediately after you press enter:")
  print("")
  print(*text)
  start = time.time()
  answer = list(map(str, input().split()))
  end = time.time()
  duration = end - start
  if len(answer) > len(text):
    ite = len(text)
  else:
    ite = len(answer)
  for i in range(ite):
    if answer[i] == text[i]:
      continue
    else:
      for x in range(ite):
        if answer[x] != text[x]:
          errors += 1
  cps = (characters - errors) / duration
  wpm = round((cps * 60) / 5)
  if wpm < 40:
    wpm_line_color = "on_red"
  elif wpm >= 40:
    wpm_line_color = "on_yellow"
  elif wpm > 60:
    wpm_line_color = "on_green"
  else:
    wpm_line_color = "on_blue"

  acc = round((100 * (characters - errors) / characters))
  if acc < 60:
    acc_line_color = "on_red"
  if acc >= 60 and acc < 80:
    acc_line_color = "on_yellow"

  if acc >= 80 and acc < 100:
    acc_line_color = "on_green"
  if acc >= 100:
    acc_line_color = "on_blue"
  print("")
  print("STATS:")
  print("WPM:", colored("  ", "grey", wpm_line_color), wpm)
  print("ERRORS:", errors)
  print("Accuracy:", colored("  ", "grey", acc_line_color), acc)
  print("")


def mode_zen():
  inwords = 0
  characters = 0
  s = ""
  foundwords = []
  proceed = input("Timer will commence immediately after you press enter:")
  start = time.time()
  answer = list(map(str, input().split()))
  end = time.time()
  duration = end - start
  length = len(answer)
  for i in answer:
    characters += len(i)
    if i in words_set:
      inwords += 1
      foundwords.append(i)
  print("")
  cps = characters / duration
  wpm = round((cps * 60) / 5)
  if wpm < 40:
    wpm_line_color = "on_red"
  elif wpm >= 40:
    wpm_line_color = "on_yellow"
  elif wpm > 60:
    wpm_line_color = "on_green"
  else:
    wpm_line_color = "on_blue"
  for i in range(len(foundwords)):
    s += foundwords[i]
    if i != len(foundwords) - 1:
      s += ","
      s += " "
    if i == len(foundwords) - 1:
      s += "."
  print("STATS:")
  print("WPM:", colored("  ", "grey", wpm_line_color), wpm)
  print("FOUND WORDS:", inwords)
  if len(s) > 0:
    print("FOUND:", s)


mode = mode_select()
while True:
  if mode == "words":
    redo = "l"
    while mode == "words":

      if redo == "l":
        length = make_length()
        text, characters = make_text(length)
        mode_words(text, characters)
        redo = input(
            'Input "r" to redo same text, "l" to reselect length, "t" for another text and "m" for mode:'
        )
      elif redo == "r":
        mode_words(text, characters)
        redo = input(
            'Input "r" to redo same text, "l" to reselect length, "t" for another text and "m" for mode:'
        )
      elif redo == "t":
        text, characters = make_text(length)
        mode_words(text, characters)
        redo = input(
            'Input "r" to redo same text, "l" to reselect length, "t" for another text and "m" for mode:'
        )
      else:
        mode = mode_select()
  elif mode == "zen":
    while mode == "zen":
      mode_zen()
      redo = input('Input "t" to restart zen, "m" to go back to menu.')
      if redo == "t":
        continue
      else:
        mode = mode_select()
