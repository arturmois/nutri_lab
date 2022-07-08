from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect


def verificar(request, paciente):

    if len(peso.split()) == 0 or len(altura.split()) == 0 or len(peso.split(gordura)) == 0 or len(peso.split(musculo)) == 0 or len(peso.split(hdl)) == 0 or len(peso.split(ldl)) == 0 or len(colesterol_total.split(trigliceridios)) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
        return redirect(f'/dados_paciente/{paciente.id}/')
    
    if not peso.isnumeric() or not altura.isnumeric() or not gordura.isnumeric() or not musculo.isnumeric() or not hdl.isnumeric() or not ldl.isnumeric() or not colesterol_total.isnumeric() or not trigliceridios.isnumeric():
        messages.add_message(request, constants.ERROR, 'Digite valores válidos.')
        return redirect(f'/dados_paciente/{paciente.id}/')
        
    return True
