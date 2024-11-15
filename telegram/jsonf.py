import json

# запись в json файл
def write_inf(data, file_name):
    with open(file_name, 'r+', encoding="utf-8") as f:
        try:
            existing_data = json.load(f)
        except:
            existing_data = {}
        existing_data.update(data)
        f.seek(0)
        json.dump(existing_data, f, indent=4)


# считывание json файла
def read_inf(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)
