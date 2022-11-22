import json

from flask import Flask, Response

app = Flask(__name__)

@app.route("/alkuluku/<num>")
def prime_num(num):
    try:
        p_num = int(num)
        if p_num <= 1:
            response_dict = {"Number": p_num, "IsPrimenum": False}
            return response_dict
        else:
            for i in range(2, p_num+1):
                if p_num % i == 0:
                    if i != p_num:
                        response_dict = {"Number": p_num, "IsPrimenum": False}
                        return response_dict
                    else:
                        response_dict = {"Number": p_num, "IsPrimenum": True}
                        return response_dict
    except ValueError:
        response_json = json.dumps('"message": not a number?')
        return Response(response=response_json, status=400)


if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
