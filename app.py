from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345'
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    " Shows the madlibs form "

    return render_template('home.html',
        prompts = story.prompts,
        template = story.template
    )

@app.route('/story')
def get_story():
    " Takes answers from the madlibs form and generates a madlib, then shows it "

    ans = {}
    for prompt in story.prompts:
        ans[prompt] = request.args.get(prompt)
    s = story.generate(ans)
    
    return render_template('/story.html', story=s)