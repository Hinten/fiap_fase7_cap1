# Ir Além 1

## 🌱 Sistema de Monitoramento de Estufa

#### 🎥 Vídeo Explicativo

- **Ir Além 1 🌱 Sistema de Monitoramento de Estufa:** [https://www.youtube.com/watch?v=QsNpCC74HIo](https://www.youtube.com/watch?v=QsNpCC74HIo) *(não listado)*


Este projeto implementa um sistema de monitoramento para estufas utilizando o microcontrolador ESP32. Ele coleta dados de **temperatura** e **umidade do ar** através do sensor DHT11, disponibilizando essas informações em tempo real por meio de um dashboard web acessível via Wi-Fi.

---

### 📁 Estrutura do Projeto

```
ir_alem_1
├── src
│   ├── greenhouse_monitor.ino      # Código principal do ESP32
│   ├── config
│   │   └── wifi_credentials.h      # SSID e senha do Wi-Fi
├── include
│   ├── sensors.h                   # Funções do sensor DHT11
│   └── web_server.h                # Rotas do servidor web
├── data
│   └── dashboard.html              # Dashboard HTML para visualização dos dados
├── platformio.ini                  # Configuração do PlatformIO
├── README.md                       # Documentação do projeto
├── LICENSE                         # Licença
```

---

### 🚀 Funcionalidades

- 📡 Mede temperatura e umidade do ar usando o sensor DHT11
- 🌐 Conecta o ESP32 à rede Wi-Fi
- 📊 Disponibiliza um dashboard web com atualização automática dos dados

---

### ⚙️ Como Funciona

1. O ESP32 conecta-se à rede Wi-Fi configurada.
2. Os sensores coletam dados ambientais periodicamente.
3. Um servidor web integrado exibe os dados em tempo real em um dashboard acessível por qualquer dispositivo na mesma rede.

---

### 📦 Requisitos

- ESP32
- Sensor DHT11
- PlatformIO instalado

---

### 👨‍💻 Como Executar

1. Configure o arquivo `wifi_credentials.h` com o SSID e senha da sua rede Wi-Fi.
2. Faça o upload do código para o ESP32 usando o PlatformIO.
3. Acesse o dashboard pelo endereço IP exibido no monitor serial após a conexão.

---

### 📄 Licença

Este projeto está licenciado sob os termos do arquivo [LICENSE](./LICENSE).
