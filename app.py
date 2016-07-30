from flask import Flask, render_template, redirect, url_for
app = Flask('Bubble Kiwi')

@app.errorhandler(404)
def not_found(error):
    return redirect('http://bubble.kiwi/')

@app.route('/<refer>')
def referal(refer=None):
    return render_template("redirect.html")

if __name__ == "__main__":
    app.run()
