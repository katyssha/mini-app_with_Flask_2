import json


def load_candidates():
    with open("candidates.json", "r", encoding='utf-8') as file:
        file_candidates = json.load(file)
        return file_candidates


def get_all():
    text = load_candidates()
    teg = '<pre>'
    for i in text:
        teg += f'''
        {i['name']}\n
        {i['position']}\n
        {i['skills']}\n
        '''
    teg += '</pre>'
    return teg


def get_by_pk(pk):
    text = load_candidates()
    for candidates in text:
        if candidates['pk'] == pk:
            return candidates


def get_by_skill(skill_name):
    text = load_candidates()
    list_dict = []
    for candidates in text:
        if skill_name.lower() in candidates["skills"].lower():
            list_dict.append(candidates)
    return list_dict
