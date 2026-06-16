#!/usr/bin/env python3
"""Basic Flask app that implements i18n and internationalization"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for your application, it deals with babel mostly"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale for your application
    Priority: URL parameter > User settings > Request header > Default
    """
    # Priority 1: URL parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Priority 2: User settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Priority 3: Request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Get user information from users dict"""
    login_as = request.args.get('login_as')
    if login_as:
        try:
            return users.get(int(login_as))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """Before request - sets g.user if user is logged in"""
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home page for your application"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
