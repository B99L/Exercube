import logging
import os

START_TAG = '####StartLogging####'
STOP_TAG = '####StopLogging####'


# The Model Name which the folder in models in named after
# The file that is choosen to log from
# The name of the log-file
def log_file(model_name, destination_file, file_to_log):
    log_file_base_path = "./models/" + model_name + "/logs/"
    if not os.path.exists(log_file_base_path):
        os.makedirs(log_file_base_path)
    modus = 0 #0 is for not logging and 1 for logging
    destination_file = open(log_file_base_path + destination_file, "a")
    with open(file_to_log, 'r') as file_to_log:
        for line in file_to_log:
            if line.find(START_TAG)>= 0:
                modus = 1
            if modus == 1:
                destination_file.write(line)
            if line.find(STOP_TAG)>= 0:
                modus = 0
    file_to_log.close()
    destination_file.close()
    #logging.Handler.close()

def create_log(model_name, destination_file, content):
    log_file_base_path = "./models/" + model_name + "/logs/"
    if not os.path.exists(log_file_base_path):
        os.makedirs(log_file_base_path)
    destination_file = open(log_file_base_path + destination_file, "a")
    destination_file.write(content)
    destination_file.close()

def create_summary_log(model_name, destination_file, model):
    stringlist = []
    model.summary(print_fn=lambda x: stringlist.append(x))
    short_model_summary = "\n".join(stringlist)
    create_log(model_name, destination_file, short_model_summary)
