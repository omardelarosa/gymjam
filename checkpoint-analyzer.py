import pickle
import argparse
import sys

from lunarlandercolab import FixedFeatureMap, Agent, GameEvaluator, LinearSizer, EmptyBuffer

def load_checkpoint(checkpoint_file_name):
    checkpoint_data = None
    with open(checkpoint_file_name, "rb") as f:
        checkpoint_data = pickle.load(f)
    if checkpoint_data:
        print("Checkpoint: {}".format(checkpoint_file_name))
        for key in checkpoint_data.elite_map:
            elite = checkpoint_data.elite_map[key]
            print("{}: fitness: {}, commands: {}".format(key, elite.fitness, elite.commands))
    return checkpoint_data


parser = argparse.ArgumentParser(description='Process checkpoints')
parser.add_argument('--files', metavar='F', type=str, nargs='+',
                    help='load checkpoints by name')

args = parser.parse_args()

checkpoints = []

print(len(sys.argv))
if args.files:
    for f in args.files:
        checkpoints.append(load_checkpoint(f))