from flask import Flask, render_template
import utils

app = Flask('__name__')

candidates = utils.load_candidates()


@app.route('/')
def list_page():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<id_>')
def single_page(id_):
    return render_template('single.html', candidate=candidates[id_])


@app.route('/search/<candidate_name>')
def candidate_name_page(candidate_name):
    candidate_name = candidate_name.capitalize()
    candidates_with_name = utils.get_candidates_by_name(candidate_name, candidates)
    return render_template('name.html', candidates=candidates_with_name, candidate_name=candidate_name)


@app.route('/skill/<skill>')
def skill_page(skill):
    candidates_with_skill = utils.get_candidates_by_skill(skill, candidates)
    return render_template('skill.html', candidates=candidates_with_skill, skill=skill)


if __name__ == '__main__':
    app.run(debug=True)
