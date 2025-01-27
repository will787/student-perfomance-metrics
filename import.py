import zipfile

# extração do arquivo do kaggle para análise
zip_file = "/home/wvmwill/enviroment/predict-student-perfomance/support/predict-student-performance-dataset.zip"
extract_path = "dados"

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Arquivos descompactados com sucesso!")