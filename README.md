
We've adhered to the honor code on this assignmnt.

Kirsten, Lee, Derek


This Github repository holds our code for our automated summary generator. To try it out please run main.py. Please note that you will need python 3.5 for later to run our generator, as well as the library NLTK. But, the rouge-1 in eval.py uses python2.

Summarizer.py:
    .py file where the actual summary generation takes place, along with the tf-idf heuristic calculations <br>
positon.py:
    .py file where position weights are generated. <br>
paragraphs.py
    separates text files from nltk out into lists of paragraphs. <br>
eval.py:
    which is a python 2 file which evaluates our summaries <br>

python wrapper for ROUGE used for eval: https://github.com/miguelbalmeida/PythonROUGE.git
