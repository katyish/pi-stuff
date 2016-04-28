from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

import patterns


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/colour/<col>")
def colour(col):
    if col in ['red', 'orange', 'yellow', 'green', 'blue', 'white']:
        # set colour here
        patterns.colour(col, 50)
        return redirect(url_for('index'))
    else:
        return "invalid colour"


@app.route("/off")
def off():
    patterns.off()
    return redirect(url_for('index'))


@app.route("/cycleColour")
def cycleColour():
    patterns.cycleColours(50, 0.2)
    patterns.cycleColours(0, 0.2)
    return redirect(url_for('index'))


@app.route("/cycleIndiv")
def cycleIndiv():
    patterns.cycleIndiv(50, 0.2)
    patterns.cycleIndiv(0, 0.2)
    return redirect(url_for('index'))


@app.route("/spiral")
def spiral():
    patterns.spiral(50, 0.2)
    patterns.spiral(0, 0.2)
    return redirect(url_for('index'))


@app.route("/cycleArms")
def cycleArms():
    patterns.cycleArms(50, 0.5)
    patterns.cycleArms(0, 0.5)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    # app.run()
    app.run(host='0.0.0.0')  # for external...
