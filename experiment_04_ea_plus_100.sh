#!/bin/sh
#
#SBATCH --verbose
#SBATCH --job-name=lunE04
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --mem=1GB

/bin/hostname
/bin/pwd

#module load python3/intel/3.6.3

eval "$(pyenv init -)"
pyenv activate lunarlander

# Where results are going to be written
OUTDIR=/scratch/od356/lunarlander_experiments_03
CHECKPOINT_FREQ=1000

for n in {1..20}
do
    python lunarlandercolab.py \
           --run-id=e04_$n \
           --search-type=ES \
           --is-plus \
           --num-generations=1000 \
           --num-parents=10 \
           --population-size=100 \
           --checkpoint-dir=$OUTDIR \
           --checkpoint-prefix=experiment04_$n \
           --checkpoint-enabled \
           --checkpoint-frequency=$CHECKPOINT_FREQ \
           --seed=1008
done
