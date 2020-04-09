#!/bin/bash

# Upgrade pip
pip install --upgrade pip

# Clone OpenAI Gym
cd lib
git clone https://github.com/openai/gym.git
cd gym
pip install -e .

# Install box2d for LunarLander env
pip install -e '.[box2d]'

# return to current directory
cd ..