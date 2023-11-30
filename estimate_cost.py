#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import tiktoken

encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")

with open("data.json") as f:
    data = json.load(f)

prompt_price = 0.001  # per 1000 tokens
generated_price = 0.002  # per 1000 tokens

total_price = 0
for sample in data:
    prompt_tokens = encoder.encode(sample["prompt"])
    generated_tokens = encoder.encode(sample["completion"])
    prompt_cost = len(prompt_tokens) / 1000 * prompt_price
    generated_cost = len(generated_tokens) / 1000 * generated_price
    total_price += prompt_cost + generated_cost

print(f"Total cost for this data file: ${total_price:.3f}")
