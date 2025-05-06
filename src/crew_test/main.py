#!/usr/bin/env python
import sys
import warnings
import random 

from datetime import datetime

from crew_test.teacher.crew import TeacherCrew
from crew_test.appraiser.crew import AppraiserCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

questions = [
    'Alvimar pagou uma compra de R$ 3,50 com uma nota de R$ 5,00 e recebeu o troco em moedas de R$ 0,25.Quantas moedas ele recebeu?',

    '''O pai de Carolina mediu o comprimento da mesa da sala com sua mão e contou 8 palmos.
    Ela também mediu a mesa do mesmo modo e contou 11 palmos.
    Qual é o tamanho do palmo de Carolina, se o palmo de seu pai mede 22 centímetros?''',

    '''Uma farmácia vende comprimidos em caixas com
    12, ao custo de 40 reais por caixa, ou em caixas com 8, ao
    custo de 25 reais por caixa. Paulo comprou exatamente
    28 comprimidos. Quanto ele gastou, em reais, nessa
    compra?
    ''',

    '''Um grupo de amigos se reuniu para comer quatro
    pizzas. Cada um deles comeu dois terços de uma pizza
    e não sobrou nada. Quantos eram os amigos?
    ''',

    '''Em um teatro, cada fileira tem 6 cadeiras. Para
    melhorar a acessibilidade, foram retiradas todas as
    cadeiras de uma fileira para formar um corredor e,
    depois, todas as 9 cadeiras na quinta posição das fileiras
    restantes. Quantas cadeiras sobraram?
    '''
]

def run():
    """
    Run the crew.
    """

    teacher = TeacherCrew().crew()
    appraiser = AppraiserCrew().crew()

    inputs = {
        'school_year': 'sexto ano',
        'question': '''
            Uma farmácia vende comprimidos em caixas com
            12, ao custo de 40 reais por caixa, ou em caixas com 8, ao
            custo de 25 reais por caixa. Paulo comprou exatamente
            28 comprimidos. Quanto ele gastou, em reais, nessa
            compra?
        ''',
        'correct_answer': '''
            Paulo comprou 28 comprimidos, em caixas com quantidades de 8 ou de 12 comprimidos cada. A única
            forma de Paulo fazer essa compra é com uma caixa de 12 comprimidos e duas caixas com 8 comprimidos. Logo, ele
            gastou 1 * 40 = 40 reais na caixa com 12 comprimidos mais 2 * 25 = 50 reais nas duas caixas com 8 comprimidos,
            totalizando 40 + 50 = 90 reais gastos nessa compra.
        ''',
        'tips': ''
    }

    inputs['tips'] = teacher.kickoff(inputs=inputs).raw
    ans = appraiser.kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CrewTest().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewTest().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        CrewTest().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
