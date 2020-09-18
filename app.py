from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@ app.route('/')
def index():
    return render_template('index.html')


@app.route("/encryptIt", methods=["GET", "POST"])
def encryption():
    if request.method == "POST":
        if "ceaserEncrypt" in request.form:
            req = request.form
            plaintext = req["ceaserPlainText"]
            cipher = []
            for letter in plaintext:
                letter = ord(letter)
                letter = letter+3
                cipher.append(letter)
            encryptedText = []
            for letters in cipher:
                letters = chr(letters)
                encryptedText.append(letters)
            answer = "".join(encryptedText)

            return render_template("/encryptIt.html", result=answer)

        elif "oneTimeEncrypt" in request.form:
            res = request.form
            plaintext = res["oneTimePadText"]
            import onetimepad
            cipher = onetimepad.encrypt(plaintext, 'random')
            return render_template("/encryptIt.html", results=cipher)

        elif "monoEncrypt" in request.form:
            req = request.form
            plaintext = req["monoText"]
            from string import printable
            from random import shuffle
            keys = list(printable)
            shuffle_keys = list(printable)
            shuffle(shuffle_keys)

            maps = dict(zip(keys, shuffle_keys))
            reverse_map = dict(zip(shuffle_keys, keys))

            cipher = []
            for letters in plaintext:
                cipherletters = maps[letters]
                cipher.append(cipherletters)

            answer = "".join(cipher)
            return render_template("/encryptIt.html", resu=answer)

    return render_template("/encryptIt.html")


def encryptIt():
    return render_template("/encryptIt.html")


if __name__ == "__main__":
    app.run(debug=True)
