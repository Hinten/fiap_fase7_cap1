# Fase 3: IoT e Automação Inteligente

## 📋 Descrição

Sistema IoT completo com ESP32 integrando sensores físicos para irrigação automatizada e inteligente.

## 🎯 Objetivos

- Leitura de sensores (DHT22, LDR)
- Lógica de acionamento automático de irrigação
- API REST para operações CRUD
- Integração com banco de dados
- Simulador de sensores (para testes sem hardware)

## 📂 Estrutura

```
phase3/
├── firmware_esp32/    # Código Arduino/MicroPython para ESP32
├── sensores/          # Simuladores e lógica de sensores
└── api_crud/          # API REST (Flask/FastAPI)
```

## 🤖 Sensores Utilizados

### DHT22
- **Função**: Temperatura e umidade do ar/solo
- **Limiar umidade**: 30% - 80%
- **Limiar temperatura**: 15°C - 35°C

### LDR (Light Dependent Resistor)
- **Função**: Luminosidade (proxy para pH)
- **Limiar**: 200 - 800 lux

### Relé
- **Função**: Acionamento de bomba de irrigação
- **Lógica**: Ativa quando umidade < 30%

## 🔧 Como Usar

### Simulador (Sem Hardware)

```bash
cd phase3/sensores
python simulador.py
```

### API CRUD

```bash
cd phase3/api_crud
python app.py
```

Endpoints disponíveis:
- `GET /api/sensors` - Listar sensores
- `GET /api/sensors/{id}` - Obter sensor
- `POST /api/sensors` - Criar sensor
- `PUT /api/sensors/{id}` - Atualizar sensor
- `DELETE /api/sensors/{id}` - Remover sensor
- `GET /api/readings` - Listar leituras

### Hardware ESP32

1. Abrir `firmware_esp32/main.ino` no Arduino IDE
2. Configurar WiFi credentials
3. Fazer upload para ESP32
4. Monitorar via Serial Monitor

## 📦 Dependências Específicas

```
flask ou fastapi
requests
paho-mqtt
uvicorn (para FastAPI)
```

## 🔗 Repositório Original

[fiap_fase3_cap1-novo](https://github.com/Hinten/fiap_fase3_cap1-novo)

## 📝 O Que Trazer do Repositório Original

- Firmware ESP32 (.ino)
- Scripts de leitura de sensores
- Lógica de irrigação automática
- API CRUD completa
- Simuladores de hardware
