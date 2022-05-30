import random
import json
import os
import sys
from src.parse_args import args
os.environ['CUDA_VISIBLE_DEVICES'] = '{}'.format(args.gpu)

import src.common.ops as ops
import src.data_processor.data_loader as data_loader
import src.data_processor.processor_utils as data_utils
from src.data_processor.data_processor import preprocess
from src.data_processor.vocab_processor import build_vocab
from src.data_processor.schema_graph import SchemaGraph
from src.data_processor.path_utils import get_model_dir, get_checkpoint_path
from src.demos.demos import Text2SQLWrapper
import src.eval.eval_tools as eval_tools
from src.eval.wikisql.lib.dbengine import DBEngine
from src.semantic_parser.ensemble_configs import model_dirs as ensemble_model_dirs
from src.semantic_parser.learn_framework import EncoderDecoderLFramework
from src.trans_checker.args import args as cs_args
import src.utils.utils as utils

import torch

print(args.seed)


# if not args.data_parallel:
#     torch.cuda.set_device('cuda:{}'.format(args.gpu))
torch.manual_seed(args.seed)
torch.cuda.manual_seed_all(args.seed)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set model ID
args.model_id = utils.model_index[args.model]
assert(args.model_id is not None)


def train(sp):
    dataset = data_loader.load_processed_data(args)


    print(dataset)
    # train_data = dataset['train']
    # print('{} training examples loaded'.format(len(train_data)))
    # dev_data = dataset['dev']
    # print('{} dev examples loaded'.format(len(dev_data)))

    # if args.xavier_initialization:
    #     ops.initialize_module(sp.mdl, 'xavier')
    # else:
    #     raise NotImplementedError

    # sp.schema_graphs = dataset['schema']
    # if args.checkpoint_path is not None:
    #     sp.load_checkpoint(args.checkpoint_path)

    # if args.test:
    #     train_data = train_data + dev_data

    # sp.run_train(train_data, dev_data)