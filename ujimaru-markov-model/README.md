# Ujimaru Markov Model

easy ujimaru(uzimaru0000 like) text generator.

Language model file inclued.

## Example

```python
ujimaru = Ujimaru()
#
print(ujimaru.make_sentence())
# 京都行かない方が良さげかな...おらもポテチ食べたい...
print(ujimaru.make_tweet()) # A sentence of 140 characters or less
# 検索しても無限にredux-thunkが出てきて「なっっっっつ」ってなったけど0.1.0のtagを打ったらちゃんとブランチ分けます
```

## What is this

see [うじまる生誕LT会](https://zli.connpass.com/event/176933/)

## Used

Text is generated from third order markov chain model based on some twitter users' tweets.

Using [markovify](https://github.com/jsvine/markovify)