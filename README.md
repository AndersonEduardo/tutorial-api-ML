# Exemplo de API para ML

Um exemplo simples de API para um modelo de ML. Abaixo, segue o tutorial para sua implementação na máquina local (usando **_Ubuntu 18.04_**). Para tudo dar certo é necessário ter [Python3](https://www.python.org/) e [venv](https://docs.python.org/3/library/venv.html) instalados na máquina.

### _Obtendo o código_

Obtenha o código deste repositório. Abra o terminal e digite (numa pasta de trabalho apropriada): `git clone https://github.com/AndersonEduardo/exemplo-api-ML.git`

### _Crie um ambiente virtual_

Entre na pasta criada (_exemplo-api-ML_) e crie um _virtual environment_: `python3 -m venv myenv`

Depois de criar, ative o ambiente virtual criado: `. myenv/bin/activate`

### _Instalando requerimentos_

Instale os requerimentos: `pip install -r requirements.txt`

### _Treinando o modelo_

Nos códigos disponibilizados neste repositório são fornecidos arquivos com extensão `.pkl`. Eles são arquivos para o modelo já treinado e salvo no diretório. Entretanto, caso queria rodar o modelo na sua máquina, basta usar: `python model.py`

### _Subindo para o servidor_

Se tudo correu bem e sem erros, rode o servidor do Flask: `python main.py`

A API deverá estar ativa no endereço: `http://127.0.0.1:12345/predict`

Entretanto, (neste exemplo) precisaremos de um serviço de cliente para utilizar a API.

### _Usando_

Esta API contém um classificador (bem simples) para o clássico problema dos sobreviventes do [naufrágio do Titanic](https://www.kaggle.com/samukaunt/titanic-passo-a-passo-com-8-modelos-ml-pt-br). Por simplicidade, aqui será usado apenas informações referentes à idade (coluna _Age_), sexo (coluna _Sex_), classe (coluna _Embarked_) e a variável resposta (coluna _Survived_, que indica se a pessoa sobreviveu ou não). Como exemplo de uso, será usado o [Postman](https://www.getpostman.com/). Faça dowload e abra o programa. Feito isso, selecione na barra de envio e escreva (ou copie e cole do navegador) o endereço ("endpoint") da API. Abaixo da barra de envio, selecione consecutivamente as opções: (i) POST; (ii) raw; (iii) JSON (application/json). Na caixa de texto, adicione os dados que serão enviados para a API processar. Como exemplo:

```

[
	{"Age":85, "Sex":"male","Embarked":"C"},
	{"Age":24, "Sex":"female","Embarked":"C"},
	{"Age":4, "Sex":"male","Embarked":"A"}
	]

```

Depois, é só clicar no botão azul `Send`. Os dados serão processados pela API e o _output_ retornará na caixa de texto inferior do Postman.

Veja em detalhe:

![](https://image.ibb.co/eCBKbe/Capture.jpg)



