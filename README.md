# BART (large-sized model), fine-tuned on CNN Daily Mail

BART is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder. BART is pre-trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text.
BART is particularly effective when fine-tuned for text generation (e.g. summarization, translation) but also works well for comprehension tasks (e.g. text classification, question answering). This particular checkpoint has been fine-tuned on CNN Daily Mail, a large collection of text-summary pairs.

It was introduced in the paper BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension by Lewis et al. and first released in this repository (https://github.com/pytorch/fairseq/tree/master/examples/bart).

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

- https://arxiv.org/abs/1910.13461

## Cite
```
@article{lewis2019bart,
    title = {BART: Denoising Sequence-to-Sequence Pre-training for Natural
Language Generation, Translation, and Comprehension},
    author = {Mike Lewis and Yinhan Liu and Naman Goyal and Marjan Ghazvininejad and
              Abdelrahman Mohamed and Omer Levy and Veselin Stoyanov
              and Luke Zettlemoyer },
    journal={arXiv preprint arXiv:1910.13461},
    year = {2019},
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

# sentence-transformers/paraphrase-MiniLM-L6-v2

This is a sentence-transformers model: it maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search. SentenceTransformers is a Python framework for state-of-the-art sentence, text and image embeddings. The initial work is described in the paper "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks". You can use this framework to compute sentence / text embeddings for more than 100 languages. These embeddings can then be compared e.g. with cosine-similarity to find sentences with a similar meaning. This can be useful for **semantic textual similar**, semantic search, or paraphrase mining.

## Cite

```
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "http://arxiv.org/abs/1908.10084",
}
```