# components/tables.py

import pandas as pd
import dash_ag_grid as dag

def create_table_from_dataframe(df: pd.DataFrame, table_id: str, hidden_columns: list = None) -> dag.AgGrid:
    """
    Cria um componente de tabela Dash AG Grid a partir de um DataFrame do pandas.
    
    :param df: DataFrame contendo os dados a serem exibidos.
    :param table_id: Identificador único para o componente da tabela.
    :param hidden_columns: Lista opcional de colunas a serem ocultadas na tabela.
    :return: Componente Dash AG Grid com os dados do DataFrame.
    """
    column_defs = [{'field': col} for col in df.columns]

    # Ocultar colunas específicas, se necessário
    if hidden_columns:
        for col_def in column_defs:
            if col_def['field'] in hidden_columns:
                col_def['hide'] = True

    return dag.AgGrid(
        id=table_id,
        rowData=df.to_dict("records"),
        columnDefs=column_defs,
        defaultColDef={
            "resizable": True,
            "sortable": True,
            "filter": True,
            "floatingFilter": True
        }
    )
