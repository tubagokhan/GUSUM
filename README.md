# GUSUM

This is an implementation of the  GUSUM ( as shorthand for Graph-Based Unsupervised Summarization) which a simple, yet effective approach to improving the state of the art in graph-based unsupervised extractive text summarization. 

Full Paper: https://aclanthology.org/2022.textgraphs-1.5

## Installation

You need to install python3 and following libraries

```
pip install sentence-transformers==2.0.0
pip install nltk==3.5
pip install numpy
pip install py-rouge==1.1

```

## Data used in the paper

For The CNN / DailyMail Dataset:  https://huggingface.co/datasets/cnn_dailymail

```
from datasets import load_dataset
dataset = load_dataset('cnn_dailymail', '3.0.0')

```

For The New York Times Annotated Corpus: https://catalog.ldc.upenn.edu/LDC2008T19 

## Files Structure

The files are organized as follows:

```
.
├── README.md
└── main.py
└── sentenceRanking.py
└── graph.py
└── data
    └── CnnDailyDataset
        ├── Documents
            ├── News1.txt
            ├── News2.txt
            ├── ....
            └── News11490.txt
        ├── Highlights
            ├── Highlight.A.1.txt
            ├── Highlight.A.2.txt
            ├── ....
            └── Highlight.A.11490.txt
        └── MySummaries
            ├── MySummary.1.txt
            ├── MySummary.2.txt
            ├── ....
            └── MySummary.11490.txt

```
## Evaluation

Automated evaluation used the py-rouge package. https://pypi.org/project/py-rouge/ Our evaluation metrics are set as shown below.

```
evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l', 'rouge-w'],
                           max_n=4,
                           limit_length=False,
                           length_limit=1000,
                           length_limit_type='words',
                           apply_avg=apply_avg,
                           apply_best=apply_best,
                           alpha=0.2, 
                           weight_factor=1.2,
                           stemming=True)
                           
 ```

## Citation
```
@InProceedings{gokhan-smith-lee:2022:textgraphs,
  author    = {Gokhan, Tuba  and  Smith, Phillip  and  Lee, Mark},
  title     = {GUSUM: Graph-based Unsupervised Summarization Using Sentence Features Scoring and Sentence-BERT},
  booktitle      = {Proceedings of TextGraphs-16: Graph-based Methods for Natural Language Processing},
  month          = {October},
  year           = {2022},
  address        = {Gyeongju, Republic of Korea},
  publisher      = {Association for Computational Linguistics},
  pages     = {44--53},
  abstract  = {Unsupervised extractive document summarization aims to extract salient sentences from a document without requiring a labelled corpus. In existing graph-based methods, vertex and edge weights are usually created by calculating sentence similarities. In this paper, we develop a Graph-Based Unsupervised Summarization(GUSUM) method for extractive text summarization based on the principle of including the most important sentences while excluding sentences with similar meanings in the summary. We modify traditional graph ranking algorithms with recent sentence embedding models and sentence features and modify how sentence centrality is computed. We first define the sentence feature scores represented at the vertices, indicating the importance of each sentence in the document. After this stage, we use Sentence-BERT for obtaining sentence embeddings to better capture the sentence meaning. In this way, we define the edges of a graph where semantic similarities are represented. Next we create an undirected graph that includes sentence significance and similarities between sentences. In the last stage, we determine the most important sentences in the document with the ranking method we suggested on the graph created. Experiments on CNN/Daily Mail, New York Times, arXiv, and PubMed datasets show our approach achieves high performance on unsupervised graph-based summarization when evaluated both automatically and by humans.},
  url       = {https://aclanthology.org/2022.textgraphs-1.5}
}

```


