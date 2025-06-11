#!/usr/bin/env python
import sys
import warnings
import random
import yaml

from datetime import datetime
from pathlib import Path

from crew_test.teacher.crew import TeacherCrew
from crew_test.appraiser.crew import AppraiserCrew
from crew_test.image_reader.crew import ImageReaderCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_inputs(folders):
    path = Path(__file__)

    for _ in range(0, 3):
        path = path.parent
    
    for folder in folders:
        path /= folder
    
    path /= "inputs.yaml"

    with open(path, "r", encoding = "utf-8") as file:
        inputs = yaml.safe_load(file)

        inputs["max_number_of_tips"] = 2
        inputs["tips"] = ""
    
    return inputs

def run():
    inputs = get_inputs(["res", "2020", "f1", "ta", "nj", "quebrando_o_quebra_cabecas_2"])

    if inputs is None:
        raise Exception("Algo deu errado!!!")
    else:
        teacher = TeacherCrew().crew()
        appraiser = AppraiserCrew().crew()
        image_reader = ImageReaderCrew().crew()

        if inputs["image_url"] is None:
            if inputs["image_description"] is None:
                inputs["image_description"] = "Sem imagem."
        else:
            inputs["image_description"] = image_reader.kickoff(inputs={"image_url": inputs["image_description"]}).raw

        inputs["tips"] = teacher.kickoff(inputs=inputs).raw

        ans = appraiser.kickoff(inputs=inputs)