# 🚀 Guia de Início Rápido

## Instalação Rápida (5 minutos)

### 1. Clonar o Repositório

```bash
git clone https://github.com/Hinten/fiap_fase7_cap1.git
cd fiap_fase7_cap1
```

### 2. Criar Ambiente Virtual

```bash
python -m venv .venv

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
# Editar .env com suas credenciais
```

### 5. Setup Banco de Dados (Opcional)

```bash
python scripts/setup_database.py
python scripts/seed_data.py
```

### 6. Iniciar Dashboard

```bash
cd dashboard
streamlit run app.py
```

Acesse: http://localhost:8501

---

## 🐳 Com Docker (Alternativa)

```bash
# Iniciar todos os serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down
```

---

## 📝 Próximos Passos

Após a instalação inicial, siga estas etapas:

1. **Migrar código das fases anteriores** seguindo o [roadmap.md](roadmap/roadmap.md)
2. **Configurar AWS** (SNS, SES, Lambda) conforme documentado
3. **Testar cada serviço** individualmente
4. **Integrar na dashboard** unificada
5. **Gravar vídeo** de apresentação

---

## 🆘 Problemas?

- Consulte o [README.md](README.md) completo
- Leia o [roadmap.md](roadmap/roadmap.md) detalhado
- Veja a documentação em [docs/](docs/)
