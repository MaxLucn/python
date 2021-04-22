from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/ajax')
def index():
    return render_template('ajax_js.html')


@app.route('/ajax/js', methods=['GET', 'POST'])
def ajax_js():
    print(request.values)
    return 'js ajax', 200


@app.route('/ajax/jq')
def ajax_jq():
    return render_template('ajax_jq.html')