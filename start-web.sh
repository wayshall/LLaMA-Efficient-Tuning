#!/bin/bash
conda activate llmtuning
CUDA_VISIBLE_DEVICES=0 python src/train_web.py
