from openie import StanfordOpenIE
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sentence_transformers import SentenceTransformer, util
from progress.spinner import MoonSpinner

# https://stanfordnlp.github.io/CoreNLP/openie.html#api
# Default value of openie.affinity_probability_cap was 1/3.
properties = {
    'openie.affinity_probability_cap': 2 / 3,
}

def lemma(lemmatizer, word, pos):
    """
    Print the results of stemmind and lemmitization using the passed stemmer, lemmatizer, word and pos (part of speech)
    """
    return lemmatizer.lemmatize(word, pos)

def lemma_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    lemmatized=[]
    s=""
    for word in words:
        word = lemma(lemmatizer, word = word, pos = wordnet.VERB)
        word= lemmatizer.lemmatize(word)
        if word not in ['as','a','also','As','the','The', 'Against', 'against']:
            lemmatized.append(word)
    for w in lemmatized:
        s=s+" "+w
    return s

def parhentesis(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

def remove_stopwords(sentence):
    words = nltk.word_tokenize(sentence)
    custom_stopwords={'–','``',"''","'s","'"}
    nostop_word=[]
    s=""
    for word in words:
        if not word in custom_stopwords:
            nostop_word.append(word)
    for w in nostop_word:
        s=s+" "+w
    return s

def similarity(source=[], sentences=[]):
    
    th=0.60
    #Compute embedding for both lists
    embeddings1 = model.encode(source, convert_to_tensor=True)
    embeddings2 = model.encode(sentences, convert_to_tensor=True)

    #Compute cosine-similarits
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    #Output the pairs with their score
    for i in range(len(source)):
        for j in range(len(sentences)):
            if cosine_scores[i][j] > th:
                print("{} \t\t Score: {:.4f}".format(sentences[j], cosine_scores[i][j]))
                return True
            else: return False


def similarity_avg(source=[], sentences=[]): # 1 source

    avg=0
    #Compute embedding for both lists
    embeddings1 = model.encode(source, convert_to_tensor=True)
    embeddings2 = model.encode(sentences, convert_to_tensor=True)

    #Compute cosine-similarits
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    for j in range(len(sentences)):
        avg=avg+cosine_scores[0][j]
    th=avg/(len(sentences))

    filtered=[]
    #Output the pairs with their score
    for i in range(len(source)):
        for j in range(len(sentences)):
            if cosine_scores[i][j] >= th:
                filtered.append(j)
    return filtered


if __name__ == "__main__":
    lemmatizer = WordNetLemmatizer()
    model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

    triples=[]
    paragphs=[]
    with open('summary.txt') as f:
        sentences = [line.rstrip() for line in f]
        
    res =[]

    for sen in sentences:
        if not sen in [None, ''] :
            new_sen=parhentesis(sen)
            new_sen=remove_stopwords(new_sen)
            res.append(new_sen)
    sentences=res

    with open('triples.txt', 'w') as f:
        with StanfordOpenIE(properties=properties) as client:
        
            triples=[]
            filtered_triples=[]
        with MoonSpinner('Triples Extraction ') as bar:    
            for text in sentences: 
                annotated=client.annotate(text)

                for triple in annotated:
                    f.write(str(triple))
                    f.write('\n')
                    sub=triple.get('subject')
                    verb=triple.get('relation')
                    obj=triple.get('object')
                    my_tripla=sub+' '+verb+' '+obj
                    triples.append(my_tripla) 

                indexes=similarity_avg([text],triples)
                
                if len(indexes)!=0:
                    for i,triple in enumerate(annotated):
                        if i in indexes:
                            sub=triple.get('subject')
                            verb=triple.get('relation')
                            obj=triple.get('object')
                            lemmatized_sub=lemma_sentence(sub)
                            lemmatized_verb=lemma_sentence(verb)
                            lemmatized_obj=lemma_sentence(obj)
                            lemmatized_triple={'subject':lemmatized_sub.strip(), 'relation':lemmatized_verb.strip(), 'object':lemmatized_obj.strip()}
                            if not lemmatized_triple in triples:
                                filtered_triples.append(lemmatized_triple) 
                bar.next()


        #saving filtered triples

        with open('filtered_triples_avg.txt', 'w') as f:
            for tri in filtered_triples:
                f.write(str(tri))
                f.write('\n')
                


