from cremi import Volume
from cremi.evaluation import NeuronIds
import vigra
import os

# Load stuff
source_folder = '/mnt/localdata01/jhennies/neuraldata/cremi_2016/170321_resolve_false_merges/'
project_folder = '/mnt/localdata01/jhennies/neuraldata/results/multicut_workflow/170425_all_samples_lifted_more_trees/'
# TODO: Change here
experiment_folder = os.path.join(project_folder, 'splA_z1/')

mc_result_filepath = os.path.join(experiment_folder, 'result.h5')
# TODO: Change here when switching half
mc_result_key = 'z/1/data'

# TODO: Change here when switching result
glob_result_filepath = os.path.join(experiment_folder, 'result_resolved_global.h5')
glob_result_key = mc_result_key
loc_result_filepath = os.path.join(experiment_folder, 'result_resolved_local.h5')
loc_result_key = mc_result_key

# TODO: Change here when switching sample
gt_filepath = os.path.join(source_folder, 'cremi.splA.train.raw_neurons.crop.axes_xyz.split_z.h5')
# TODO: Change here when switching half
gt_key = 'z/1/neuron_ids'

mc_result = vigra.readHDF5(mc_result_filepath, mc_result_key)
glob_result = vigra.readHDF5(glob_result_filepath, glob_result_key)
loc_result = vigra.readHDF5(loc_result_filepath, loc_result_key)
gt = vigra.readHDF5(gt_filepath, gt_key)

vol_gt = Volume(gt)
neuron_ids_evaluation = NeuronIds(vol_gt)

# Evaluate baseline
vol_mc_result = Volume(mc_result)
(voi_split, voi_merge) = neuron_ids_evaluation.voi(vol_mc_result)
adapted_rand = neuron_ids_evaluation.adapted_rand(vol_mc_result)

print 'Baseline'
print "\tvoi split   : " + str(voi_split)
print "\tvoi merge   : " + str(voi_merge)
print "\tadapted RAND: " + str(adapted_rand)

# Evaluate global resolving
vol_glob_result = Volume(glob_result)
(voi_split, voi_merge) = neuron_ids_evaluation.voi(vol_glob_result)
adapted_rand = neuron_ids_evaluation.adapted_rand(vol_glob_result)

print 'Global'
print "\tvoi split   : " + str(voi_split)
print "\tvoi merge   : " + str(voi_merge)
print "\tadapted RAND: " + str(adapted_rand)

# Evaluate local resolving
vol_loc_result = Volume(loc_result)
(voi_split, voi_merge) = neuron_ids_evaluation.voi(vol_loc_result)
adapted_rand = neuron_ids_evaluation.adapted_rand(vol_loc_result)

print 'Local'
print "\tvoi split   : " + str(voi_split)
print "\tvoi merge   : " + str(voi_merge)
print "\tadapted RAND: " + str(adapted_rand)