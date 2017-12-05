from secdiagai.form_analyzer import FormAnalyzer
import json

TR_JSON_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/scripts/fixtures/transactions/jsons/01_excom_133_Full.json'
MODELS_PATH = '/secdiagai/model'
DUMP_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/analysis_results/result.json'


with open(TR_JSON_PATH) as f:
    transactions = json.load(f)
    analyzer = FormAnalyzer(MODELS_PATH)
    result = analyzer.create_analysis_result(transactions)

    with open(DUMP_PATH, mode='w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)




