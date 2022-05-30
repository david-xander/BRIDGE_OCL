# BRIDGE for OCL


## Requirements
You need to use Anaconda and Python 3.7
python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
python3 -m pip install -r requirements.txt
export PYTHONPATH=`pwd` && python -m nltk.downloader punkt

## Picasso commands
module load anaconda/2021.05
source activate tabularsemantics
(Do not use conda activate in loginexa)

## Anaconda
python -m pip install -r requirements


# PROJECT BASED ON: 
## Bridging Textual and Tabular Data for Cross-Domain Text-to-SQL Semantic Parsing

Authors:
Xi Victoria Lin, Richard Socher and Caiming Xiong. [Bridging Textual and Tabular Data for Cross-Domain Text-to-SQL Semantic Parsing](https://arxiv.org/abs/2012.12627). Findings of EMNLP 2020.

Authors's Repository:
https://github.com/salesforce/TabularSemanticParsing