#!/usr/bin/env bash
cd BRIDGE_OCL
source activate tabularsemantics
bash ./experiment-bridge.sh configs/bridge/spider-bridge-bert-large.sh --train 0
