from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    information = utils.get_all()
    return information


@app.route('/candidates/<int:x>')
def inf_with_picture(x):
    inf_pk = utils.get_by_pk(x)
    picture = inf_pk['picture']
    teg = f"<img src='({picture})'>\n"
    teg += '\n'
    teg += '<pre>\n'
    teg += f'''
        {inf_pk['name']}\n
        {inf_pk['position']}\n
        {inf_pk['skills']}\n
        '''
    teg += '</pre>'
    return teg


@app.route('/skills/<skills>')
def information_skills(skills):
    inf_skills = utils.get_by_skill(skills)
    teg = '<pre>\n'
    for i in inf_skills:
        teg += f'''
            {i['name']}\n
            {i['position']}\n
            {i['skills']}\n
        '''
    teg += '</pre>'
    return teg


app.run()
