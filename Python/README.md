# Sistema de Detecção e Quantificação de Microplásticos na Água

## Integrantes
- Pedro Henrique Martins Alves dos Santos RM: 558107
- Victor de Almeida Gonçalves RM: 558799
- Felipe Cerboncini Cordeiro RM: 554909

## Contexto e Motivação
A presença de microplásticos nos oceanos representa um risco significativo para a saúde humana e para o meio ambiente marinho. Estes poluentes podem ser ingeridos por seres marinhos, entrando na cadeia alimentar e afetando tanto a vida aquática quanto os humanos que consomem frutos do mar. Nosso projeto visa mitigar esses danos, fornecendo alimentos mais seguros e de melhor qualidade, e auxiliando o governo na limpeza e preservação dos oceanos.

## Nosso Projeto
Este projeto simula a identificação e análise de amostras para quantificar a concentração de microplásticos no ambiente aquático.

### Identificação
A identificação dos microplásticos é realizada através de fotos capturadas por uma câmera embutida em um drone. Estas fotos são analisadas para detectar a presença de microplásticos ou outros resíduos poluentes. A simulação de detecção utiliza a função **random.randint(0, 1)**, onde 0 indica ausência e 1 presença de microplásticos.

### Coleta e Análise da Amostra
Quando microplásticos ou resíduos são identificados, uma amostra é coletada e analisada. No projeto, esta análise é simulada utilizando a função **random.uniform(5, 95)**, com base em um protótipo de Arduino desenvolvido no Thinkercad. Para mais detalhes, visite nosso repositório [aqui](https://github.com/VictorAlgonca/GS-EdgeComputing).

### Mapa de Calor
Após a análise das amostras, um mapa de calor das coordenadas analisadas é exibido, indicando as áreas com maior ou menor concentração de microplásticos.

![foto mapa de calor](https://imgur.com/2GgJ89j.png)

## Funcionamento do Sistema

1. O sistema solicita as coordenadas desejadas para análise.
2. Em seguida, pede o raio de análise (em metros) para cobrir todas as coordenadas registradas.
3. O sistema então simula a operação do drone e a análise do local. Se nenhum microplástico for encontrado, a mensagem "Nenhum microplástico encontrado" será exibida e o programa finalizará. Caso contrário, a mensagem "Microplástico detectado" será exibida e a coleta e análise da amostra será realizada.
4. Após a coleta e análise, o mapa de calor das coordenadas analisadas será exibido.

## Implementação do Projeto (Passo a Passo)

### Requisitos
- **Python:** Versão 3 [Baixe aqui](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe)
- **PyCharm Community Edition:** [Baixe aqui](https://www.jetbrains.com/pt-br/pycharm/download/download-thanks.html?platform=windows)
- **Bibliotecas:** `matplotlib`, `mplcursors` e `numpy`

### Configuração do Ambiente

1. **Criar um Ambiente Virtual:**
   - Abra o PyCharm e crie ou abra seu projeto.
   - No menu superior, vá para `File` > `New Project Settings` > `Preferences for New Projects` (ou `Settings` se já estiver em um projeto).
   - Navegue até `Project: [Seu Projeto]` > `Python Interpreter`.
   - Clique no ícone de engrenagem e selecione `Add...`.
   - Escolha `New environment` e selecione `Virtualenv`.
   - Escolha um local para o novo ambiente virtual e clique em `OK`.

2. **Ativar o Ambiente Virtual:**
   - Abra o terminal integrado do PyCharm (geralmente na parte inferior da janela do IDE).
   - Se o ambiente virtual não estiver ativado automaticamente, você pode ativá-lo manualmente:

     - **Unix (Linux/Mac):**
       ```sh
       source venv/bin/activate
       ```

     - **Windows:**
       ```sh
       .\venv\Scripts\activate
       ```

   - Substitua `venv` pelo nome da pasta do seu ambiente virtual, caso tenha escolhido um nome diferente.

3. **Verificar se o Ambiente está Ativo:**
   - Você saberá que o ambiente virtual está ativo quando o nome do ambiente aparecer entre parênteses no início da linha do terminal.

4. **Instalar Bibliotecas:**
   - Com o ambiente virtual ativado, instale as bibliotecas necessárias:
     ```sh
     pip install matplotlib 
     pip install mplcursors
     pip install numpy
     ```

## Impacto Ambiental

### Impacto na Vida Marinha
- Microplásticos são ingeridos por diversos organismos marinhos, causando asfixia, obstruções intestinais e até morte.
- Eles servem como vetores para contaminantes tóxicos, liberando substâncias nocivas dentro dos organismos.

### Impacto na Saúde Humana
- Microplásticos estão presentes na cadeia alimentar, sendo encontrados em frutos do mar, água potável e condimentos.
- A ingestão contínua pode levar ao acúmulo de partículas no corpo humano, aumentando o risco de distúrbios endócrinos e câncer.

### Necessidade de Ações Sustentáveis
- Adotar políticas públicas e iniciativas para reduzir a produção e descarte de plásticos.
- Investir em pesquisas para entender os efeitos dos microplásticos na saúde humana e no meio ambiente.

## Considerações Futuras

### Pesquisa Multidisciplinar e Avaliação de Riscos
- Investir em pesquisas que explorem os impactos dos microplásticos em diferentes sistemas biológicos.
- Realizar estudos epidemiológicos e toxicológicos para avaliar os riscos à saúde humana.

### Tecnologias de Detecção e Remoção
- Desenvolver métodos mais eficazes para detectar e quantificar microplásticos em alimentos, água e ar.
- Investir em tecnologias de remoção, como filtração avançada e adsorção seletiva.

### Conscientização e Políticas Sustentáveis
- Educar o público sobre os riscos dos microplásticos por meio de campanhas de conscientização.
- Implementar políticas restritivas para reduzir a produção e o descarte de plásticos.

## Referências
- [Documentação Python](https://docs.python.org/)

## Contribuições
As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será muito apreciada.

Se você tiver uma sugestão que possa melhorar o projeto, de um Fork no repositório e crie um Pull Request. Você também pode simplesmente abrir um problema com a tag “aprimoramento”. 

1. Fork o projeto;
2. Crie uma Branch;
3. De Commit nas suas alterações;
4. De um Push para a sua Branch;
5. Abra uma Pull Request.

## Licença
Distribuído sob a licença MIT. Consulte `LICENSE.txt` para obter mais informações.

## Conclusão
Nosso projeto simula a identificação e análise de amostras para quantificar a concentração de microplásticos no ambiente. Esta iniciativa é crucial para a remoção e controle dos danos causados pela presença de microplásticos, contribuindo para a saúde humana e a preservação ambiental.