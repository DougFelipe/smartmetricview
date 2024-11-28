import os
from fpdf import FPDF

class ReportStructuringService:
    def __init__(self):
        self.pdf = FPDF()

    def structuring_report(self, nome_arquivo, repositorio_url, description, ck_metrics, analise_llm_ck):
        """Classe responsável por estruturar e gerar relatório em .pdf"""

        try:
            if not description or description.strip() == "":
                description = "Descrição não fornecida."

            self.pdf.add_page()
            self.pdf.set_font("Arial", size=12)

            # Cabeçalho
            self.pdf.set_font("Arial", 'B', size=16)
            self.pdf.cell(200, 10, txt="Relatório do Projeto", ln=True, align='C')
            self.pdf.ln(10)

            # Informações Gerais
            self.pdf.set_font("Arial", size=12)
            self.pdf.cell(200, 10, txt="Informações Gerais", ln=True, align='L')
            self.pdf.ln(5)
            self.pdf.multi_cell(0, 10, txt=f"URL Repositório: {repositorio_url}")
            self.pdf.ln(5)
            self.pdf.multi_cell(0, 10, txt=f"Descrição do Projeto: {description}")
            self.pdf.ln(10)

            # Métricas CK
            self.pdf.set_font("Arial", 'B', size=12)
            self.pdf.cell(200, 10, txt="Métricas CK", ln=True, align='L')
            self.pdf.set_font("Arial", size=12)
            self.pdf.ln(5)
            self.pdf.multi_cell(0, 10, txt=ck_metrics)
            self.pdf.ln(10)

            # Análise LLM CK
            self.pdf.set_font("Arial", 'B', size=12)
            self.pdf.cell(200, 10, txt="Análise LLM CK", ln=True, align='L')
            self.pdf.set_font("Arial", size=12)
            self.pdf.ln(5)
            self.pdf.multi_cell(0, 10, txt=analise_llm_ck)
            self.pdf.ln(10)

            output_dir = os.getenv("DOWNLOAD_DIRECTORY")
            if not output_dir:
                raise ReportStructuringException("Diretório de download não especificado.")

            if not os.path.exists(output_dir):
                try:
                    os.makedirs(output_dir)
                except Exception as e:
                    raise ReportStructuringException(f"Erro ao criar diretório de download: {str(e)}")

            output_path = os.path.join(output_dir, nome_arquivo)
            self.pdf.output(output_path)
        except Exception as e:
            raise ReportStructuringException(f"Erro ao estruturar o relatório: {str(e)}")
