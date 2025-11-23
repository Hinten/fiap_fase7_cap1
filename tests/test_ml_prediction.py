"""
Unit tests for the ML prediction module (src/modelo_preditivo/realizar_previsao_func.py)
Tests machine learning model loading and prediction functionality
"""
import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock
import os
import joblib
import pandas as pd
import numpy as np


class TestConverteDataLeitura:
    """Tests for converte_data_leitura function"""
    
    def test_converte_data_meia_noite(self):
        """Test conversion at midnight"""
        from src.modelo_preditivo.realizar_previsao_func import converte_data_leitura
        
        hora = datetime(2025, 5, 20, 0, 0, 0)
        resultado = converte_data_leitura(hora)
        
        assert resultado == 0.0
    
    def test_converte_data_meio_dia(self):
        """Test conversion at noon"""
        from src.modelo_preditivo.realizar_previsao_func import converte_data_leitura
        
        hora = datetime(2025, 5, 20, 12, 0, 0)
        resultado = converte_data_leitura(hora)
        
        assert resultado == 720.0  # 12 * 60
    
    def test_converte_data_com_minutos_segundos(self):
        """Test conversion with minutes and seconds"""
        from src.modelo_preditivo.realizar_previsao_func import converte_data_leitura
        
        hora = datetime(2025, 5, 20, 14, 30, 30)
        resultado = converte_data_leitura(hora)
        
        # 14 hours * 60 + 30 minutes + 30 seconds / 60
        expected = 14 * 60 + 30 + 30 / 60
        assert abs(resultado - expected) < 0.01
    
    def test_converte_data_fim_do_dia(self):
        """Test conversion at end of day"""
        from src.modelo_preditivo.realizar_previsao_func import converte_data_leitura
        
        hora = datetime(2025, 5, 20, 23, 59, 59)
        resultado = converte_data_leitura(hora)
        
        # 23 hours * 60 + 59 minutes + 59 seconds / 60
        expected = 23 * 60 + 59 + 59 / 60
        assert abs(resultado - expected) < 0.01


class TestCarregarModeloERealizarPrevisao:
    """Tests for carregar_modelo_e_realizar_previsao function"""
    
    def create_mock_model(self):
        """Helper to create a mock ML model"""
        mock_model = MagicMock()
        mock_model.feature_names_in_ = ['hora_leitura', 'Fósforo', 'Potássio', 'PH', 'Umidade']
        mock_model.predict.return_value = np.array([1])  # Predict "Sim"
        
        mock_scaler = MagicMock()
        mock_scaler.transform.return_value = np.array([[0.5, 1, 1, 1, 0.455]])
        
        mock_label_encoder = MagicMock()
        mock_label_encoder.inverse_transform.return_value = np.array(['Sim'])
        
        return {
            'modelo': mock_model,
            'scaler': mock_scaler,
            'label_encoder': mock_label_encoder
        }
    
    @patch('joblib.load')
    def test_previsao_positiva_sim(self, mock_joblib_load):
        """Test prediction returns 'Sim'"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock
        mock_model_data = self.create_mock_model()
        mock_joblib_load.return_value = mock_model_data
        
        # Execute
        resultado = carregar_modelo_e_realizar_previsao(
            path_arquivo='fake_path.pkl',
            hora_leitura=datetime(2025, 5, 20, 14, 30, 0),
            fosforo=1,
            potassio=1,
            ph=1,
            umidade=45.5
        )
        
        # Verify
        assert resultado == 'Sim'
        assert mock_model_data['modelo'].predict.called
    
    @patch('joblib.load')
    def test_previsao_negativa_nao(self, mock_joblib_load):
        """Test prediction returns 'Não'"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock
        mock_model_data = self.create_mock_model()
        mock_model_data['modelo'].predict.return_value = np.array([0])
        mock_model_data['label_encoder'].inverse_transform.return_value = np.array(['Não'])
        mock_joblib_load.return_value = mock_model_data
        
        # Execute
        resultado = carregar_modelo_e_realizar_previsao(
            path_arquivo='fake_path.pkl',
            hora_leitura=datetime(2025, 5, 20, 14, 30, 0),
            fosforo=1,
            potassio=1,
            ph=1,
            umidade=75.0
        )
        
        # Verify
        assert resultado == 'Não'
    
    @patch('joblib.load')
    def test_scaler_transform_chamado(self, mock_joblib_load):
        """Test that scaler transform is called correctly"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock
        mock_model_data = self.create_mock_model()
        mock_joblib_load.return_value = mock_model_data
        
        # Execute
        carregar_modelo_e_realizar_previsao(
            path_arquivo='fake_path.pkl',
            hora_leitura=datetime(2025, 5, 20, 14, 30, 0),
            fosforo=0,
            potassio=0,
            ph=0,
            umidade=45.5
        )
        
        # Verify scaler was called twice (initial and final transform)
        assert mock_model_data['scaler'].transform.call_count == 2
    
    @patch('joblib.load')
    def test_arquivo_inexistente(self, mock_joblib_load):
        """Test handling of non-existent model file"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock to raise exception
        mock_joblib_load.side_effect = FileNotFoundError("Model file not found")
        
        # Execute and expect exception
        with pytest.raises(FileNotFoundError):
            carregar_modelo_e_realizar_previsao(
                path_arquivo='nonexistent.pkl',
                hora_leitura=datetime.now(),
                fosforo=1,
                potassio=1,
                ph=1,
                umidade=50.0
            )


class TestRealizarPrevisaoModeloPadrao:
    """Tests for realizar_previsao_modelo_padrao function"""
    
    @patch('src.modelo_preditivo.realizar_previsao_func.carregar_modelo_e_realizar_previsao')
    def test_usa_modelo_padrao_svmrbf(self, mock_carregar):
        """Test that default model SVMrbf.pkl is used"""
        from src.modelo_preditivo.realizar_previsao_func import realizar_previsao_modelo_padrao
        
        # Setup mock
        mock_carregar.return_value = 'Sim'
        
        # Execute
        resultado = realizar_previsao_modelo_padrao(
            hora_leitura=datetime(2025, 5, 20, 14, 30, 0),
            fosforo=1,
            potassio=1,
            ph=1,
            umidade=45.5
        )
        
        # Verify
        assert resultado == 'Sim'
        assert mock_carregar.called
        
        # Verify correct model path
        call_args = mock_carregar.call_args
        assert 'SVMrbf.pkl' in call_args[1]['path_arquivo']
    
    @patch('src.modelo_preditivo.realizar_previsao_func.carregar_modelo_e_realizar_previsao')
    def test_parametros_passados_corretamente(self, mock_carregar):
        """Test that parameters are passed correctly"""
        from src.modelo_preditivo.realizar_previsao_func import realizar_previsao_modelo_padrao
        
        # Setup mock
        mock_carregar.return_value = 'Não'
        
        # Test parameters
        hora = datetime(2025, 5, 20, 10, 15, 30)
        fosforo = 0
        potassio = 1
        ph = 0
        umidade = 30.5
        
        # Execute
        resultado = realizar_previsao_modelo_padrao(
            hora_leitura=hora,
            fosforo=fosforo,
            potassio=potassio,
            ph=ph,
            umidade=umidade
        )
        
        # Verify
        call_args = mock_carregar.call_args
        assert call_args[1]['hora_leitura'] == hora
        assert call_args[1]['fosforo'] == fosforo
        assert call_args[1]['potassio'] == potassio
        assert call_args[1]['ph'] == ph
        assert call_args[1]['umidade'] == umidade


class TestEdgeCases:
    """Tests for edge cases and boundary conditions"""
    
    @patch('joblib.load')
    def test_umidade_zero(self, mock_joblib_load):
        """Test prediction with 0% humidity"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock
        mock_model_data = TestCarregarModeloERealizarPrevisao().create_mock_model()
        mock_joblib_load.return_value = mock_model_data
        
        # Execute
        resultado = carregar_modelo_e_realizar_previsao(
            path_arquivo='fake_path.pkl',
            hora_leitura=datetime.now(),
            fosforo=1,
            potassio=1,
            ph=1,
            umidade=0.0
        )
        
        # Should not raise exception
        assert resultado in ['Sim', 'Não']
    
    @patch('joblib.load')
    def test_umidade_maxima(self, mock_joblib_load):
        """Test prediction with 100% humidity"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock
        mock_model_data = TestCarregarModeloERealizarPrevisao().create_mock_model()
        mock_joblib_load.return_value = mock_model_data
        
        # Execute
        resultado = carregar_modelo_e_realizar_previsao(
            path_arquivo='fake_path.pkl',
            hora_leitura=datetime.now(),
            fosforo=1,
            potassio=1,
            ph=1,
            umidade=100.0
        )
        
        # Should not raise exception
        assert resultado in ['Sim', 'Não']
    
    @patch('joblib.load')
    def test_todos_sensores_criticos(self, mock_joblib_load):
        """Test prediction with all sensors in critical state"""
        from src.modelo_preditivo.realizar_previsao_func import carregar_modelo_e_realizar_previsao
        
        # Setup mock
        mock_model_data = TestCarregarModeloERealizarPrevisao().create_mock_model()
        mock_joblib_load.return_value = mock_model_data
        
        # Execute
        resultado = carregar_modelo_e_realizar_previsao(
            path_arquivo='fake_path.pkl',
            hora_leitura=datetime.now(),
            fosforo=0,
            potassio=0,
            ph=0,
            umidade=20.0
        )
        
        # Should return 'Sim' for irrigation
        assert resultado in ['Sim', 'Não']
