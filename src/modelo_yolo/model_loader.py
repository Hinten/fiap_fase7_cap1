"""
Utilitário para carregar e gerenciar modelos YOLO treinados.
"""
import os
import logging
from typing import Optional, List
from pathlib import Path

try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False
    logging.warning("Ultralytics não está instalado. Instale com: pip install ultralytics")


class YOLOModelLoader:
    """Classe para gerenciar o carregamento e cache de modelos YOLO."""
    
    _model_cache = {}
    
    @staticmethod
    def get_models_directory() -> str:
        """Retorna o diretório padrão onde os modelos treinados devem ser armazenados."""
        return os.path.join("src", "modelo_yolo", "modelos_treinados")
    
    @staticmethod
    def list_available_models() -> List[str]:
        """
        Lista todos os modelos .pt disponíveis no diretório de modelos.
        
        Returns:
            Lista de nomes de arquivos de modelos (.pt)
        """
        models_dir = YOLOModelLoader.get_models_directory()
        
        if not os.path.exists(models_dir):
            os.makedirs(models_dir, exist_ok=True)
            return []
        
        models = [f for f in os.listdir(models_dir) if f.endswith('.pt')]
        return sorted(models)
    
    @staticmethod
    def load_model(model_path: str, use_cache: bool = True) -> Optional[object]:
        """
        Carrega um modelo YOLO do arquivo especificado.
        
        Args:
            model_path: Caminho para o arquivo .pt do modelo
            use_cache: Se True, usa cache para evitar recarregar o mesmo modelo
            
        Returns:
            Objeto do modelo YOLO carregado ou None se houver erro
        """
        if not YOLO_AVAILABLE:
            raise ImportError(
                "Ultralytics não está instalado. "
                "Instale com: pip install ultralytics"
            )
        
        # Verifica se o arquivo existe
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Modelo não encontrado: {model_path}")
        
        # Usa cache se solicitado
        if use_cache and model_path in YOLOModelLoader._model_cache:
            logging.info(f"Usando modelo em cache: {model_path}")
            return YOLOModelLoader._model_cache[model_path]
        
        try:
            logging.info(f"Carregando modelo YOLO: {model_path}")
            model = YOLO(model_path)
            
            # Adiciona ao cache
            if use_cache:
                YOLOModelLoader._model_cache[model_path] = model
            
            return model
        except Exception as e:
            logging.error(f"Erro ao carregar modelo {model_path}: {str(e)}")
            raise
    
    @staticmethod
    def clear_cache():
        """Limpa o cache de modelos carregados."""
        YOLOModelLoader._model_cache.clear()
        logging.info("Cache de modelos YOLO limpo")
    
    @staticmethod
    def get_model_info(model_path: str) -> dict:
        """
        Obtém informações sobre um modelo sem carregá-lo completamente.
        
        Args:
            model_path: Caminho para o arquivo do modelo
            
        Returns:
            Dicionário com informações do modelo
        """
        if not os.path.exists(model_path):
            return {"error": "Arquivo não encontrado"}
        
        file_size = os.path.getsize(model_path)
        file_size_mb = file_size / (1024 * 1024)
        
        return {
            "path": model_path,
            "filename": os.path.basename(model_path),
            "size_mb": round(file_size_mb, 2),
            "exists": True
        }


def realizar_inferencia(model, image_source, conf_threshold: float = 0.25, 
                       iou_threshold: float = 0.45, max_det: int = 300):
    """
    Realiza inferência com um modelo YOLO em uma imagem.
    
    Args:
        model: Modelo YOLO carregado
        image_source: Caminho da imagem ou array numpy
        conf_threshold: Limite de confiança para detecções (0-1)
        iou_threshold: Limite de IoU para NMS
        max_det: Número máximo de detecções
        
    Returns:
        Resultados da predição do YOLO
    """
    try:
        results = model.predict(
            source=image_source,
            conf=conf_threshold,
            iou=iou_threshold,
            max_det=max_det,
            verbose=False
        )
        return results
    except Exception as e:
        logging.error(f"Erro durante inferência: {str(e)}")
        raise
