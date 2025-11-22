"""
AWS Rekognition Image Analyzer
================================

Este módulo implementa a integração com o AWS Rekognition para análise de imagens.
O AWS Rekognition é um serviço de análise de imagens e vídeos baseado em deep learning
que pode detectar objetos, cenas, textos, rostos, e muito mais.

Principais funcionalidades implementadas:
- Detecção de rótulos (labels) em imagens
- Detecção de rostos e análise de atributos faciais
- Detecção de texto em imagens (OCR)
- Análise de moderação de conteúdo
- Comparação de rostos

Autor: FIAP - Fase 7 Cap 1
Data: 2025
"""

import boto3
import json
from typing import Dict, List, Optional, Union
from pathlib import Path
import logging

# Configuração de logging para rastreamento de operações
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RekognitionAnalyzer:
    """
    Classe principal para interação com o AWS Rekognition.
    
    Esta classe encapsula as funcionalidades do boto3 para o serviço Rekognition,
    fornecendo métodos simplificados para análise de imagens.
    
    Atributos:
        rekognition_client: Cliente boto3 para o serviço Rekognition
        s3_client: Cliente boto3 para o serviço S3 (para imagens armazenadas)
        region: Região AWS onde os serviços estão configurados
    """
    
    def __init__(self, region_name: str = 'us-east-1'):
        """
        Inicializa o cliente AWS Rekognition.
        
        Args:
            region_name: Região AWS a ser utilizada. Padrão: 'us-east-1'
                        Importante: No AWS Learner Lab, use a região disponível.
        
        Nota:
            As credenciais AWS são obtidas automaticamente através de:
            1. Variáveis de ambiente (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            2. Arquivo ~/.aws/credentials
            3. IAM Role (se executando em EC2)
        """
        try:
            # Inicializa o cliente Rekognition
            # Este cliente é responsável por todas as operações de análise de imagem
            self.rekognition_client = boto3.client(
                'rekognition',
                region_name=region_name
            )
            
            # Inicializa o cliente S3 para operações com buckets
            # Útil quando as imagens estão armazenadas no S3
            self.s3_client = boto3.client(
                's3',
                region_name=region_name
            )
            
            self.region = region_name
            logger.info(f"Cliente Rekognition inicializado com sucesso na região {region_name}")
            
        except Exception as e:
            logger.error(f"Erro ao inicializar cliente Rekognition: {str(e)}")
            raise
    
    def detect_labels(
        self,
        image_path: Optional[str] = None,
        image_bytes: Optional[bytes] = None,
        s3_bucket: Optional[str] = None,
        s3_key: Optional[str] = None,
        max_labels: int = 10,
        min_confidence: float = 80.0
    ) -> Dict:
        """
        Detecta objetos, cenas e conceitos em uma imagem.
        
        Esta é uma das funcionalidades mais utilizadas do Rekognition.
        O serviço retorna uma lista de labels (rótulos) identificados na imagem,
        cada um com um nível de confiança associado.
        
        Args:
            image_path: Caminho local para a imagem (opção 1)
            image_bytes: Bytes da imagem em memória (opção 2)
            s3_bucket: Nome do bucket S3 (opção 3)
            s3_key: Chave/caminho da imagem no S3 (opção 3)
            max_labels: Número máximo de labels a retornar (padrão: 10)
            min_confidence: Confiança mínima para incluir um label (0-100, padrão: 80)
        
        Returns:
            Dicionário contendo os labels detectados e metadados
            
        Exemplo de retorno:
            {
                'Labels': [
                    {
                        'Name': 'Person',
                        'Confidence': 99.8,
                        'Instances': [...],
                        'Parents': [...]
                    },
                    ...
                ],
                'LabelModelVersion': '3.0'
            }
        
        Raises:
            ValueError: Se nenhuma fonte de imagem for fornecida
            Exception: Erros de comunicação com a API
        """
        try:
            # Prepara o objeto Image de acordo com a fonte fornecida
            image_input = self._prepare_image_input(
                image_path, image_bytes, s3_bucket, s3_key
            )
            
            logger.info(f"Detectando labels na imagem (max: {max_labels}, min confidence: {min_confidence}%)")
            
            # Chama a API do Rekognition para detectar labels
            # MaxLabels: limita quantos labels retornar
            # MinConfidence: filtra labels com confiança abaixo do limiar
            response = self.rekognition_client.detect_labels(
                Image=image_input,
                MaxLabels=max_labels,
                MinConfidence=min_confidence
            )
            
            logger.info(f"Detectados {len(response['Labels'])} labels")
            
            return response
            
        except Exception as e:
            logger.error(f"Erro ao detectar labels: {str(e)}")
            raise
    
    def detect_faces(
        self,
        image_path: Optional[str] = None,
        image_bytes: Optional[bytes] = None,
        s3_bucket: Optional[str] = None,
        s3_key: Optional[str] = None,
        attributes: List[str] = ['ALL']
    ) -> Dict:
        """
        Detecta rostos em uma imagem e analisa seus atributos.
        
        O Rekognition pode detectar múltiplos rostos em uma imagem e analisar
        diversos atributos como idade estimada, emoções, uso de óculos, etc.
        
        Args:
            image_path: Caminho local para a imagem
            image_bytes: Bytes da imagem em memória
            s3_bucket: Nome do bucket S3
            s3_key: Chave da imagem no S3
            attributes: Lista de atributos a analisar. Opções:
                       - ['ALL']: Todos os atributos (padrão)
                       - ['DEFAULT']: Atributos básicos
                       
        Returns:
            Dicionário com informações sobre os rostos detectados
            
        Atributos analisados:
            - BoundingBox: Localização do rosto na imagem
            - AgeRange: Faixa etária estimada
            - Smile: Se está sorrindo
            - Eyeglasses: Se usa óculos
            - Sunglasses: Se usa óculos escuros
            - Gender: Gênero estimado
            - Beard: Se tem barba
            - Mustache: Se tem bigode
            - EyesOpen: Se os olhos estão abertos
            - MouthOpen: Se a boca está aberta
            - Emotions: Emoções detectadas (feliz, triste, etc.)
            - Landmarks: Pontos de referência faciais (olhos, nariz, boca)
            - Pose: Orientação do rosto
            - Quality: Qualidade da imagem do rosto
            - Confidence: Confiança na detecção
        """
        try:
            image_input = self._prepare_image_input(
                image_path, image_bytes, s3_bucket, s3_key
            )
            
            logger.info("Detectando rostos na imagem")
            
            # Chama a API para detectar rostos
            # Attributes especifica quais atributos faciais analisar
            response = self.rekognition_client.detect_faces(
                Image=image_input,
                Attributes=attributes
            )
            
            logger.info(f"Detectados {len(response['FaceDetails'])} rostos")
            
            return response
            
        except Exception as e:
            logger.error(f"Erro ao detectar rostos: {str(e)}")
            raise
    
    def detect_text(
        self,
        image_path: Optional[str] = None,
        image_bytes: Optional[bytes] = None,
        s3_bucket: Optional[str] = None,
        s3_key: Optional[str] = None,
        min_confidence: float = 80.0
    ) -> Dict:
        """
        Detecta e extrai texto de uma imagem (OCR - Optical Character Recognition).
        
        Útil para:
        - Digitalização de documentos
        - Leitura de placas
        - Extração de texto de imagens
        - Análise de letreiros e sinalizações
        
        Args:
            image_path: Caminho local para a imagem
            image_bytes: Bytes da imagem em memória
            s3_bucket: Nome do bucket S3
            s3_key: Chave da imagem no S3
            min_confidence: Confiança mínima para incluir texto detectado
        
        Returns:
            Dicionário contendo:
            - TextDetections: Lista de textos detectados
                - DetectedText: O texto propriamente dito
                - Type: 'LINE' ou 'WORD'
                - Id: Identificador único
                - Confidence: Nível de confiança
                - Geometry: Localização do texto na imagem
        """
        try:
            image_input = self._prepare_image_input(
                image_path, image_bytes, s3_bucket, s3_key
            )
            
            logger.info("Detectando texto na imagem")
            
            # Chama a API para detectar texto
            # Filters pode ser usado para filtrar por confiança, tipo, etc.
            response = self.rekognition_client.detect_text(
                Image=image_input,
                Filters={
                    'WordFilter': {
                        'MinConfidence': min_confidence
                    }
                }
            )
            
            logger.info(f"Detectados {len(response['TextDetections'])} textos")
            
            return response
            
        except Exception as e:
            logger.error(f"Erro ao detectar texto: {str(e)}")
            raise
    
    def detect_moderation_labels(
        self,
        image_path: Optional[str] = None,
        image_bytes: Optional[bytes] = None,
        s3_bucket: Optional[str] = None,
        s3_key: Optional[str] = None,
        min_confidence: float = 60.0
    ) -> Dict:
        """
        Detecta conteúdo impróprio ou inseguro em imagens.
        
        Esta funcionalidade é útil para:
        - Moderação de conteúdo em redes sociais
        - Filtragem de imagens em plataformas
        - Compliance e segurança
        
        Categorias detectadas:
        - Explicit Nudity: Nudez explícita
        - Suggestive: Conteúdo sugestivo
        - Violence: Violência
        - Visually Disturbing: Visualmente perturbador
        - Rude Gestures: Gestos ofensivos
        - Drugs: Drogas
        - Tobacco: Tabaco
        - Alcohol: Álcool
        - Gambling: Jogos de azar
        - Hate Symbols: Símbolos de ódio
        
        Args:
            image_path: Caminho local para a imagem
            image_bytes: Bytes da imagem em memória
            s3_bucket: Nome do bucket S3
            s3_key: Chave da imagem no S3
            min_confidence: Confiança mínima para incluir label de moderação
        
        Returns:
            Dicionário com labels de moderação detectados
        """
        try:
            image_input = self._prepare_image_input(
                image_path, image_bytes, s3_bucket, s3_key
            )
            
            logger.info("Analisando conteúdo da imagem para moderação")
            
            # Chama a API para detectar conteúdo impróprio
            response = self.rekognition_client.detect_moderation_labels(
                Image=image_input,
                MinConfidence=min_confidence
            )
            
            logger.info(f"Detectados {len(response['ModerationLabels'])} labels de moderação")
            
            return response
            
        except Exception as e:
            logger.error(f"Erro ao detectar labels de moderação: {str(e)}")
            raise
    
    def compare_faces(
        self,
        source_image_path: Optional[str] = None,
        target_image_path: Optional[str] = None,
        source_bytes: Optional[bytes] = None,
        target_bytes: Optional[bytes] = None,
        similarity_threshold: float = 80.0
    ) -> Dict:
        """
        Compara rostos entre duas imagens.
        
        Esta funcionalidade é útil para:
        - Verificação de identidade
        - Controle de acesso
        - Busca de pessoas em banco de imagens
        
        Args:
            source_image_path: Caminho da imagem de origem (referência)
            target_image_path: Caminho da imagem alvo (para comparação)
            source_bytes: Bytes da imagem de origem
            target_bytes: Bytes da imagem alvo
            similarity_threshold: Limiar de similaridade (0-100)
        
        Returns:
            Dicionário contendo:
            - SourceImageFace: Informações do rosto de origem
            - FaceMatches: Lista de rostos correspondentes na imagem alvo
                - Similarity: Porcentagem de similaridade
                - Face: Detalhes do rosto correspondente
            - UnmatchedFaces: Rostos na imagem alvo que não correspondem
        """
        try:
            # Prepara imagem de origem
            if source_image_path:
                with open(source_image_path, 'rb') as f:
                    source_bytes = f.read()
            elif source_bytes is None:
                raise ValueError("É necessário fornecer source_image_path ou source_bytes")
            
            # Prepara imagem alvo
            if target_image_path:
                with open(target_image_path, 'rb') as f:
                    target_bytes = f.read()
            elif target_bytes is None:
                raise ValueError("É necessário fornecer target_image_path ou target_bytes")
            
            logger.info("Comparando rostos entre duas imagens")
            
            # Chama a API para comparar rostos
            # SimilarityThreshold: apenas retorna matches acima deste limiar
            response = self.rekognition_client.compare_faces(
                SourceImage={'Bytes': source_bytes},
                TargetImage={'Bytes': target_bytes},
                SimilarityThreshold=similarity_threshold
            )
            
            matches = len(response['FaceMatches'])
            unmatched = len(response['UnmatchedFaces'])
            logger.info(f"Encontrados {matches} matches, {unmatched} rostos não correspondentes")
            
            return response
            
        except Exception as e:
            logger.error(f"Erro ao comparar rostos: {str(e)}")
            raise
    
    def _prepare_image_input(
        self,
        image_path: Optional[str],
        image_bytes: Optional[bytes],
        s3_bucket: Optional[str],
        s3_key: Optional[str]
    ) -> Dict:
        """
        Método auxiliar para preparar o input de imagem para a API.
        
        O Rekognition aceita imagens de três formas:
        1. Bytes da imagem (até 5MB)
        2. Referência ao S3 (sem limite de tamanho, mas imagem deve estar no S3)
        
        Args:
            image_path: Caminho local da imagem
            image_bytes: Bytes da imagem
            s3_bucket: Bucket S3
            s3_key: Chave no S3
        
        Returns:
            Dicionário no formato esperado pela API
        
        Raises:
            ValueError: Se nenhuma fonte válida for fornecida
        """
        # Opção 1: Imagem no S3
        if s3_bucket and s3_key:
            logger.debug(f"Usando imagem do S3: s3://{s3_bucket}/{s3_key}")
            return {
                'S3Object': {
                    'Bucket': s3_bucket,
                    'Name': s3_key
                }
            }
        
        # Opção 2: Imagem em bytes
        if image_bytes:
            logger.debug("Usando imagem de bytes em memória")
            return {'Bytes': image_bytes}
        
        # Opção 3: Imagem de arquivo local
        if image_path:
            logger.debug(f"Lendo imagem do arquivo: {image_path}")
            with open(image_path, 'rb') as image_file:
                return {'Bytes': image_file.read()}
        
        # Nenhuma fonte fornecida
        raise ValueError(
            "É necessário fornecer pelo menos uma fonte de imagem: "
            "image_path, image_bytes, ou (s3_bucket + s3_key)"
        )
    
    def format_labels_output(self, response: Dict) -> str:
        """
        Formata a saída de detect_labels de forma legível.
        
        Args:
            response: Resposta da API detect_labels
        
        Returns:
            String formatada com os labels detectados
        """
        output = "\n=== LABELS DETECTADOS ===\n\n"
        
        for label in response['Labels']:
            output += f"• {label['Name']}: {label['Confidence']:.2f}% de confiança\n"
            
            if label.get('Parents'):
                parents = [p['Name'] for p in label['Parents']]
                output += f"  Categorias: {', '.join(parents)}\n"
            
            if label.get('Instances'):
                output += f"  Instâncias detectadas: {len(label['Instances'])}\n"
            
            output += "\n"
        
        return output
    
    def format_faces_output(self, response: Dict) -> str:
        """
        Formata a saída de detect_faces de forma legível.
        
        Args:
            response: Resposta da API detect_faces
        
        Returns:
            String formatada com informações dos rostos
        """
        output = f"\n=== ROSTOS DETECTADOS: {len(response['FaceDetails'])} ===\n\n"
        
        for idx, face in enumerate(response['FaceDetails'], 1):
            output += f"Rosto {idx}:\n"
            output += f"  Confiança: {face['Confidence']:.2f}%\n"
            
            if 'AgeRange' in face:
                output += f"  Idade estimada: {face['AgeRange']['Low']}-{face['AgeRange']['High']} anos\n"
            
            if 'Gender' in face:
                output += f"  Gênero: {face['Gender']['Value']} ({face['Gender']['Confidence']:.1f}%)\n"
            
            if 'Emotions' in face:
                emotions = sorted(face['Emotions'], key=lambda x: x['Confidence'], reverse=True)
                top_emotion = emotions[0]
                output += f"  Emoção principal: {top_emotion['Type']} ({top_emotion['Confidence']:.1f}%)\n"
            
            if 'Smile' in face:
                output += f"  Sorrindo: {'Sim' if face['Smile']['Value'] else 'Não'} ({face['Smile']['Confidence']:.1f}%)\n"
            
            if 'Eyeglasses' in face:
                output += f"  Óculos: {'Sim' if face['Eyeglasses']['Value'] else 'Não'} ({face['Eyeglasses']['Confidence']:.1f}%)\n"
            
            output += "\n"
        
        return output
    
    def format_text_output(self, response: Dict) -> str:
        """
        Formata a saída de detect_text de forma legível.
        
        Args:
            response: Resposta da API detect_text
        
        Returns:
            String formatada com os textos detectados
        """
        output = "\n=== TEXTOS DETECTADOS ===\n\n"
        
        # Agrupa por linhas
        lines = [t for t in response['TextDetections'] if t['Type'] == 'LINE']
        
        for text in lines:
            output += f"• {text['DetectedText']}\n"
            output += f"  Confiança: {text['Confidence']:.2f}%\n\n"
        
        return output


def main():
    """
    Função principal para demonstração do uso da classe RekognitionAnalyzer.
    
    Esta função serve como exemplo de uso e pode ser executada diretamente
    para testar as funcionalidades básicas do Rekognition.
    """
    print("=" * 60)
    print("AWS Rekognition - Demonstração")
    print("=" * 60)
    print()
    
    try:
        # Inicializa o analisador
        print("Inicializando conexão com AWS Rekognition...")
        analyzer = RekognitionAnalyzer(region_name='us-east-1')
        print("✓ Conexão estabelecida com sucesso!\n")
        
        # Exemplo de uso com arquivo local
        # Descomente as linhas abaixo para testar com uma imagem real
        """
        image_path = "../examples/sample_image.jpg"
        
        # Detecta labels
        print("1. Detectando objetos e cenas...")
        labels_response = analyzer.detect_labels(image_path=image_path)
        print(analyzer.format_labels_output(labels_response))
        
        # Detecta rostos
        print("2. Detectando e analisando rostos...")
        faces_response = analyzer.detect_faces(image_path=image_path)
        print(analyzer.format_faces_output(faces_response))
        
        # Detecta texto
        print("3. Detectando texto (OCR)...")
        text_response = analyzer.detect_text(image_path=image_path)
        print(analyzer.format_text_output(text_response))
        """
        
        print("Para usar este script, descomente as linhas de exemplo")
        print("e forneça o caminho para uma imagem de teste.")
        
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
        print("\nVerifique se:")
        print("1. As credenciais AWS estão configuradas corretamente")
        print("2. A região está correta")
        print("3. O serviço Rekognition está disponível na sua conta")


if __name__ == "__main__":
    main()
