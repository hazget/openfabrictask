import os
import warnings
from Sciencebot import bot
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
import json
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    with open("config/execution.json", "w") as jsonfile:
        configuration_object = json.load(jsonfile)
        configuration_object ["config_class"] = configuration
        json.dump(configuration_object, jsonfile)
        jsonfile.close()
    


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        answer = bot(text)
    output.append(str(answer))
    return SimpleText(dict(text = output))

    
