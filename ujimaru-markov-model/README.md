# Ujimaru Markov Model

An easy ujimaru(uzimaru0000 like) text generator library and a CLI tool using it.

Language model file inclued(28MiB).

## Example

In normal python program.

```python
from ujimaru_markov_model import Ujimaru
ujimaru = Ujimaru()

print(ujimaru.make_sentence())
# なんでかElmでCLI作って得られた知見をいくつかqiitaとかにいれておいてcpすることにします！！
print(ujimaru.make_tweet()) # A sentence of 140 characters or less
# 検索しても無限にredux-thunkが出てきて「なっっっっつ」ってなったけど0.1.0のtagを打ったらちゃんとブランチ分けます
```

## Installation

```
pip install ujimaru-markov-model
```

### Usage

```
ujimaru
# へーー自然を撮るならいいってことか（それはそうなんだけど普通のRTになってるって！
```

## What is this

see [うじまる生誕LT会](https://zli.connpass.com/event/176933/)

## Used

Text is generated from third order markov chain model based on some twitter users' tweets.

Using [markovify](https://github.com/jsvine/markovify)