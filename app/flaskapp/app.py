from flask import Flask, jsonify, request
from methods.pmc import CalculatePmc
from methods.helpers import Helpers
import methods.abort
from validations.pmc import ValidationPmc

pmc = CalculatePmc()
helpers = Helpers()
validation = ValidationPmc()
abort = methods.abort.abort

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def home():
    return jsonify({"status":200})

# ATLを算出する
# @param yesterdayAtl, currentTss
#
@app.route('/atl')
def get_atl():
    yesterday_atl = request.args.get('yesterdayAtl', '')
    current_tss = request.args.get('currentTss', '')

    if validation.yesterday_atl(yesterday_atl) or validation.current_tss(current_tss):
        return jsonify(abort(400)), 400

    data = {
        "status":200,
        "current_atl": pmc.current_atl(yesterday_atl, current_tss)
    }

    return jsonify(data)

# CTLを算出する
# @param yesterdayCtl, currentTss
#
@app.route('/ctl')
def get_ctl():
    yesterday_ctl = request.args.get('yesterdayCtl', '')
    current_tss = request.args.get('currentTss', '')

    if validation.yesterday_ctl(yesterday_ctl) or validation.current_tss(current_tss):
        return jsonify(abort(400)), 400


    data = {
	    "status":200,
	    "current_ctl":pmc.current_ctl(yesterday_ctl, current_tss)
    }

    return jsonify(data)


    # TODO 日付とTSSから複数日のPMCを返すAPIを作成する

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, env='development')
