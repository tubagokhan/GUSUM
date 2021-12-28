# GUSUM

This is an implementation of the  GUSUM ( as shorthand for Graph-Based Unsupervised Summarization) which a simple, yet effective approach to improving the state of the art in graph-based unsupervised extractive text summarization.

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

## 

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
@ inproceedings{ 


}
```


