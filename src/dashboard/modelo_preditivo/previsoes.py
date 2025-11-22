import logging
import datetime
import streamlit as st
import os

from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
from src.settings import DEBUG
from src.notificacoes.email import enviar_email


def modelo_preditivo_view():
    """
    View para realizar previsões manuais com o modelo preditivo.
    :return:
    """

    st.title("🔮 Previsão Manual com Modelo Preditivo")

    st.write("Nesta página, você pode realizar previsões manuais utilizando o modelo preditivo treinado.")

    #pega os modelos em src/modelo_preditivo/modelos_otimizados_salvos

    if not os.path.exists("src/modelo_preditivo/modelos_otimizados_salvos"):
        st.error("⚠️ Modelo preditivo não encontrado. Por favor, treine o modelo antes de realizar previsões.")
        return

    modelos_paths = [f for f in os.listdir("src/modelo_preditivo/modelos_otimizados_salvos") if f.endswith('.pkl')]

    # Carrega o modelo preditivo
    modelo_selecionado = st.selectbox(
        "Selecione o modelo preditivo:",
        options=modelos_paths,
        format_func=lambda x: x.replace('.pkl', '')  # Exibe o nome do modelo sem a extensão
    )

    if not modelo_selecionado:
        st.error("⚠️ Nenhum modelo selecionado.")
        return

    modelo_selecionado_full_path = os.path.join("src/modelo_preditivo/modelos_salvos", modelo_selecionado)

    data_leitura = st.date_input("Data da leitura:", value=datetime.date.today())
    hora_leitura = st.time_input("Hora da leitura:", value=datetime.datetime.now().time())
    fosforo = st.number_input("Fósforo (0 ou 1):", min_value=0, max_value=1, value=1)
    potassio = st.number_input("Potássio (0 ou 1):", min_value=0, max_value=1, value=1)
    ph = st.number_input("pH (0 ou 1):", min_value=0, max_value=1, value=1)
    umidade = st.number_input("Umidade do solo:", min_value=0.0, value=45.5)

    # Combina data e hora em um datetime
    hora_leitura_dt = datetime.datetime.combine(data_leitura, hora_leitura)

    # Seção de Notificação por E-mail
    st.divider()
    st.subheader("📧 Notificação por E-mail")
    
    enviar_email_checkbox = st.checkbox(
        "Enviar notificação por e-mail após a previsão",
        value=False,
        help="Marque esta opção para receber um e-mail com o resultado da previsão"
    )
    
    if enviar_email_checkbox:
        # Validar variáveis de ambiente necessárias
        sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
        sns_region = os.environ.get('SNS_REGION')
        
        if not sns_topic_arn or not sns_region:
            st.warning("⚠️ As variáveis de ambiente SNS_TOPIC_ARN e SNS_REGION devem estar configuradas para enviar e-mails.")
        
        # Campos de entrada para assunto e mensagem
        assunto_padrao = "Resultado da Previsão de Irrigação"
        mensagem_padrao = "A previsão de irrigação foi realizada com os seguintes parâmetros:\n\n" + \
                         f"Data/Hora: {data_leitura} {hora_leitura}\n" + \
                         f"Fósforo: {fosforo}\n" + \
                         f"Potássio: {potassio}\n" + \
                         f"pH: {ph}\n" + \
                         f"Umidade: {umidade}\n\n" + \
                         "Resultado: [Será preenchido após a previsão]"
        
        email_assunto = st.text_input(
            "Assunto do E-mail:",
            value=assunto_padrao,
            help="Personalize o assunto do e-mail de notificação"
        )
        
        email_mensagem = st.text_area(
            "Mensagem do E-mail:",
            value=mensagem_padrao,
            height=200,
            help="Personalize a mensagem do e-mail. O resultado da previsão será adicionado automaticamente."
        )

    if st.button("Realizar Previsão"):
        try:
            previsao = carregar_modelo_e_realizar_previsao(
                modelo_selecionado_full_path,
                hora_leitura=hora_leitura_dt,
                fosforo=fosforo,
                potassio=potassio,
                ph=ph,
                umidade=umidade
            )
            st.success(f"🔮 Previsão realizada com sucesso!\nPrecisa Irrigar?: {previsao}")
            
            # Enviar e-mail se a opção estiver habilitada
            if enviar_email_checkbox:
                try:
                    # Verificar variáveis de ambiente
                    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
                    sns_region = os.environ.get('SNS_REGION')
                    
                    if not sns_topic_arn or not sns_region:
                        st.error("❌ Não foi possível enviar o e-mail: Variáveis de ambiente SNS_TOPIC_ARN e SNS_REGION não configuradas.")
                    else:
                        # Gerar mensagem com resultado da previsão
                        mensagem_final = email_mensagem
                        if "[Será preenchido após a previsão]" in mensagem_final:
                            mensagem_final = mensagem_final.replace(
                                "[Será preenchido após a previsão]",
                                f"Precisa Irrigar?: {previsao}"
                            )
                        else:
                            mensagem_final += f"\n\n=== RESULTADO DA PREVISÃO ===\nPrecisa Irrigar?: {previsao}"
                        
                        # Atualizar assunto com resultado
                        assunto_final = email_assunto
                        if previsao == "Sim":
                            assunto_final = f"{email_assunto} - ✅ Irrigação Necessária"
                        else:
                            assunto_final = f"{email_assunto} - ⛔ Irrigação Não Necessária"
                        
                        resposta = enviar_email(assunto_final, mensagem_final)
                        st.success(f"✅ E-mail enviado com sucesso! ID da Mensagem: {resposta['MessageId']}")
                        
                except Exception as email_error:
                    st.error(f"❌ Erro ao enviar e-mail: {str(email_error)}")
                    logging.error(f"Erro ao enviar e-mail de notificação: {email_error}")
                    if DEBUG:
                        raise
                        
        except Exception as e:
            st.error(f"⚠️ Erro ao realizar a previsão: {str(e)}")
            logging.error(e)
            if DEBUG:
                raise

previsao_manual_page = st.Page(
    modelo_preditivo_view,
    title="Previsão Manual",
    url_path="previsao_manual"
)