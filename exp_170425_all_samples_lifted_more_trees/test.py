from cremi import Volume
from cremi.evaluation import NeuronIds
import vigra
import os

# Load stuff
source_folder = '/mnt/localdata02/jhennies/neuraldata/cremi_2016/170321_resolve_false_merges/'
project_folder = '/mnt/localdata01/jhennies/neuraldata/results/multicut_workflow/170425_all_samples_lifted_more_trees/'
experiment_folder = project_folder + 'splB_z1/'

mc_result_filepath = os.path.join(experiment_folder, 'result.h5')
mc_result_key = 'z/1/data'

res_result_filepath = os.path.join(experiment_folder, 'result_resolved_global.h5')
res_result_key = mc_result_key

gt_filepath = os.path.join(source_folder, 'cremi.splB.train.raw_neurons_defect_correct.crop.axes_xyz.split_z.h5')
gt_key = 'z/1/neuron_ids'

mc_result = vigra.readHDF5(mc_result_filepath, mc_result_key)
res_result = vigra.readHDF5(res_result_filepath, res_result_key)
gt = vigra.readHDF5(gt_filepath, gt_key)

# Evaluate
vol_mc_result = Volume(mc_result)
vol_gt = Volume(gt)

neuron_ids_evaluation = NeuronIds(vol_gt)

(voi_split, voi_merge) = neuron_ids_evaluation.voi(vol_mc_result)
adapted_rand = neuron_ids_evaluation.adapted_rand(vol_mc_result)

print ''
print "\tvoi split   : " + str(voi_split)
print "\tvoi merge   : " + str(voi_merge)
print "\tadapted RAND: " + str(adapted_rand)
