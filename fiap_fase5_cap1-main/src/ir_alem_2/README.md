# Ir Além 2 - 🌱 Projeto de monitoramento inteligente de plantas

#### 🎥 Vídeo Explicativo

- ** Ir Além 2 🌱 Projeto de monitoramento inteligente de plantas:** [https://www.youtube.com/watch?v=kxKfG09zvTg](https://www.youtube.com/watch?v=kxKfG09zvTg) *(não listado)*


Projeto de monitoramento inteligente de plantas utilizando ESP32, sensores ambientais, API em Python (FastAPI), dashboard interativo (Streamlit) e modelo de Machine Learning para previsão da saúde vegetal.

## Descrição
O "Ir Além 2" integra hardware e software para monitorar, coletar, analisar e exibir dados ambientais de plantas em tempo real. O sistema utiliza um ESP32 conectado a sensores (umidade do solo, temperatura e umidade do ar, luminosidade) que envia leituras para uma API Python. Os dados são processados, armazenados e exibidos em um dashboard web, além de serem analisados por um modelo de Machine Learning para prever a saúde da planta.

## Estrutura do Projeto
- **src/ir_alem_2/esp32/**: Código-fonte do ESP32 (C++/Arduino)
- **src/ir_alem_2/src/api/**: API FastAPI para receber e processar dados
- **src/ir_alem_2/src/dashboard/**: Dashboard em Streamlit
- **src/ir_alem_2/src/machine_learning/**: Notebooks e scripts de ML
- **database/**: Módulo de persistência de dados
- **diagram.json**: Diagrama de conexão dos sensores

## Pré-requisitos
- Python 3.11+
- pip
- [PlatformIO](https://platformio.org/) (para ESP32)

## Instalação

### 1. Instale as dependências Python
```bash
pip install -r requirements.txt
```

### 2. Instale o PlatformIO (para ESP32)
Siga as instruções em https://platformio.org/install

## Como Rodar

### 1. Rodar o Dashboard (Frontend) e API

Na raiz do projeto:

```bash
streamlit run dashboard_ir_alem_2.py
```
O dashboard abrirá no navegador padrão.

### 2. Compilar e Subir o Código no ESP32
- Conecte o ESP32 ao computador.
- Edite o arquivo `platformio.ini` se necessário (SSID, senha, IP da API).
- Compile e envie:
```bash
platformio run --target upload
```

## Funcionamento do ESP32

O ESP32 é o componente central do sistema embarcado do projeto "Ir Além 2". Ele é responsável por coletar dados ambientais, exibir informações ao usuário e se comunicar com a API para armazenamento e análise dos dados. Abaixo, detalhamos seu funcionamento:

### Sensores e Periféricos Conectados
- **DHT22:** Mede temperatura e umidade do ar.
- **LDR:** Mede a intensidade de luz (luminosidade do ambiente).
- **Sensor de umidade do solo:** Mede a umidade do solo.
- **LCD I2C:** Exibe leituras dos sensores, status de conexão, mensagens de sucesso ou erro e o resultado da análise de saúde da planta.

### Fluxo de Funcionamento
1. **Inicialização:**
   - O ESP32 inicializa todos os sensores e o display LCD.
   - Tenta se conectar à rede Wi-Fi configurada.

2. **Ciclo de Operação:**
   - A cada 5 segundos, o ESP32 lê os valores dos sensores (temperatura, umidade do ar, luminosidade e umidade do solo).
   - Os valores lidos são exibidos no LCD em tempo real, facilitando o acompanhamento local.
   - Os dados são enviados para a API via Wi-Fi. O LCD informa o status do envio (sucesso ou erro).
   - Após o envio, o ESP32 solicita à API uma análise da saúde da planta, baseada nos dados enviados e no modelo de Machine Learning.
   - O resultado da análise (planta saudável ou doente) é exibido no LCD.

3. **Resiliência e Feedback:**
   - Caso a conexão Wi-Fi falhe, o ESP32 tenta reconectar automaticamente e exibe mensagens de erro no LCD.
   - Se houver falha no envio dos dados ou na análise de saúde, o sistema informa o usuário e tenta novamente nas próximas iterações.

### Diagrama de Hardware

<p align="center">
  <img src="../../assets/ir_alem_2/esp32_ir_alem.JPG" alt="Circuito Sensor" border="0" width=70% height=70%>
</p>

Para detalhes sobre as conexões físicas dos sensores e periféricos ao ESP32, consulte o arquivo `diagram.json` na raiz do projeto. O diagrama mostra claramente os pinos utilizados e a topologia do sistema.

Esse funcionamento garante a automação do monitoramento, a robustez na comunicação e a facilidade de uso tanto localmente (via LCD) quanto remotamente (via dashboard e API).

## Machine Learning
O notebook `src/ir_alem_2/src/machine_learning/treinamento_modelo.ipynb` mostra o processo de análise, treinamento e exportação do modelo de ML para prever a saúde da planta com base nos dados coletados.

## Páginas do Dashboard

### Página Principal
A página principal do dashboard exibe um panorama visual das leituras dos sensores conectados ao sistema. Nela, o usuário encontra:

- **Gráfico Temporal dos Sensores:**
  Um gráfico de linhas mostra a evolução das leituras dos sensores ao longo do tempo, agrupadas por tipo (umidade do solo, temperatura, umidade do ar, luminosidade, etc). Isso permite identificar tendências, padrões e possíveis anomalias ambientais que podem afetar a saúde da planta.

- **Tabela de Dados:**
  Abaixo do gráfico, é apresentada uma tabela com os valores médios das leituras, organizados por data e tipo de sensor. Isso facilita a análise detalhada e a exportação dos dados, se necessário.

- **Mensagem Explicativa:**
  Um texto orienta o usuário sobre a interpretação do gráfico e da tabela, reforçando o objetivo de monitoramento contínuo.

Essa página é ideal para acompanhamento histórico e tomada de decisão baseada em dados reais coletados pelo ESP32.

### Página Previsão
A página de previsão permite ao usuário simular cenários e obter uma análise preditiva da saúde da planta, utilizando o modelo de Machine Learning treinado pelo projeto. Nela, o usuário pode:

- **Inserir Dados Manualmente:**
  Campos para entrada de valores de umidade do solo, umidade do ambiente, luminosidade (lux) e temperatura. Esses valores podem ser obtidos dos sensores ou inseridos para simulação.

- **Obter Previsão Instantânea:**
  Ao clicar no botão de previsão, o sistema utiliza o modelo de Machine Learning para analisar os dados informados e retorna se a planta está saudável ou não, exibindo uma mensagem visual (sucesso ou alerta).

Essa funcionalidade é útil tanto para validação dos dados coletados quanto para simulações de diferentes condições ambientais, auxiliando no entendimento do impacto de cada variável na saúde da planta.

## API e Previsão de Saúde da Planta

A API do projeto "Ir Além 2" é desenvolvida em FastAPI e atua como o núcleo de integração entre o hardware (ESP32), o banco de dados e o modelo de Machine Learning. Ela é responsável por receber, armazenar e processar os dados dos sensores, além de fornecer previsões sobre a saúde da planta.

### Principais Endpoints
- **/init**: Realiza o cadastro e inicialização dos sensores na base de dados, garantindo que cada sensor esteja registrado corretamente.
- **/leitura**: Recebe as leituras dos sensores (umidade do solo, temperatura, umidade do ar, luminosidade) e armazena no banco de dados, associando cada valor ao tipo de sensor e ao momento da leitura.
- **/saude**: Realiza a previsão da saúde da planta a partir dos dados recebidos, utilizando um modelo de Machine Learning treinado.

### Previsão da Saúde da Planta (`/saude`)
O endpoint `/saude` é um dos principais recursos da API. Ele recebe, via requisição POST, um conjunto de dados ambientais e retorna se a planta está saudável ou não, com base em um modelo de Machine Learning.

- **Entrada esperada (JSON):**
```json
{
  "serial": "<serial_do_sensor>",
  "soil_humidity": 45.0,
  "temperature": 24.5,
  "humidity": 60.0,
  "lux": 300.0
}
```

- **Processamento:**
  - A API extrai os valores enviados e os repassa para o modelo de Machine Learning.
  - O modelo analisa os dados e retorna uma previsão booleana: `true` para saudável, `false` para não saudável.

- **Resposta (JSON):**
```json
{
  "saude": true
}
```

### Fluxo de Uso
1. O ESP32 envia uma requisição POST para `/saude` com os dados dos sensores.
2. A API processa os dados, executa o modelo de Machine Learning e retorna a resposta indicando a saúde da planta.

Esse mecanismo permite que o sistema forneça feedback inteligente e em tempo real sobre o estado da planta, tanto para o usuário local (via LCD) quanto remoto (via dashboard).

