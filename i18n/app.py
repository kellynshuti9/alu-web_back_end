#!/usr/bin/env python3
"""
A Basic flask application
"""
import pytz
import datetime
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel
from flask_babel import format_datetime


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    try:
        return users.get(int(id))
    except (ValueError, TypeError):
        return None


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    Priority order:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # Priority 1: URL parameter
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    
    # Priority 2: User settings
    if g.user and g.user.get('locale') in Config.LANGUAGES:
        return g.user.get('locale')
    
    # Priority 3: Request header
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match
    
    # Priority 4: Default locale
    return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets timezone from request object
    Priority order:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default timezone
    """
    # Priority 1: URL parameter
    tz = request.args.get('timezone', '').strip()
    
    # Priority 2: User settings
    if not tz and g.user:
        tz = g.user.get('timezone', '')
    
    # Validate timezone and return
    try:
        if tz:
            # Validate the timezone exists
            pytz.timezone(tz)
            return tz
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    
    # Priority 3: Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """
    Adds valid user to the global session object `g`
    and sets the current time
    """
    # Get user from login_as parameter
    login_as = request.args.get('login_as')
    if login_as:
        g.user = get_user(login_as)
    else:
        g.user = None
    
    # Set current time for template - use 'current_time' to match template
    g.current_time = format_datetime(datetime.datetime.now())


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()