from flask import Flask, jsonify, request
from methods import pmc, tss

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

not_found = {"status":404}

@app.route('/')
def home():
    return jsonify({"status":200})

# ATLを算出する
# @param yesterdayAtl, currentTss
# TODO パラメータが文字型だった場合の処理を追加する
#
@app.route('/atl')
def get_atl():
    yesterday_atl = request.args.get('yesterdayAtl', '')
    current_tss = request.args.get('currentTss', '')

    if (yesterday_atl == "") or (current_tss == ""):
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

    if (yesterday_ctl == "") or (current_tss == ""):
        return jsonify(not_found), 404

    data = {
	    "status":200,
	    "current_ctl":pmc.current_ctl(yesterday_ctl, current_tss)
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
