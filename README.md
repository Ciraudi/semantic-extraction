# Python3 wrapper for Text Summarization module
![Stanford NLP Wrapper CI](https://github.com/philipperemy/Stanford-OpenIE-Python/workflows/Stanford%20NLP%20Wrapper%20CI/badge.svg)

Open information extraction (open IE) refers to the extraction of structured relation triples from plain text, such that the schema for these relations does not need to be specified in advance. For example, Barack Obama was born in Hawaii would create a triple `(Barack Obama; was born in; Hawaii)`, corresponding to the open domain relation "was born in". CoreNLP is a Java implementation of an open IE system as described in the paper:

More information can be found here : http://nlp.stanford.edu/software/openie.html

The OpenIE library is only available in english: https://stanfordnlp.github.io/CoreNLP/human-languages.html

## Installation and usage

You need python3, venv and pip installed.
Summarizer uses neuralcoref library, which needs spacy 2.1.0 version. In order to avoid conflict between spacy version with the query module, which requires spacy>=3.x version, it is RECOMMENDED to install all the packages in a virtual environment (i.e. venv), to be used to launch summurizer.py file

```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements_summarizer.txt
python3 -m spacy download en_core_web_sm
```

## References

- https://www.kaggle.com/asitang/stanford-resources
- https://www.kaggle.com/geofila/corenlp?select=stanford-corenlp-full-2018-10-05

## Cite

```
@misc{StanfordOpenIEWrapper,
  author = {Philippe Remy},
  title = {Python wrapper for Stanford OpenIE},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/philipperemy/Stanford-OpenIE-Python}},
}
```

# Python3 wrapper for Stanford OpenIE and Query module
![Stanford NLP Wrapper CI](https://github.com/philipperemy/Stanford-OpenIE-Python/workflows/Stanford%20NLP%20Wrapper%20CI/badge.svg)

Open information extraction (open IE) refers to the extraction of structured relation triples from plain text, such that the schema for these relations does not need to be specified in advance. For example, Barack Obama was born in Hawaii would create a triple `(Barack Obama; was born in; Hawaii)`, corresponding to the open domain relation "was born in". CoreNLP is a Java implementation of an open IE system as described in the paper:

More information can be found here : http://nlp.stanford.edu/software/openie.html

The OpenIE library is only available in english: https://stanfordnlp.github.io/CoreNLP/human-languages.html

## Installation

You need python3, pip and Java installed. Java is used by the CoreNLP library.

```bash
pip install numpy
pip install cython
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm 
pip install -r requirements.txt

```
## References

- https://www.kaggle.com/asitang/stanford-resources
- https://www.kaggle.com/geofila/corenlp?select=stanford-corenlp-full-2018-10-05

## Cite

```
@misc{StanfordOpenIEWrapper,
  author = {Philippe Remy},
  title = {Python wrapper for Stanford OpenIE},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/philipperemy/Stanford-OpenIE-Python}},
}
```