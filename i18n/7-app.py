#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, request, render_template, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' App config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    ''' return the right dictionary '''
    login_as = request.args.get('login_as')
    if login_as:
        try:
            return users.get(int(login_as))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    ''' def before request '''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    ''' return best languages
    Priority: URL parameter > User settings > Request header > Default
    '''
    # Priority 1: URL parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Priority 2: User settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    
    # Priority 3: Request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    ''' the best time zone
    Priority: URL parameter > User settings > Default
    '''
    # Priority 1: URL parameter
    tz = request.args.get('timezone')
    
    # Priority 2: User settings
    if not tz and g.user:
        tz = g.user.get('timezone')
    
    # Validate timezone
    try:
        if tz:
            pytz.timezone(tz)  # Validates the timezone
            return tz
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    
    # Priority 3: Default
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    ''' return the template '''
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()