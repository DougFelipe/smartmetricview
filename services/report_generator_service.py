import os
from fpdf import FPDF

class ReportGenerator:
    def generate_report(self, nome_arquivo, repositorio_url, description, ck_metrics, analise_llm_ck):
        # Criação do objeto PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Cabeçalho
        pdf.set_font("Arial", 'B', size=16)
        pdf.cell(200, 10, txt="Relatório do Projeto", ln=True, align='C')
        pdf.ln(10)  # Linha em branco após o cabeçalho

        # Informações Gerais
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informações Gerais", ln=True, align='L')
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=f"URL Repositório: {repositorio_url}")
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=f"Descrição do Projeto: {description}")
        pdf.ln(10)  # Espaço após informações gerais

        # Métricas CK
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(200, 10, txt="Métricas CK", ln=True, align='L')
        pdf.set_font("Arial", size=12)
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=ck_metrics)
        pdf.ln(10)  # Espaço após métricas CK

        # Análise LLM SOLID
        # pdf.set_font("Arial", 'B', size=12)
        # pdf.cell(200, 10, txt="Análise LLM SOLID", ln=True, align='L')
        # pdf.set_font("Arial", size=12)
        # pdf.ln(5)
        # pdf.multi_cell(0, 10, txt=analise_llm_solid)
        # pdf.ln(10)  # Espaço após análise LLM SOLID

        # Análise LLM CK
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(200, 10, txt="Análise LLM CK", ln=True, align='L')
        pdf.set_font("Arial", size=12)
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt=analise_llm_ck)
        pdf.ln(10)  # Espaço após análise LLM CK

        # Diretório de saída
        output_dir = os.getenv("DOWNLOAD_DIRECTORY")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Cria o diretório se ele não existir

        # Caminho completo do arquivo
        output_path = os.path.join(output_dir, nome_arquivo)

        # Salva o arquivo PDF
        pdf.output(output_path)

