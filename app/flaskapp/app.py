from flask import Flask, jsonify, request
from methods.pmc import CalculatePmc
from methods.helpers import Helpers

pmc = CalculatePmc()
helpers = Helpers()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

not_found = {"status":404}

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

    if (yesterday_atl == "") or (current_tss == "") or (not helpers.is_num(yesterday_atl)):
        return jsonify(not_found), 404

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

    # TODO `isdecimal`の部分を少数に対応させる
    if (yesterday_ctl == "") or (current_tss == "") or (not helpers.is_num(yesterday_ctl)) or (not helpers.is_num(current_tss)):
        return jsonify(not_found), 404

    data = {
	    "status":200,
	    "current_ctl":pmc.current_ctl(yesterday_ctl, current_tss)
    }

    return jsonify(data)


    # TODO 日付とTSSから複数日のPMCを返すAPIを作成する

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, env='development')
