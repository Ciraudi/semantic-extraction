/* 
 * 
 * Authors:
 * Ciraudo Egidio       0622701566  e.ciraudo@studenti.unisa.it           
 * Aleksandruk Lyubov   0622701472	l.aleksandruk@studenti.unisa.it 
 * Valentino Daniele    0622701069  d.valentino5@studenti.unisa.it
 * D'Amato Giuseppina   0622701577  g.damato43@studenti.unisa.it
 *
 * Copyright (C) 2022 - All Rights Reserved 
 *
 * This file is part of semantic-extraction.
 *
 * semantic-extraction is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * semantic-extraction is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with semantic-extraction.  If not, see <http://www.gnu.org/licenses/>.
 */

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

