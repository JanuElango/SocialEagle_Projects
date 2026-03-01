from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Japanese": "ja",
    "Telugu": "te"
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    original_text = ""
    from_lang = "English"
    to_lang = "Tamil"
    error = ""

    if request.method == "POST":
        original_text = request.form.get("text")
        from_lang = request.form.get("from_language")
        to_lang = request.form.get("to_language")

        if not original_text:
            error = "Please enter text to translate."
        elif from_lang == to_lang:
            error = "Source and Target languages must be different."
        else:
            try:
                translated_text = GoogleTranslator(
                    source=languages[from_lang],
                    target=languages[to_lang]
                ).translate(original_text)
            except Exception as e:
                error = f"Translation Error: {str(e)}"

    return render_template(
        "index.html",
        languages=languages,
        translated_text=translated_text,
        original_text=original_text,
        from_lang=from_lang,
        to_lang=to_lang,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)