from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/dados')
def dados():
    # Substitua pelo caminho da sua planilha local (ou use API Google Sheets com autenticação)
    df = pd.read_excel('atendimentos.xlsx')

    # Renomeie as colunas conforme o nome real da planilha
    registros = df[['Base', 'Técnico', 'Data']].dropna().to_dict(orient='records')
    return jsonify(registros)

if __name__ == '__main__':
    app.run(debug=True)
