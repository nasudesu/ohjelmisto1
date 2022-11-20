import json

from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/sum')
def get_sum():
    args = request.args
    # print(args)
    try:
        num1 = float(args.get('number1'))
        num2 = float(args.get('number2'))
        sum_of_nums = num1 + num2
        response_dict = {"number1": num1, "number2": num2, "sum": sum_of_nums}
        response_json = json.dumps(response_dict)
        return Response(response=response_json, status=200, mimetype="application/json")
    except TypeError:
        response_json = json.dumps('"message": Invalid parameters missing?')
        return Response(response=response_json, status=400)
    except ValueError:
        return 'Invalid value: not a number?'


@app.route('/hello/<your_name>/<location>')
def hello(your_name, location):

    return 'Hello!' + your_name + 'olet paikassa' + location


@app.errorhandler(404)
def page_not_found(error):
    error_text = str(error)
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=5000)
