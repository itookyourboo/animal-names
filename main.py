from base_skill.skill import *
from .state import State
from .strings import *


handler = CommandHandler()


@handler.hello_command
def hello(req, res, session):
    res.text = txt(TEXT_HELLO)
    res.buttons = [button(x) for x in btn(BUTTONS_HELLO)]
    session['state'] = State.MAIN_MENU


@handler.command(words=tkn(WORDS_CAT), states=State.MAIN_MENU)
def cat(res, req, session):
    res.text = txt(TEXT_CAT)


@handler.command(words=tkn(WORDS_DOG), states=State.MAIN_MENU)
def dog(res, req, session):
    res.text = txt(TEXT_DOG)
    res.buttons = [button(x) for x in btn(BUTTONS_SEX)]
    session['state'] = State.DOG_SEX


@handler.command(words=tkn(WORDS_DOG_BOY), states=State.DOG_SEX)
def dog_boy(res, req, session):
    res.text = txt(TEXT_DOG_NAME_FIRST) + txt(TEXT_DOG_NAME)
    session['dog_boy'] = True
    session['state'] = State.DOG_NAME


@handler.command(words=tkn(WORDS_DOG_GIRL), states=State.DOG_SEX)
def dog_girl(res, req, session):
    res.text = txt(TEXT_DOG_NAME_FIRST) + txt(TEXT_DOG_NAME)
    session['dog_boy'] = False
    session['state'] = State.DOG_NAME


@handler.command(words=tkn(WORDS_MORE), states=State.DOG_NAME)
def dog_more(res, req, session):
    res.text = txt(TEXT_DOG_NAME)


@handler.undefined_command(states=tuple(State))
def wtf(req, res, session):
    res.text = txt(TEXT_WTF)


class AnimalNamesSkill(BaseSkill):
    name = 'animal_names'
    command_handler = handler
