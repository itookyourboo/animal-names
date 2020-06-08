from base_skill.skill import *
from .strings import *
from .dbhelper import get_name, add_wtf, put_like, get_likes


handler = CommandHandler()


@handler.hello_command
def hello(req, res, session):
    res.text = txt(TEXT_HELLO)
    session['state'] = State.MAIN_MENU
    default_buttons(res, session)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_CAT), states=State.MAIN_MENU)
def cat(res, req, session):
    res.text = txt(TEXT_CAT)
    session['animal'] = 'cat'
    session['state'] = State.SEX
    default_buttons(res, session)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_DOG), states=State.MAIN_MENU)
def dog(res, req, session):
    res.text = txt(TEXT_DOG)
    session['animal'] = 'dog'
    session['state'] = State.SEX
    default_buttons(res, session)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_DOG_BOY), states=State.SEX)
def boy(res, req, session):
    session['sex'] = 'boy'
    show_name(res, session, intro=True)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_DOG_GIRL), states=State.SEX)
def girl(res, req, session):
    session['sex'] = 'girl'
    show_name(res, session, intro=True)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_MORE), states=State.NAME)
def more(res, req, session):
    show_name(res, session)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_LIKED), states=State.MAIN_MENU)
def liked(res, req, session):
    show_likes(res, req, session)
    default_buttons(res, session)


@handler.command(words=tkn(WORDS_LIKE), states=State.NAME)
def like(res, req, session):
    put_like(req.user_id, session['animal'], session['name'])
    show_name(res, session, like=True)
    default_buttons(res, session)


@handler.command(words=tkn(WORDS_HELP), states=State.ALL)
def help_(res, req, session):
    res.text = txt(TEXT_HELP)
    default_buttons(res, session)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_ABILITY), states=State.ALL)
def ability(res, req, session):
    res.text = txt(TEXT_ABILITY)
    default_buttons(res, session)
    save_last_res(res, session)


@handler.command(words=tkn(WORDS_REPEAT), states=State.ALL)
def repeat(res, req, session):
    if session['state'] == State.NAME:
        show_name(res, session, change=False)
    else:
        res.text = session.get('last_text', TEXT_FORGOT)
        default_buttons(res, session)


@handler.command(words=tkn(WORDS_EXIT), states=State.ALL)
def exit_(res, req, session):
    if session['state'] == State.MAIN_MENU:
        res.text = txt(TEXT_BYE)
        res.end_session = True
        session.clear()
    else:
        session['state'] = State.MAIN_MENU
        res.text = txt(TEXT_BACK)
        default_buttons(res, session)


@handler.undefined_command(states=State.ALL)
def wtf(res, req, session):
    res.text = txt(TEXT_WTF.get(session['state'], 'Добавь обработку'))
    add_wtf(res, req, session)
    default_buttons(res, session)


def show_name(res, session, intro=False, like=False, change=True):
    session['state'] = State.NAME
    animal, sex = session['animal'], session['sex']
    if change:
        session['name'] = get_name(animal, sex)
    x = txt(TEXT_NAME[f'{animal}_{sex}']).format(session['name'])
    res.text = txt(TEXT_NAME_INTRO if intro else TEXT_LIKE if like else '') + x
    default_buttons(res, session)


def show_likes(res, req, session):
    likes = list(map(lambda x: x[0], get_likes(req.user_id)))
    res.text = txt(TEXT_LIKED) + ', '.join(likes)


def default_buttons(res, session):
    res.buttons = [button(x) for x in btn(BUTTONS[session['state']])]


def save_last_res(res, session):
    session['last_text'] = res.text


class AnimalNamesSkill(BaseSkill):
    name = 'animal_names'
    command_handler = handler
