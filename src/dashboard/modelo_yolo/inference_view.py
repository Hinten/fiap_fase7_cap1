"""
View do dashboard para realizar inferência com modelos YOLO treinados.
"""
import logging
import os
import io
from typing import Optional
import streamlit as st
from PIL import Image
import numpy as np

try:
    from src.modelo_yolo.model_loader import (
        YOLOModelLoader, 
        realizar_inferencia,
        YOLO_AVAILABLE
    )
except ImportError as e:
    logging.error(f"Erro ao importar YOLOModelLoader: {e}")
    YOLO_AVAILABLE = False


def yolo_inference_view():
    """
    View principal para realizar inferência com modelos YOLO.
    Permite carregar modelos, fazer upload de imagens e visualizar predições.
    """
    st.title("🎯 Inferência com Modelos YOLO")
    
    st.write(
        "Nesta página, você pode carregar modelos YOLO treinados e realizar "
        "detecção de objetos em imagens."
    )
    
    # Verifica se ultralytics está disponível
    if not YOLO_AVAILABLE:
        st.error(
            "⚠️ A biblioteca Ultralytics não está instalada. "
            "Por favor, instale com: `pip install ultralytics`"
        )
        st.info(
            "📝 Adicione `ultralytics==8.0.196` ao arquivo requirements.txt "
            "e execute `pip install -r requirements.txt`"
        )
        return
    
    # Seção 1: Seleção do Modelo
    st.header("1️⃣ Selecionar Modelo")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Lista modelos disponíveis
        available_models = YOLOModelLoader.list_available_models()
        
        if not available_models:
            st.warning(
                f"⚠️ Nenhum modelo encontrado no diretório: "
                f"`{YOLOModelLoader.get_models_directory()}`\n\n"
                "Por favor, coloque seus modelos .pt treinados neste diretório."
            )
            
            # Opção de upload de modelo
            st.subheader("Upload de Modelo")
            uploaded_model = st.file_uploader(
                "Faça upload de um modelo YOLO (.pt)",
                type=['pt'],
                help="Selecione um arquivo .pt de modelo YOLO treinado"
            )
            
            if uploaded_model is not None:
                # Salva o modelo no diretório correto
                models_dir = YOLOModelLoader.get_models_directory()
                os.makedirs(models_dir, exist_ok=True)
                
                model_path = os.path.join(models_dir, uploaded_model.name)
                
                with open(model_path, "wb") as f:
                    f.write(uploaded_model.getbuffer())
                
                st.success(f"✅ Modelo salvo em: {model_path}")
                st.info("🔄 Recarregue a página para ver o modelo na lista.")
                return
        else:
            # Seleção de modelo
            selected_model = st.selectbox(
                "Selecione um modelo treinado:",
                options=available_models,
                format_func=lambda x: x.replace('.pt', ''),
                help="Escolha um dos modelos YOLO disponíveis"
            )
            
            if selected_model:
                model_path = os.path.join(
                    YOLOModelLoader.get_models_directory(),
                    selected_model
                )
                
                # Mostra informações do modelo
                model_info = YOLOModelLoader.get_model_info(model_path)
                st.info(
                    f"📦 **Modelo:** {model_info['filename']}  \n"
                    f"💾 **Tamanho:** {model_info['size_mb']} MB"
                )
    
    with col2:
        # Botão para upload adicional de modelo
        st.subheader("Adicionar Modelo")
        uploaded_model = st.file_uploader(
            "Upload .pt",
            type=['pt'],
            key="upload_additional_model",
            label_visibility="collapsed"
        )
        
        if uploaded_model is not None:
            models_dir = YOLOModelLoader.get_models_directory()
            os.makedirs(models_dir, exist_ok=True)
            
            model_path = os.path.join(models_dir, uploaded_model.name)
            
            with open(model_path, "wb") as f:
                f.write(uploaded_model.getbuffer())
            
            st.success("✅ Salvo!")
            st.rerun()
    
    if not available_models:
        return
    
    # Seção 2: Upload de Imagem
    st.header("2️⃣ Selecionar Imagem")
    
    uploaded_image = st.file_uploader(
        "Faça upload de uma imagem para análise",
        type=['jpg', 'jpeg', 'png', 'bmp'],
        help="Formatos suportados: JPG, JPEG, PNG, BMP"
    )
    
    if uploaded_image is None:
        st.info("👆 Faça upload de uma imagem para começar a análise")
        return
    
    # Carrega e exibe a imagem original
    image = Image.open(uploaded_image)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📷 Imagem Original")
        st.image(image, use_container_width=True)
    
    # Seção 3: Configurações de Inferência
    st.header("3️⃣ Configurações de Detecção")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        conf_threshold = st.slider(
            "Confiança Mínima",
            min_value=0.0,
            max_value=1.0,
            value=0.25,
            step=0.05,
            help="Detecções com confiança abaixo deste valor serão descartadas"
        )
    
    with col2:
        iou_threshold = st.slider(
            "IoU (NMS)",
            min_value=0.0,
            max_value=1.0,
            value=0.45,
            step=0.05,
            help="Limiar de IoU para Non-Maximum Suppression"
        )
    
    with col3:
        max_det = st.number_input(
            "Detecções Máximas",
            min_value=1,
            max_value=1000,
            value=300,
            step=10,
            help="Número máximo de detecções por imagem"
        )
    
    # Seção 4: Realizar Inferência
    st.header("4️⃣ Realizar Detecção")
    
    if st.button("🚀 Detectar Objetos", type="primary", use_container_width=True):
        with st.spinner("🔄 Carregando modelo e realizando inferência..."):
            try:
                # Carrega o modelo
                model_path = os.path.join(
                    YOLOModelLoader.get_models_directory(),
                    selected_model
                )
                model = YOLOModelLoader.load_model(model_path)
                
                # Converte imagem PIL para numpy array
                image_np = np.array(image)
                
                # Realiza inferência
                results = realizar_inferencia(
                    model,
                    image_np,
                    conf_threshold=conf_threshold,
                    iou_threshold=iou_threshold,
                    max_det=max_det
                )
                
                # Processa resultados
                if results and len(results) > 0:
                    result = results[0]
                    
                    # Renderiza imagem com detecções
                    annotated_image = result.plot()
                    
                    # Converte de BGR para RGB (OpenCV -> PIL)
                    annotated_image_rgb = Image.fromarray(annotated_image[..., ::-1])
                    
                    with col2:
                        st.subheader("🎯 Detecções")
                        st.image(annotated_image_rgb, use_container_width=True)
                    
                    # Mostra estatísticas
                    st.success("✅ Inferência concluída com sucesso!")
                    
                    # Extrai informações das detecções
                    boxes = result.boxes
                    num_detections = len(boxes)
                    
                    st.subheader("📊 Resultados da Detecção")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Total de Detecções", num_detections)
                    
                    with col2:
                        if num_detections > 0:
                            avg_conf = float(boxes.conf.mean())
                            st.metric("Confiança Média", f"{avg_conf:.2%}")
                        else:
                            st.metric("Confiança Média", "N/A")
                    
                    with col3:
                        if num_detections > 0:
                            max_conf = float(boxes.conf.max())
                            st.metric("Confiança Máxima", f"{max_conf:.2%}")
                        else:
                            st.metric("Confiança Máxima", "N/A")
                    
                    # Tabela de detecções
                    if num_detections > 0:
                        st.subheader("🔍 Detalhes das Detecções")
                        
                        detections_data = []
                        for i, box in enumerate(boxes):
                            class_id = int(box.cls[0])
                            confidence = float(box.conf[0])
                            class_name = result.names[class_id]
                            
                            detections_data.append({
                                "#": i + 1,
                                "Classe": class_name,
                                "Confiança": f"{confidence:.2%}",
                                "Coordenadas (x1, y1, x2, y2)": 
                                    f"({int(box.xyxy[0][0])}, {int(box.xyxy[0][1])}, "
                                    f"{int(box.xyxy[0][2])}, {int(box.xyxy[0][3])})"
                            })
                        
                        st.dataframe(detections_data, use_container_width=True)
                    else:
                        st.warning("⚠️ Nenhum objeto detectado com os parâmetros atuais.")
                        st.info(
                            "💡 Tente diminuir o limite de confiança ou ajustar "
                            "os outros parâmetros."
                        )
                    
                    # Botão para download da imagem anotada
                    st.subheader("💾 Download")
                    
                    # Converte imagem para bytes
                    img_byte_arr = io.BytesIO()
                    annotated_image_rgb.save(img_byte_arr, format='PNG')
                    img_byte_arr = img_byte_arr.getvalue()
                    
                    st.download_button(
                        label="📥 Baixar Imagem com Detecções",
                        data=img_byte_arr,
                        file_name=f"deteccoes_{uploaded_image.name}",
                        mime="image/png",
                        use_container_width=True
                    )
                    
                else:
                    st.error("⚠️ Erro ao processar resultados da inferência.")
                    
            except Exception as e:
                st.error(f"❌ Erro durante a inferência: {str(e)}")
                logging.error(f"Erro na inferência YOLO: {str(e)}", exc_info=True)
                
                # Mostra informações de debug em modo de desenvolvimento
                if os.getenv('DEBUG', 'false').lower() == 'true':
                    st.exception(e)


# Cria a página do Streamlit
yolo_inference_page = st.Page(
    yolo_inference_view,
    title="Inferência YOLO",
    url_path="yolo_inference",
    icon="🎯"
)
