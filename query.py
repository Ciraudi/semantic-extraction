import nltk
from SPARQLWrapper import SPARQLWrapper, JSON
from nltk.corpus import wordnet
import ast
import spacy
from progress.spinner import MoonSpinner

def getURI_spacy(source):
  doc = nlp(source)
  founds=[]
  for ent in doc.ents:
    found_text = ent.text
    found_URI =  ent.kb_id_
    found=found_text + ' - ' + found_URI
    if not found in founds:
      founds.append(found)
  other=getURI(source)
  if other!= ' ' and other not in founds:
    founds.append(other)
  return founds

def getURI(source):
  sparql.setQuery('''
  select distinct ?x {
    ?x a ?type ;
      rdfs:label "%s"@en 
  }
  ''' % source)
  sparql.setReturnFormat(JSON)
  qres = sparql.query().convert()
  result=qres['results']['bindings']
  if len(result) > 0:
    value = source + ' - ' + result[0]['x']['value']
    return value
  else:
    return ' '

def getSense(source):
  syns = wordnet.synsets(source)
  #if at least one verb sense, return it, alse return the first one
  for s in syns:
    tag= s.pos()
    if tag == 'v'  and source[0].islower():
        result=(source + ' - verb: ' + s.definition())
        return result
  if len(syns)!=0 and source[0].islower():
    if syns[0].pos() == 'n':
      tag='noun: '
    elif syns[0].pos() == 'a':
      tag='adjective: '
    else:
      tag='adverb: '
    result = source + ' - '+tag +syns[0].definition()
    return result
  else :
    return " "
  

def substitute_name(sentence):
  words = nltk.word_tokenize(sentence)
  if 'Harry' in words and 'Potter' not in words:
    sentence=''
    for word in words:
      if word == 'Harry':
        word= 'Harry Potter '
      sentence=sentence+word
  return sentence
   

if __name__ == "__main__":
  nlp = spacy.blank('en')
  nlp.add_pipe('dbpedia_spotlight')
  sparql = SPARQLWrapper('https://dbpedia.org/sparql')
  triples={}
  final_triples=[]
  uri_sub_list=[]
  uri_obj_list=[]
  with open('filtered_triples_avg.txt') as f:
      triples = [line.rstrip() for line in f]

  with open('final_triples.txt', 'w') as f:
    with MoonSpinner('Working hard for you ') as bar:    
      for i,triple in enumerate(triples):

        res = ast.literal_eval(triple)
        sub=res.get('subject')
        verb=res.get('relation')
        obj=res.get('object')
        f.write("--------------------------------- TRIPLE %s --------------------------------" % str(i+1))
        f.write('\n')
        f.write(sub+'\t\t'+verb+'\t\t'+obj)
        f.write('\n')    
        uri_sub_list=getURI_spacy(substitute_name(sub))
        uri_obj_list=getURI_spacy(substitute_name(obj))
        if len(uri_sub_list)>=1 or len(uri_obj_list)>=1:
          f.write('\n')
          f.write('URI:')
          f.write('\n')
        if len(uri_sub_list)>=1:
          for elem in uri_sub_list:
            f.write(elem)
            f.write('\n')
        if len(uri_obj_list)>=1:
          for elem in uri_obj_list:
            f.write(elem)
            f.write('\n')

        f.write('\n')
        f.write('VERB SENSES:')
        f.write('\n')
        verb_list = verb.split()
        for verb in verb_list:
          verb=getSense(verb)
          f.write(verb)
          f.write('\n')
        f.write('\n')
        bar.next()
    
    




