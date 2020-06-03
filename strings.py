from random import choice
from .state import State


TEXT_HELLO = 'Привет!\n' \
             'Говорят, как корабль назовёшь, так он и поплывёт.\n' \
             'Для кого хотите подобрать кличку?\n' \
             'Кошка или собака?'
TEXT_CAT = 'Кошки - очаровательные существа. Мальчик или девочка?'
TEXT_DOG = 'Пёсик - это хорошо. Мальчик или девочка?'

TEXT_HELP = 'Сначала выберите животного: кошка или собака. Затем пол: девочка или мальчик.' \
            'И я вам предложу варианты.\n' \
            'Если понравится, скажите "Лайк".\n' \
            'Если хотите посмотреть ещё, скажите "Дальше"'
TEXT_ABILITY = 'Я могу подобрать имя для вышего питомца, у меня очень много идей.\n' \
               'Гарантирую, что вы найдете ту самую кличку.'
TEXT_LIKE = 'Я добавила в понравившиеся!\nДавайте продолжим.\n'

# TODO: variations
TEXT_WTF = 'Я не понимаю/Моя твоя не понимать'
TEXT_BYE = 'Пока!/До свидания!'

TEXT_BACK = 'Выберите животное: кошка, собака.\nЕсли хотите выйти, скажите "Выйти".'

TEXT_FORGOT = 'Извините, я забыла. Попробуйте сказать "Помощь".'

TEXT_NAME_INTRO = 'Если понравилось имя, скажите "Лайк".\n' \
                      'Если хотите посмотреть ещё, скажите "Дальше".\n'

_ANIMAL_DEFAULT = 'Предлагаю такое имя: {}/Вот хорошое имя: {}/Имя {} звучит неплохо.'
_DOG_DEFAULT = _ANIMAL_DEFAULT + \
               '/{}, ко мне!/{}, дай лапу!/{}, сидеть!/{}, нельзя!/Спи, {}, спи, мой пупсик.'
_CAT_DEFAULT = _ANIMAL_DEFAULT + \
               '/{}, идём кушать!/{}, иди ко мне!/{}, нельзя!/Спи, {}, спи, мой котёнок.'

TEXT_NAME = {
    'dog_boy': _DOG_DEFAULT + '/{}, ты что наделал?/{}, зачем ты сгрыз мои тапки?',
    'dog_girl': _DOG_DEFAULT + '/{}, ты что наделала?/{}, зачем ты сгрызла мои тапки?',
    'cat_boy': _CAT_DEFAULT,
    'cat_girl': _CAT_DEFAULT
}

WORDS_CAT = 'кот/кошка/котик/киса/котенка/котёнок/киска/' \
            'кота/кошки/котика/кисы/котенка/котёнка/киски'
# TODO: словоформы - коту кошке..
WORDS_DOG = 'собака/пёс/пес/собачка/щенок/щеночек/кутёнок/пёсик/песик' \
            'собаки/пса/пёсика/песика/собачки/щенка/щеночка/кутёнка/'
# TODO: словоформы - собаке псу...
WORDS_DOG_GIRL = 'девочка/девка/сучка/сука/женщина'
WORDS_DOG_BOY = 'мальчик/пацан/кобель/мужик/мужчина'

WORDS_LIKE = 'лайк/нравится/красивое/красиво/классно/прикольно'
WORDS_MORE = 'еще/ещё/дальше/больше/вперед/вперёд/следующая/следующий/следующее/далее'

WORDS_YES = 'да/даа'
WORDS_NO = 'нет/неа/не'

WORDS_HELP = 'помощь/помоги/как/подсказка'
WORDS_ABILITY = 'умеешь/можешь/могёшь/могешь'
WORDS_REPEAT = 'ещё/еще/повтори/повтори-ка/повтор/понял/слышал/услышал/расслышал/прослушал/скажи/а'
WORDS_EXIT = 'выход/хватит/пока/свидания/стоп/выйти/выключи/останови/остановить/отмена/закончить/' \
             'закончи/отстань/назад/обратно/верни/вернись'

BUTTONS = {
    State.MAIN_MENU: ('Кошка', 'Собака', 'Помощь', 'Что ты умеешь?'),
    State.SEX: ('Девочка', 'Мальчик'),
    State.NAME: ('Лайк', 'Дальше/Ещё/Далее', 'Повтори', 'Выйти')
}


def txt(string):
    return choice(string.split('/'))


def tkn(string):
    return tuple(string.split('/'))


def btn(string):
    if isinstance(string, tuple):
        return list(map(lambda x: txt(x), string))
    return txt(string),
