# Ujimaru (Happy Birthday uzimaru0000)

This project is a twitter bot like [@uzimaru0000](https://twitter.com/uzimaru0000)

projects:
- Twitter Client (Rust, Kuon)
- Twitter Crawler (Go, anaconda)
- Ujimaru API (Python, flask)
- Ujimaru Markov Experiment(Python, NLP)
- Ujimaru Markov Model (Python, NLP)
- Ujimaru Reformer (Python, NLP)

## Twitter Client

Twitter client implementations for [@ujimaru0000](https://twitter.com/ujimaru0000)

Written in Rust. (Using [Kuon](https://github.com/hppRC/kuon))

### TL;DR

Just below.

```rust
let api: kuon::TwitterAPI = get_api_client().await?;

let endpoint = &std::env::var("UJIMARU_API")?;
let text = reqwest::get(endpoint).await?.text().await?;

api.tweet(&text).await?;
```


## Twitter Crawler

Twitter crawler for collect tweets of uzimaru and other users.

Written in Go. (Using [anaconda](https://github.com/ChimeraCoder/anaconda))


## Ujimaru API

Text generation API for ujimaru.

Written in Python. (Using [markovify](https://github.com/jsvine/markovify) and [ujimaru-markov-model](https://pypi.org/project/ujimaru-markov-model/))

This is a flask application, and deployed on the Cloud Run.


## Ujimaru Markov Experiment

Implementations and experiments.

- build Markov models
- dump models as JSON
- cleansing texts
- library usage tests


## Ujimaru Markov Model

An easy ujimaru(uzimaru0000 like) text generator library.

PyPI: [ujimaru-markov-model](https://pypi.org/project/ujimaru-markov-model/)

This library generates text using a third-order Markov chain.

```
pip install ujimaru-markov-model
```

### Usage

```
# On CLI
ujimaru
# へーー自然を撮るならいいってことか（それはそうなんだけど普通のRTになってるって！
``

or

```python
# In a Python program
# load model (model included).
from ujimaru_markov_model import Ujimaru
ujimaru = Ujimaru()

print(ujimaru.make_sentence())
# なんでかElmでCLI作って得られた知見をいくつかqiitaとかにいれておいてcpすることにします！！
print(ujimaru.make_tweet()) # A sentence of 140 characters or less
# 検索しても無限にredux-thunkが出てきて「なっっっっつ」ってなったけど0.1.0のtagを打ったらちゃんとブランチ分けます
```

## Ujimaru Reformer

A text generation program by [reformer](https://github.com/google/trax/tree/master/trax/models/reformer) and [sentencepiece](https://github.com/google/sentencepiece).


see below
- [https://ai-scholar.tech/articles/treatise/reformer-ai-364](https://ai-scholar.tech/articles/treatise/reformer-ai-364)
- [Reformer: The Efficient Transformer](https://arxiv.org/abs/2001.04451)


### Caution

This program will use your computer resources extremely.  
You should use Google Colaboratory to run this model.

