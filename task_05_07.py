import json


def pars_file(name_file):
    """Парсинг текстового файла"""
    with open(name_file, 'r', encoding='utf-8') as txt:
        return [i.split() for i in txt.readlines()]


def el_dict(str_dict):
    """Создает словарь предметов со списками записей"""
    result = {}
    for i in str_dict:
        result[i[0]] = i[1:]
    return result


def rep(rep_margin):
    report = {}
    list_report = []
    av_result = 0
    i = 0
    for key, val in rep_margin.items():
        margin = int(val[1]) if val[1].isdigit() else 0
        cost = int(val[2]) if val[2].isdigit() else 0
        result = margin - cost
        report[key] = result
        if result > 0:
            av_result += result
            i += 1
    av_result = av_result / i
    list_report.append(report)
    list_report.append({"average_profit": av_result})
    return list_report


with open('result_text_7.json', 'w', encoding='utf-8') as txt:
    json.dump(rep(el_dict(pars_file('text_7.txt'))), txt, indent=4, sort_keys=True, ensure_ascii=False)
