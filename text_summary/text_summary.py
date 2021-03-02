import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


text="""In an attempt to build an AI-ready workforce, Microsoft announced Intelligent 
        Cloud Hub which has been launched to empower the next generation of students with
        AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud
        Hub will support around 100 institutions with AI infrastructure, course content and
        curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow." The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills."""

stopwords=list(STOP_WORDS)

nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
tokens=[token.text for token in doc]
punctuation=punctuation+'\n'
word_frequencies={}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text]=1
            else:
                word_frequencies[word.text]+=1
max_frequency=max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word]=word_frequencies[word]/max_frequency

sentence_tokens=[sent for sent in doc.sents]
select_length= int(len(sentence_tokens)*0.3)
summary= nlargest(select_length,sentence_scores,key=sentence_scores.get)
final_summary=[word.text for word in summary]
summary=''.join(final_summary)
print(summary)