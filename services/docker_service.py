import subprocess
import os

def run_ck_analysis(repo_url):
    current_directory = os.getcwd()  # Obtém o diretório de trabalho atual
    output_directory = os.path.join(current_directory, "output")  # Define o diretório de saída para os arquivos CSV

    try:
        # Comando para executar o Docker com montagem de volume
        result = subprocess.check_output(
            [
                'docker', 'run',
                '-e', f'REPO_URL={repo_url}',
                '-v', f"{output_directory}:/app/output",  # Monta o diretório de saída do host no container
                'ck-analyzer'
            ],
            stderr=subprocess.STDOUT
        )
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Erro durante a execução: {e.output.decode("utf-8")}'
