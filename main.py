from base_skill.skill import *
from .state import State
from .strings import *
from .dbhelper import get_name


handler = CommandHandler()


@handler.hello_command
def hello(req, res, session):
    res.text = txt(TEXT_HELLO)
    res.buttons = [button(x) for x in btn(BUTTONS_HELLO)]
    session['state'] = State.MAIN_MENU


@handler.command(words=tkn(WORDS_CAT), states=State.MAIN_MENU)
def cat(res, req, session):
    res.text = txt(TEXT_CAT)
    res.buttons = [button(x) for x in btn(BUTTONS_SEX)]
    session['animal'] = 'cat'
    session['state'] = State.SEX


@handler.command(words=tkn(WORDS_DOG), states=State.MAIN_MENU)
def dog(res, req, session):
    res.text = txt(TEXT_DOG)
    res.buttons = [button(x) for x in btn(BUTTONS_SEX)]
    session['animal'] = 'dog'
    session['state'] = State.SEX


@handler.command(words=tkn(WORDS_DOG_BOY), states=State.SEX)
def boy(res, req, session):
    session['sex'] = 'boy'
    show_name(res, session, True)


@handler.command(words=tkn(WORDS_DOG_GIRL), states=State.SEX)
def girl(res, req, session):
    session['sex'] = 'girl'
    show_name(res, session, True)


@handler.command(words=tkn(WORDS_MORE), states=State.NAME)
def more(res, req, session):
    show_name(res, session, False)


@handler.undefined_command(states=tuple(State))
def wtf(req, res, session):
    res.text = txt(TEXT_WTF)


def show_name(res, session, intro=False):
    session['state'] = State.NAME
    x = txt(TEXT_NAME[session['animal']]).format(get_name(session['animal'], session['sex']))
    if intro:
        res.text = txt(TEXT_NAME_INTRO) + x
    else:
        res.text = x
    res.buttons = [button(x) for x in btn(BUTTONS_NAME)]


class AnimalNamesSkill(BaseSkill):
    name = 'animal_names'
    command_handler = handler
