from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello_world():
    return "Hello World!  1111"


app.add_url_rule('/home','home',hello_world)
print(app.url_map)
#  不推荐的写法
if __name__ == '__main__':
    app.run(debug=True)
