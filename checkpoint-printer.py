import argparse
import sys
from lunarlandercolab import FixedFeatureMap, Agent, GameEvaluator, LinearSizer, EmptyBuffer
from checkpointing import Checkpoint
import csv

# Use as a CLI when called directly
parser = argparse.ArgumentParser(description='Process checkpoints')
parser.add_argument('--files', metavar='F', type=str, nargs='+',
                    help='load checkpoints by name')
parser.add_argument('--logs', metavar='L', type=str, nargs='+',
                    help='load logs by filename')

args = parser.parse_args()

checkpoints = []

print(len(sys.argv))

runs = []

if args.files:
    for f in args.files:
        c = Checkpoint(checkpoint_file_name=f)
        checkpoints.append(c)
        if c.checkpoint_data:
            run = {
                'file_name': f
            }
            if isinstance(c.checkpoint_data, FixedFeatureMap):
                # NOTE: these are only for the FINAL map at the end of the run
                # Spreadsheet I column - mean cells filled is avg of these across all runs
                cells_filled_for_given_run = len(c.checkpoint_data.elite_map.keys())
                run['cells_filled'] = cells_filled_for_given_run
                # Spreadsheet G col -
                print("num_keys: {}".format(cells_filled_for_given_run))
                # Summed mean fitness = sum(for_each cell get fitness) / num_cells
                # aka average fitness per cell in map for run
                sum_fitness = 0
                for key in c.checkpoint_data.elite_map:
                    elite = c.checkpoint_data.elite_map[key]
                    sum_fitness += elite.fitness
                    print("{}: fitness: {}, commands: {}".format(key, elite.fitness, elite.commands))
                run['sum_fitness'] = sum_fitness
            else:
                    # print(c.checkpoint_data)
                    print(c.checkpoint_data.fitness, c.checkpoint_data.commands)
            runs.append(run)
    for r in runs:
        print(r)
