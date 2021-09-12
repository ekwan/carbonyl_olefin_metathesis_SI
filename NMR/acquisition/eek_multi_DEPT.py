# takes a series of experiments in a template directory
# and runs them for the specified sample positions
#
# note: must start script in a PROCNO

# make sure that the expnos do not exist in the destinations first!
#
# experiments do not have to exist first

import os
from datetime import datetime
from collections import OrderedDict
import random

### PARAMETERS ###
# note that existing data in the destination
# experiments will be overwritten
user_dir= "/opt/topspin4.0.5/data/kwaneu/nmr"
log_filename = "eek_log-12_30_20.txt"
lock_solvent = "dmso"
shimming_command = "topshim tuneb ordmax=6 o1p=2.5 selwid=0.2"
#shimming_command = "topshim ordmax=6 o1p=2.5 selwid=0.2"
stabilization_time = 300 # time to wait after shimming before starting to do anything
repetitions = 7 # how many times to repeat the acquisition cycle
randomize_order = True  # whether to acquire the samples in the acquisition cycle in a random order
starting_target_expno=206 # expnos will increment based on repetitions
##################

### EXPERIMENTS ###
template_experiment_name = "alison-template"
template_experiment_map = {  # map from source_expno to source_experiment_description
	#10 : "proton",
	11 : "DEPT",
}

# which experiments to run
# the same expnos will be used in the target experiments
target_experiment_map = OrderedDict() # sample_name --> sx_number
#target_experiment_map["alison-sample11"] = 18
#target_experiment_map["alison-sample12"] = 19
#target_experiment_map["alison-sample13"] = 20
#target_experiment_map["alison-sample14"] = 21
target_experiment_map["alison-sample2"] = 2
target_experiment_map["alison-sample4"] = 4
target_experiment_map["alison-sample6"] = 6
target_experiment_map["alison-sample8"] = 8


# represents a single acquisition
class Acquisition():
	def __init__(self, source_experiment_name, source_expno, sx_number, destination_experiment_name, destination_expno, experiment_description):
		self.source_experiment_name = source_experiment_name            # eg alison-template (the name of the folder containing the template experiment)
		self.source_expno = source_expno                                # eg 1 (which expno the experiment to run is in the template experiment)
		self.sx_number = sx_number                                      # eg 1 (the location of the sample in the sample changer)
		self.destination_experiment_name = destination_experiment_name  # eg alison-sample1 (the folder name of the sample to acquire on)
		self.destination_expno = destination_expno                      # eg 100 (which expno the experiment to run is in the acquisition experiment)
		self.experiment_description = experiment_description            # eg DEPT (a string description of the experiment to be run in this expno)

todo_list = [] # contains Acquisitions

for repetition in range(repetitions):
	sample_list = list(target_experiment_map.items())
	if randomize_order:
		random.shuffle(sample_list)
	for target_experiment_name,sx_number in sample_list:
		for i,(source_expno,source_experiment_description) in enumerate(template_experiment_map.iteritems()):
			destination_expno = starting_target_expno + repetition*len(template_experiment_map) + i
			acquisition = Acquisition(template_experiment_name, source_expno, sx_number, target_experiment_name, destination_expno, source_experiment_description)
			todo_list.append(acquisition)

total_n_experiments = len(todo_list)
###################

# change the working directory
os.chdir(user_dir)

# get the current time as a string
def timestamp():
	now = datetime.now()
	return now.strftime("[%Y-%m-%d %H:%M:%S] ")

# delete the log file if it already exists
if os.path.exists(log_filename):
	os.remove(log_filename)

# define some basic operations first
with open(log_filename, "a") as log_file:
	# write a message to the log file
	def log(message, end="\n"):
		log_file.write(timestamp() + message + end)
		log_file.flush()

	# insert the sample at sample_position
	def sx(sample_position):
		log("Switching to sx %s..." % sample_position)
		ct = XCMD("sx %s" % sample_position, wait=WAIT_TILL_DONE, arg=None)
		log("Sample is in.")

	# shim
	def prepare():
		log("Locking...")
		XCMD("noqu lock %s" % lock_solvent)
		log("Done locking.  Shimming...")
		XCMD("noqu %s" % shimming_command)
		log("Done shimming.  Waiting to stabilize...")
		SLEEP(stabilization_time)
		log("Done waiting.")

	# acquire
	def acquire(experiment_name, expno, experiment_description, current_n_experiments):
		log("Acquiring %s (%s, experiment %s; %s of %s)..." % (experiment_description, experiment_name, expno, current_n_experiments, total_n_experiments))
		XCMD("re %s %s 1" % (experiment_name, expno))
		XCMD("noqu zg yes")
		SLEEP(5)
		XCMD("xf2")
		log("Done acquiring.")

	# copy from template to destination
	def initialize(source_experiment_name, source_expno, destination_experiment_name, destination_expno, experiment_description):
		XCMD("re %s %s" % (source_experiment_name, source_expno))
		XCMD("wrpa %s %s 1" % (destination_experiment_name, destination_expno))
		XCMD("re %s %s 1" % (destination_experiment_name, destination_expno))
		log("Initialized %s experiment for sample %s (expno %s)." % (experiment_description, destination_experiment_name, destination_expno))

	# initialize
	log("=== Automated Acquisition ===")
	log("Working directory is: %s" % os.getcwd())

	# start the run
	current_n_experiments = 1
	last_sx_number = -1
	for a in todo_list:
		source_experiment_name, source_expno, sx_number, destination_experiment_name, destination_expno, experiment_description = a.source_experiment_name, a.source_expno, a.
sx_number, a.destination_experiment_name, a.destination_expno, a.experiment_description
		if last_sx_number != sx_number:
			sx(sx_number)
			prepare()
		initialize(source_experiment_name, source_expno, destination_experiment_name, destination_expno, experiment_description)
		SLEEP(1)
		acquire(destination_experiment_name, destination_expno, experiment_description, current_n_experiments)
		current_n_experiments += 1
		last_sx_number = sx_number


	log("=== Program Complete ===")
