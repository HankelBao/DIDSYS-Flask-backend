from settings import *

@app.route("/<a>")
def hello(a):
    return a

class subjects_api:
    @staticmethod
    @app.route("/subjects")
    def subjects_index():
        return "Here are apis about subjects"

    @staticmethod
    @app.route("/subjects/all")
    def subjects_all():
        subjects_cursors = mongo.db.subjects.find()
        subjects = []
        for subject in subjects_cursors:
            subject.pop("_id")
            subjects.append(subject)
        return jsonify(subjects)

    @staticmethod
    @app.route("/subjects/add")
    def subjects_add():
        name = request.args.get("name")
        full_score = request.args.get("full_score")
        mongo.db.subjects.insert({
            "name":name,
            "full_score": full_score
        })
        return "Succeed"

class classes_api:
    @app.route("/classes")
    def classes_index():
        return "Here are apis about classes"

@app.route("/inspectors")
def inspectors_index():
    return "Here are apis about inspectors"

@app.route("/scores")
def scores_index():
    return "Here are apis about scores"

class admin_api:
    @staticmethod
    @app.route("/admin/clear")
    def admin_clear():
        mongo.db.subjects.remove()
        mongo.db.classes.remove()
        mongo.db.inspectors.remove()
        mongo.db.scores.remove()
        return "Succeed"