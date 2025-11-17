"""
CLI Launcher - Command Line Interface for FarmTech Solutions
Launcher via linha de comando para disparar fases individuais ou completas

Uso:
    python -m src.fase7.launcher --fase 1
    python -m src.fase7.launcher --all
    python -m src.fase7.launcher --test-aws

Autor: Grupo 28 - FIAP 2025
"""

import argparse
import sys
import logging
from typing import Optional
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.fase7.orchestrator import run_phase, run_all_phases, get_execution_history

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def print_banner():
    """Exibe banner do sistema."""
    banner = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║      🌾 FarmTech Solutions - System Launcher 🌾         ║
║                                                          ║
║         Sistema Agrícola Inteligente - Fase 7           ║
║                   FIAP 2025 - Grupo 28                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_phase_description(phase: int):
    """Exibe descrição de uma fase."""
    descriptions = {
        1: "🌾 Fase 1: Cálculos Agrícolas + API Meteorológica",
        2: "💾 Fase 2: Banco de Dados (MER/DER)",
        3: "🔌 Fase 3: IoT (ESP32, Sensores e Irrigação)",
        4: "📊 Fase 4: Dashboard (Streamlit) + Machine Learning",
        5: "☁️ Fase 5: AWS Alertas (SNS/SES)",
        6: "👁️ Fase 6: Visão Computacional (YOLO)"
    }
    
    if phase in descriptions:
        print(f"\n{descriptions[phase]}")
        print("─" * 60)


def run_single_phase(phase: int, verbose: bool = False) -> bool:
    """
    Executa uma fase específica.
    
    Args:
        phase: Número da fase (1-6)
        verbose: Se True, exibe detalhes completos
    
    Returns:
        bool indicando sucesso
    """
    print_phase_description(phase)
    
    logger.info(f"Iniciando Fase {phase}...")
    
    result = run_phase(phase)
    
    if result['status'] == 'success':
        print(f"✅ Fase {phase} executada com sucesso!")
        print(f"⏱️  Tempo decorrido: {result['elapsed_seconds']:.2f}s")
        
        if verbose:
            print(f"\n📋 Detalhes:")
            for key, value in result.get('result', {}).items():
                print(f"   {key}: {value}")
        
        return True
    else:
        print(f"❌ Fase {phase} falhou!")
        print(f"❗ Erro: {result.get('error', 'Unknown error')}")
        return False


def run_all_phases_cli(verbose: bool = False):
    """
    Executa todas as fases em sequência.
    
    Args:
        verbose: Se True, exibe detalhes completos
    """
    print("\n🚀 Executando todas as fases em sequência...")
    print("=" * 60)
    
    summary = run_all_phases()
    
    print("\n" + "=" * 60)
    print("📊 Resumo da Execução")
    print("=" * 60)
    print(f"✅ Fases bem-sucedidas: {summary['successful']}/{summary['total_phases']}")
    print(f"❌ Fases com erro: {summary['failed']}/{summary['total_phases']}")
    
    if verbose:
        print("\n📋 Detalhes por Fase:")
        for result in summary['results']:
            phase = result['phase']
            status = "✅" if result['status'] == 'success' else "❌"
            elapsed = result.get('elapsed_seconds', 0)
            print(f"   {status} Fase {phase}: {result['status']} ({elapsed:.2f}s)")


def test_aws_connection():
    """Testa conexão com AWS SNS."""
    print("\n☁️ Testando conexão com AWS SNS...")
    print("─" * 60)
    
    try:
        from src.fase5.aws.alert_service import test_aws_connection, publish_alert
        
        result = test_aws_connection()
        
        if result['status'] == 'success':
            print("✅ Conexão AWS estabelecida com sucesso!")
            print(f"   Tópico: {result.get('topic_name', 'N/A')}")
            print(f"   ARN: {result.get('topic_arn', 'N/A')}")
            print(f"   Assinaturas confirmadas: {result.get('subscriptions_confirmed', '0')}")
            print(f"   Assinaturas pendentes: {result.get('subscriptions_pending', '0')}")
            
            # Perguntar se quer enviar alerta de teste
            response = input("\n📧 Deseja enviar um alerta de teste? (s/N): ")
            if response.lower() == 's':
                alert_result = publish_alert(
                    subject="🧪 Teste do Sistema FarmTech",
                    message="Este é um alerta de teste enviado via CLI. Se você recebeu este email/SMS, o sistema está funcionando corretamente!",
                    severity="INFO"
                )
                
                if alert_result['status'] == 'success':
                    print(f"✅ Alerta enviado com sucesso! (MessageId: {alert_result.get('message_id', 'N/A')})")
                else:
                    print(f"❌ Falha ao enviar alerta: {alert_result.get('error', 'Unknown')}")
        else:
            print(f"❌ Falha na conexão AWS: {result.get('error', 'Unknown error')}")
            print("\n💡 Dicas:")
            print("   1. Verifique se as credenciais estão configuradas no .env")
            print("   2. Confirme que o tópico SNS existe")
            print("   3. Valide as permissões IAM do usuário")
            
    except ImportError:
        print("❌ Módulo boto3 não instalado!")
        print("   Execute: pip install boto3")
    except Exception as e:
        print(f"❌ Erro ao testar conexão: {e}")


def show_execution_history():
    """Exibe histórico de execuções."""
    print("\n📜 Histórico de Execuções")
    print("=" * 60)
    
    history = get_execution_history()
    
    if not history:
        print("   Nenhuma execução registrada ainda.")
        return
    
    for record in history:
        phase = record['phase']
        status = "✅" if record['status'] == 'success' else "❌"
        timestamp = record['timestamp']
        elapsed = record.get('elapsed_seconds', 0)
        
        print(f"{status} Fase {phase} - {timestamp} ({elapsed:.2f}s)")


def main():
    """Função principal do CLI."""
    parser = argparse.ArgumentParser(
        description="FarmTech Solutions - System Launcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  %(prog)s --fase 1              # Executar apenas Fase 1
  %(prog)s --fase 5              # Executar apenas Fase 5 (AWS)
  %(prog)s --all                 # Executar todas as fases
  %(prog)s --test-aws            # Testar conexão AWS
  %(prog)s --history             # Ver histórico de execuções
  %(prog)s --fase 3 --verbose    # Fase 3 com saída detalhada
        """
    )
    
    parser.add_argument(
        '--fase',
        type=int,
        choices=range(1, 7),
        metavar='N',
        help='Número da fase a executar (1-6)'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Executar todas as fases em sequência'
    )
    
    parser.add_argument(
        '--test-aws',
        action='store_true',
        help='Testar conexão com AWS SNS'
    )
    
    parser.add_argument(
        '--history',
        action='store_true',
        help='Exibir histórico de execuções'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Exibir saída detalhada'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Não exibir banner inicial'
    )
    
    args = parser.parse_args()
    
    # Exibir banner
    if not args.no_banner:
        print_banner()
    
    # Validar argumentos
    if not any([args.fase, args.all, args.test_aws, args.history]):
        parser.print_help()
        sys.exit(1)
    
    # Processar comandos
    success = True
    
    if args.history:
        show_execution_history()
    
    if args.test_aws:
        test_aws_connection()
    
    if args.fase:
        success = run_single_phase(args.fase, args.verbose)
    
    if args.all:
        run_all_phases_cli(args.verbose)
    
    # Exit code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
