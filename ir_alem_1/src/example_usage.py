"""
Exemplos de Uso do AWS Rekognition
===================================

Este script demonstra diferentes casos de uso do AWS Rekognition,
mostrando como analisar imagens para diversos propósitos.

Casos de uso demonstrados:
1. Análise agrícola: Identificação de culturas e condições de plantio
2. Segurança: Detecção de pessoas e objetos
3. Documentos: Extração de texto (OCR)
4. Moderação: Verificação de conteúdo apropriado
5. Identificação: Comparação de rostos

Autor: FIAP - Fase 7 Cap 1
Data: 2025
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, Any

from aws_config import print_credential_status

# Adiciona o diretório src ao path para imports
sys.path.insert(0, str(Path(__file__).parent))

from rekognition_analyzer import RekognitionAnalyzer


def print_header(title: str):
    """Imprime um cabeçalho formatado"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def analyze_agricultural_image(analyzer: RekognitionAnalyzer, image_path: str):
    """
    Caso de Uso 1: Análise de Imagens Agrícolas
    
    Neste cenário, usamos o Rekognition para identificar:
    - Tipo de cultura plantada
    - Condições da plantação
    - Presença de pragas ou doenças
    - Estado de maturação
    
    Args:
        analyzer: Instância do RekognitionAnalyzer
        image_path: Caminho para a imagem agrícola
    """
    print_header("CASO DE USO 1: Análise de Imagem Agrícola")
    
    print(f"Analisando imagem: {image_path}")
    print("Aguarde enquanto o Rekognition processa a imagem...\n")
    
    # Detecta elementos na imagem com alta confiança
    response = analyzer.detect_labels(
        image_path=image_path,
        max_labels=20,  # Queremos ver mais labels para análise agrícola
        min_confidence=70.0  # Confiança mínima de 70%
    )
    
    # Analisa os resultados buscando termos relacionados à agricultura
    agricultural_terms = [
        'plant', 'crop', 'field', 'farm', 'agriculture',
        'vegetation', 'leaf', 'soil', 'harvest'
    ]
    
    print("📊 Resultados da Análise:\n")
    
    agricultural_labels = []
    for label in response['Labels']:
        label_name_lower = label['Name'].lower()
        
        # Verifica se é um termo agrícola
        is_agricultural = any(term in label_name_lower for term in agricultural_terms)
        
        if is_agricultural:
            agricultural_labels.append(label)
            print(f"🌱 {label['Name']}: {label['Confidence']:.1f}% de confiança")
        else:
            print(f"   {label['Name']}: {label['Confidence']:.1f}% de confiança")
    
    # Gera insights
    print("\n💡 Insights:")
    if agricultural_labels:
        print(f"✓ Detectados {len(agricultural_labels)} elementos agrícolas na imagem")
        print("✓ Esta imagem contém elementos relacionados à agricultura")
    else:
        print("⚠ Nenhum elemento agrícola específico foi detectado")
    
    # Salva resultado completo
    output_file = Path(image_path).stem + "_agricultural_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Resultado completo salvo em: {output_file}")


def analyze_security_image(analyzer: RekognitionAnalyzer, image_path: str):
    """
    Caso de Uso 2: Análise de Segurança
    
    Detecta presença de pessoas e objetos relevantes para segurança:
    - Número de pessoas
    - Veículos
    - Objetos suspeitos
    - Horário (dia/noite)
    
    Args:
        analyzer: Instância do RekognitionAnalyzer
        image_path: Caminho para a imagem de segurança
    """
    print_header("CASO DE USO 2: Análise de Segurança")
    
    print(f"Analisando imagem: {image_path}")
    print("Detectando pessoas e objetos...\n")
    
    # Detecta labels gerais
    labels_response = analyzer.detect_labels(
        image_path=image_path,
        max_labels=15,
        min_confidence=75.0
    )
    
    # Detecta rostos especificamente
    faces_response = analyzer.detect_faces(
        image_path=image_path,
        attributes=['ALL']
    )
    
    print("🔍 Análise de Segurança:\n")
    
    # Conta pessoas e objetos relevantes
    people_count = 0
    vehicles = []
    relevant_objects = []
    
    for label in labels_response['Labels']:
        name = label['Name']
        confidence = label['Confidence']
        
        if name.lower() == 'person':
            people_count = len(label.get('Instances', []))
            print(f"👥 Pessoas detectadas: {people_count}")
            print(f"   Confiança: {confidence:.1f}%")
        
        elif 'vehicle' in name.lower() or name.lower() in ['car', 'truck', 'motorcycle']:
            vehicles.append(name)
            print(f"🚗 Veículo: {name} ({confidence:.1f}%)")
        
        elif name.lower() in ['door', 'window', 'gate', 'entrance']:
            relevant_objects.append(name)
            print(f"🚪 Objeto: {name} ({confidence:.1f}%)")
    
    # Análise facial
    if faces_response['FaceDetails']:
        print(f"\n😊 Rostos detectados: {len(faces_response['FaceDetails'])}")
        
        for idx, face in enumerate(faces_response['FaceDetails'], 1):
            print(f"\n   Rosto {idx}:")
            
            if 'AgeRange' in face:
                print(f"   • Idade estimada: {face['AgeRange']['Low']}-{face['AgeRange']['High']} anos")
            
            if 'Emotions' in face:
                top_emotion = max(face['Emotions'], key=lambda x: x['Confidence'])
                print(f"   • Emoção: {top_emotion['Type']} ({top_emotion['Confidence']:.1f}%)")
    
    # Resumo
    print("\n📋 Resumo da Análise:")
    print(f"   Total de pessoas: {people_count}")
    print(f"   Total de veículos: {len(vehicles)}")
    print(f"   Total de rostos: {len(faces_response['FaceDetails'])}")


def extract_text_from_document(analyzer: RekognitionAnalyzer, image_path: str):
    """
    Caso de Uso 3: Extração de Texto (OCR)
    
    Extrai texto de documentos, placas, letreiros, etc.
    Útil para:
    - Digitalização de documentos
    - Leitura de placas de veículos
    - Análise de sinalizações
    
    Args:
        analyzer: Instância do RekognitionAnalyzer
        image_path: Caminho para a imagem com texto
    """
    print_header("CASO DE USO 3: Extração de Texto (OCR)")
    
    print(f"Analisando imagem: {image_path}")
    print("Extraindo texto...\n")
    
    response = analyzer.detect_text(
        image_path=image_path,
        min_confidence=80.0
    )
    
    # Separa linhas e palavras
    lines = [t for t in response['TextDetections'] if t['Type'] == 'LINE']
    words = [t for t in response['TextDetections'] if t['Type'] == 'WORD']
    
    print("📝 Texto Detectado:\n")
    
    if lines:
        print("Linhas encontradas:")
        for idx, line in enumerate(lines, 1):
            print(f"{idx}. {line['DetectedText']}")
            print(f"   Confiança: {line['Confidence']:.1f}%")
            print()
    else:
        print("⚠ Nenhum texto foi detectado na imagem")
    
    print(f"\n📊 Estatísticas:")
    print(f"   Total de linhas: {len(lines)}")
    print(f"   Total de palavras: {len(words)}")
    
    # Concatena todo o texto
    if lines:
        full_text = "\n".join([line['DetectedText'] for line in lines])
        print(f"\n📄 Texto completo extraído:")
        print("-" * 70)
        print(full_text)
        print("-" * 70)


def moderate_content(analyzer: RekognitionAnalyzer, image_path: str):
    """
    Caso de Uso 4: Moderação de Conteúdo
    
    Verifica se a imagem contém conteúdo impróprio ou sensível.
    Importante para:
    - Redes sociais
    - Plataformas de compartilhamento
    - Aplicações com conteúdo gerado por usuários
    
    Args:
        analyzer: Instância do RekognitionAnalyzer
        image_path: Caminho para a imagem a ser moderada
    """
    print_header("CASO DE USO 4: Moderação de Conteúdo")
    
    print(f"Analisando imagem: {image_path}")
    print("Verificando conteúdo impróprio...\n")
    
    response = analyzer.detect_moderation_labels(
        image_path=image_path,
        min_confidence=60.0
    )
    
    moderation_labels = response['ModerationLabels']
    
    print("🛡️ Resultado da Moderação:\n")
    
    if moderation_labels:
        print("⚠️ ATENÇÃO: Conteúdo potencialmente impróprio detectado!\n")
        
        for label in moderation_labels:
            print(f"❌ {label['Name']}")
            print(f"   Confiança: {label['Confidence']:.1f}%")
            
            if 'ParentName' in label:
                print(f"   Categoria: {label['ParentName']}")
            print()
        
        print("⛔ Recomendação: Esta imagem pode não ser apropriada para exibição pública")
    else:
        print("✅ Nenhum conteúdo impróprio detectado")
        print("✓ A imagem parece ser segura para exibição")


def compare_two_faces(
    analyzer: RekognitionAnalyzer,
    source_image: str,
    target_image: str
):
    """
    Caso de Uso 5: Comparação de Rostos
    
    Compara rostos entre duas imagens para verificar se são da mesma pessoa.
    Aplicações:
    - Verificação de identidade
    - Controle de acesso
    - Autenticação biométrica
    
    Args:
        analyzer: Instância do RekognitionAnalyzer
        source_image: Imagem de referência
        target_image: Imagem para comparação
    """
    print_header("CASO DE USO 5: Comparação de Rostos")
    
    print(f"Imagem de referência: {source_image}")
    print(f"Imagem para comparação: {target_image}")
    print("\nComparando rostos...\n")
    
    response = analyzer.compare_faces(
        source_image_path=source_image,
        target_image_path=target_image,
        similarity_threshold=80.0
    )
    
    print("🔍 Resultado da Comparação:\n")
    
    # Informações do rosto de origem
    source_face = response['SourceImageFace']
    print(f"Rosto de referência detectado:")
    print(f"   Confiança: {source_face['Confidence']:.1f}%\n")
    
    # Matches encontrados
    matches = response['FaceMatches']
    
    if matches:
        print(f"✅ Encontrados {len(matches)} rostos correspondentes:\n")
        
        for idx, match in enumerate(matches, 1):
            similarity = match['Similarity']
            face = match['Face']
            
            print(f"Match {idx}:")
            print(f"   Similaridade: {similarity:.1f}%")
            print(f"   Confiança: {face['Confidence']:.1f}%")
            
            if similarity > 95:
                print(f"   ✓ Alta probabilidade de ser a mesma pessoa")
            elif similarity > 85:
                print(f"   ~ Provável que seja a mesma pessoa")
            else:
                print(f"   ? Possível semelhança, mas não conclusivo")
            print()
    else:
        print("❌ Nenhum rosto correspondente encontrado")
        print("   As imagens provavelmente são de pessoas diferentes")
    
    # Rostos não correspondentes
    unmatched = response['UnmatchedFaces']
    if unmatched:
        print(f"\n👥 {len(unmatched)} rosto(s) adicional(is) encontrado(s) sem correspondência")


def main():
    """
    Função principal que demonstra todos os casos de uso.
    """
    print("\n" + "=" * 70)
    print("  AWS REKOGNITION - EXEMPLOS DE USO")
    print("  FIAP - Fase 7 Cap 1")
    print("=" * 70)
    
    # Verifica variáveis de ambiente
    print("\n🔧 Verificando configuração...\n")

    print_credential_status()
    
    aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    
    if not aws_access_key or not aws_secret_key:
        print("⚠️  ATENÇÃO: Credenciais AWS não encontradas nas variáveis de ambiente")
        print("\nPara usar este script, configure:")
        print("   export AWS_ACCESS_KEY_ID='sua_access_key'")
        print("   export AWS_SECRET_ACCESS_KEY='sua_secret_key'")
        print("   export AWS_DEFAULT_REGION='us-east-1'  # opcional")
        print("\nOu use o arquivo ~/.aws/credentials")
        return
    
    print(f"✓ Credenciais AWS configuradas")
    print(f"✓ Região: {aws_region}\n")
    
    try:
        # Inicializa o analisador
        print("Conectando ao AWS Rekognition...")
        analyzer = RekognitionAnalyzer(region_name=aws_region)
        print("✓ Conexão estabelecida!\n")
        
        # Define o diretório de exemplos
        examples_dir = Path(__file__).parent.parent / "examples"
        
        # Verifica se existem imagens de exemplo
        if not examples_dir.exists():
            print(f"⚠️  Diretório de exemplos não encontrado: {examples_dir}")
            print("\nPara executar os exemplos, crie o diretório 'examples' e adicione imagens de teste:")
            print("   - agricultural_field.jpg (para análise agrícola)")
            print("   - security_camera.jpg (para análise de segurança)")
            print("   - document.jpg (para extração de texto)")
            print("   - content_check.jpg (para moderação)")
            print("   - face1.jpg e face2.jpg (para comparação de rostos)")
            print("\nVocê pode usar suas próprias imagens ou baixar exemplos da internet.")
            return
        
        # Lista de exemplos disponíveis
        print("🎯 Exemplos Disponíveis:\n")
        print("1. Análise Agrícola")
        print("2. Análise de Segurança")
        print("3. Extração de Texto (OCR)")
        print("4. Moderação de Conteúdo")
        print("5. Comparação de Rostos")
        print("\n0. Sair")
        
        while True:
            print("\n" + "-" * 70)
            choice = input("\nEscolha um exemplo (0-5): ").strip()
            
            if choice == '0':
                print("\n👋 Até logo!")
                break
            
            elif choice == '1':
                image_path = input("Caminho da imagem agrícola (ou Enter para exemplo padrão): ").strip()
                if not image_path:
                    image_path = str(examples_dir / "agricultural_field.jpg")
                
                if Path(image_path).exists():
                    analyze_agricultural_image(analyzer, image_path)
                else:
                    print(f"❌ Arquivo não encontrado: {image_path}")
            
            elif choice == '2':
                image_path = input("Caminho da imagem de segurança (ou Enter para exemplo padrão): ").strip()
                if not image_path:
                    image_path = str(examples_dir / "security_camera.jpg")
                
                if Path(image_path).exists():
                    analyze_security_image(analyzer, image_path)
                else:
                    print(f"❌ Arquivo não encontrado: {image_path}")
            
            elif choice == '3':
                image_path = input("Caminho da imagem com texto (ou Enter para exemplo padrão): ").strip()
                if not image_path:
                    image_path = str(examples_dir / "document.jpg")
                
                if Path(image_path).exists():
                    extract_text_from_document(analyzer, image_path)
                else:
                    print(f"❌ Arquivo não encontrado: {image_path}")
            
            elif choice == '4':
                image_path = input("Caminho da imagem para moderação (ou Enter para exemplo padrão): ").strip()
                if not image_path:
                    image_path = str(examples_dir / "content_check.jpg")
                
                if Path(image_path).exists():
                    moderate_content(analyzer, image_path)
                else:
                    print(f"❌ Arquivo não encontrado: {image_path}")
            
            elif choice == '5':
                source = input("Caminho da imagem de referência (ou Enter para padrão): ").strip()
                target = input("Caminho da imagem para comparar (ou Enter para padrão): ").strip()
                
                if not source:
                    source = str(examples_dir / "face1.jpg")
                if not target:
                    target = str(examples_dir / "face2.jpg")
                
                if Path(source).exists() and Path(target).exists():
                    compare_two_faces(analyzer, source, target)
                else:
                    print(f"❌ Um ou mais arquivos não encontrados")
            
            else:
                print("❌ Opção inválida. Escolha entre 0 e 5.")
    
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
        print("\nVerifique:")
        print("1. Suas credenciais AWS estão corretas")
        print("2. Você tem permissões para usar o Rekognition")
        print("3. O serviço está disponível na sua região")
        print("4. Sua conta AWS Learner Lab tem o serviço habilitado")


if __name__ == "__main__":
    main()
