from transformers import pipeline
import spacy
import neuralcoref

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
nlp = spacy.load("en_core_web_sm")

# Add neural coref to SpaCy's pipe
neuralcoref.add_to_pipe(nlp)

with open('HP-Wikipedia.txt') as f:
    sentences = [line.rstrip() for line in f if len(line.split())>0 and line.split()[-1][-1]=="."]
#sentences=filter(None, sentences)

summarized=[]

for sent in sentences:
    leng = len(sent.split())
    print(sent)
    min=1
    summary=summarizer(sent, max_length=2*leng, min_length=min, do_sample=False)
    text=summary[0]
    text=text.get('summary_text')
    doc = nlp(text)
    text=doc._.coref_resolved
    #print(text)
    summarized.append(text)

with open('summary_no_titles.txt', 'w') as f:
    for sum in summarized:
        f.write(sum)
        f.write('\n')
        f.write('\n')

