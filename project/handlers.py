'''в этом файле находятся все команды для выполнения ботом'''
from functions import f_graph_root, f_graph_gip, f_graph_cube, f_graph_line, f_graph_square, graph

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

router = Router()

class type_of_graphic(StatesGroup):
    line = State()
    square = State()
    cube = State()
    gip = State()
    root = State()
    not_standard = State()
# класс для поимки состояний, чтобы переходило к выполнению команды только после выполнения определенной предыдущей
equation = str()
cursor_id = int()
# создание переменных для будущего уравнения и курсора
def commands_kb():
    '''эта функция создает клавиатуру меню, которая будет появляться после нажатия /start или "меню",
    в ней находятся кнопки для записи стандартных видов функций и кнопки "другое" для перехода к
    построению собственной функции'''
    commands_kb_list = [
        [KeyboardButton(text="линейная"), KeyboardButton(text="квадратичная")],
        [KeyboardButton(text="кубическая"), KeyboardButton(text="обратная пропорциональность"), KeyboardButton(text="корень из х")], [KeyboardButton(text="другое"), KeyboardButton(text="правила ввода")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=commands_kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard
def back_kb():
    '''клавиатура с кнопкой для возвращения в меню '''
    back_kb_list = [[KeyboardButton(text="меню")]]
    keyboard = ReplyKeyboardMarkup(keyboard=back_kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard
@router.message(CommandStart())
async def message_id(msg: Message):
    '''после команды /start отправляется сообщение и выводится клавиатура для выбора функции'''
    await msg.answer(f"Привет! Этот бот поможет вам построить график функции. Скажите, какая у вас функция?", reply_markup=commands_kb())


@router.message(F.text == 'меню')
async def message_id(msg: Message):
    '''после получения сообщения "меню" обнуляется писавшееся ранее уравнение
    и выводится клавиатура с выбором функций'''
    global equation, cursor_id
    equation = ''
    cursor_id = 0
    # обнуляется уравнения для возможности записи другого
    await msg.answer(f"Выберите вид функции графика", reply_markup=commands_kb())

@router.message(F.text == 'правила ввода')
async def message_id(msg: Message):
    '''функция выводит правила для написания уравнения'''
    await msg.answer(f'Правила ввода:'
                     f'\n \u1696 Если вы выбираете из предложенных видов функций, то следуйте указаниям '
                     f'появляющимся после нажатия на кнопку, остальные праила для ручного ввода уравнения'
                     f'\n \u1696 Неизвестные переменные должны обозначаться символами x и y '
                     f'\n \u1696 Вы можете вводить действия как с клавиатуры бота, так и со своей, '
                     f'но можно вводить только один знак/число за раз'
                     f'\n \u1696 эти кнопки сдвигают курсор вправо и влево соответственно'
                     f'\n \u1696 ** \u002D знак степени'
                     f'\n \u1696 знак \u0336 > передвигает курсор влево (зеркаальный ему соответственно вправо) ' 
                     f'вправо и влево соответственно'
                     f'\n \u1696 == \u002D так пишется обычное равно'
                     f'\n \u1696 можно вернуться в меню, чтобы выбрать вид функции, но тогда вводимое сообщение удалится'
                     f'\n \u1696 нужно обязательно записывать знаки операций, нельзя пропустить знак умножения'
                     f'\n \u1696 бот принимает только целые числа'
                     f'\n \u1696 можно удалить символ, на котором сейчас находится курсор'
                     f'\n \u1696 после ввода полного уравнения нажмите ok и получите график')


@router.message(F.text == 'линейная')
async def message_line(msg: Message, state: FSMContext):
    '''отправляет сообщение о виде функции и способе ввода, состояние для того,
     чтобы после получения цифр построить нужный график линейной функции'''
    await msg.answer(f"y = kx + b, введите значение k, b через пробел без запятых, если какой-то из переменных нет - введите 0", reply_markup=back_kb())
    await state.set_state(state=type_of_graphic.line)


    @router.message(type_of_graphic.line)
    async def message_graph_line(msg: Message, state: FSMContext):
        '''из полученнных данных получает из другой функции график и отпраляет его пользователю, отмена состояния'''
        k, b = msg.text.split(' ')
        photo = f_graph_line(float(k), float(b))
        await msg.answer_photo(photo, caption=f"функция y = {k}x+{b}")
        await state.set_state(state=None)

@router.message(F.text == 'квадратичная')
async def message_square(msg: Message, state: FSMContext):
    '''отправляет сообщение о виде функции и способе ввода, состояние для того,
     чтобы после получения цифр построить нужный график квадратичной функции'''
    await msg.answer(f"y = ax\u00B2 + bx + c, введите значение a, b, c через пробел без запятых, если какой-то из переменных нет - введите 0", reply_markup=back_kb())
    await state.set_state(state=type_of_graphic.square)

    @router.message(type_of_graphic.square)
    async def message_graph_square(message: Message):
        '''из полученнных данных получает из другой функции график и отпраляет его пользователю, отмена состояния'''
        a, b, c = message.text.split(' ')
        photo = f_graph_square(float(a), float(b), float(c))
        await message.answer_photo(photo, caption=f"функция y = {a}x\u00B2 + {b}x + {c}")
        await state.set_state(state=None)

@router.message(F.text == 'кубическая')
async def message_cube(msg: Message, state: FSMContext):
    '''отправляет сообщение о виде функции и способе ввода, состояние для того,
     чтобы после получения цифр построить нужный график кубической функции'''
    await msg.answer(f"y = ax\u00B3+b, введите значение a, b через пробел без запятых, если какой-то из переменных нет - введите 0", reply_markup=back_kb())
    await state.set_state(state=type_of_graphic.cube)

    @router.message(type_of_graphic.cube)
    async def message_graph_cube(msg: Message):
        '''из полученнных данных получает из другой функции график и отпраляет его пользователю, отмена состояния'''
        a, b = msg.text.split(' ')
        photo = f_graph_cube(float(a), float(b))
        await msg.answer_photo(photo, caption=f"функция y = {a}x\u00B3+{b}")
        await state.set_state(state=None)

@router.message(F.text == 'обратная пропорциональность')
async def message_gip(msg: Message, state: FSMContext):
    '''отправляет сообщение о виде функции и способе ввода, состояние для того,
     чтобы после получения цифр построить нужный график обратно пропорциональной функции'''
    await msg.answer(f"y = k/(x+a), введите значение k, a через пробел без запятых, если какой-то из переменных нет - введите 0", reply_markup=back_kb())
    await state.set_state(state=type_of_graphic.gip)

    @router.message(type_of_graphic.gip)
    async def message_graph_gip(msg: Message):
        '''из полученнных данных получает из другой функции график и отпраляет его пользователю, отмена состояния'''
        k, a = msg.text.split(' ')
        photo = f_graph_gip(float(k), float(a))
        await msg.answer_photo(photo, caption=f"функция y = {k}/(x+{a})")
        await state.set_state(state=None)

@router.message(F.text == 'корень из х')
async def message_root(msg: Message, state: FSMContext):
    '''отправляет сообщение о виде функции и способе ввода, состояние для того,
     чтобы после получения цифр построить нужный график функции корня из х'''
    await msg.answer(f"y = \u221a(ax+b) + c, введите значение a, b, c через пробел без запятых, если какой-то из переменных нет - введите 0", reply_markup=back_kb())
    await state.set_state(state=type_of_graphic.root)

    @router.message(type_of_graphic.root)
    async def message_graph_root(msg: Message):
        '''из полученнных данных получает из другой функции график и отпраляет его пользователю, отмена состояния'''
        a, b, c = msg.text.split(' ')
        photo = f_graph_root(float(a), float(b), float(c))
        await msg.answer_photo(photo, caption=f"функция y = \u221a({a}x+{b}) + {c}")
        await state.set_state(state=None)


commands_sign = ['**', '*', '-', '+', '/', '==', '(', ')', 'x', 'y']
# список операций и переменных

def signs_kb():
    '''клавиатура с операциями, возможными в графике функции'''
    sign_kb_list = [[KeyboardButton(text="**"), KeyboardButton(text="*"), KeyboardButton(text="-"), KeyboardButton(text="+"), KeyboardButton(text="/")],
    [KeyboardButton(text="("), KeyboardButton(text=")"), KeyboardButton(text="==")], [KeyboardButton(text="<--"), KeyboardButton(text="-->"), KeyboardButton(text="x"), KeyboardButton(text="y")],
        [KeyboardButton(text="удалить"), KeyboardButton(text="ok"), KeyboardButton(text="меню"), KeyboardButton(text="правила ввода")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=sign_kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

@router.message(F.text == 'другое')
async def message_diff(msg: Message, state: FSMContext):
    '''выводит клавиатуру с возможными операциями, состояние для перехода к другим командам'''
    equation = ''
    cursor_id = 0
    await msg.answer(f"Пожалуйста, ознакомьтесь с правилами ввода и введите уравнение", reply_markup=signs_kb())
    await state.set_state(state=type_of_graphic.not_standard)

    @router.message(type_of_graphic.not_standard)
    async def message_graph_input(msg: Message):
        '''ловит знаки операций из клавиатуры и записывает их в блок уравнений, двигает курсор (он невидимый),
        выводит обратно меню с выбором функций, удаляет неверно записанные символы, записывает цифры в уравнение,
        пишет об ошибке при неверном вводе'''
        if msg.text in commands_sign:
            global equation, cursor_id

            equation = equation[:cursor_id] + str(msg.text) + equation[cursor_id:]
            cursor_id += len(str(msg.text))
            # добавляет текст и сдвигает курсор
            await msg.answer(f'{equation}')

        elif msg.text == '<--':
            cursor_id -= 1
            await msg.answer(f'{equation}')
        #     сдвигает курсор влево

        elif msg.text == '-->':
            cursor_id += 1
            await msg.answer(f'{equation}')
            #     сдвигает курсор вправо

        elif msg.text.isdigit():
            equation = equation[:cursor_id] + str(msg.text) + equation[cursor_id:]
            cursor_id += len(str(msg.text))
            await msg.answer(f'{equation}')
            # добавляет к уравнению число

        elif msg.text == 'удалить':
            equation = equation[:cursor_id-1] + equation[cursor_id:]
            cursor_id -= 1
            await msg.answer(f'{equation}')
            # удаляет элемент до курсора

        elif msg.text == 'ok':
            await msg.answer(f'ваше уравнение: {equation}')
            photo = graph(equation)
            await msg.answer_photo(photo, caption=f"{equation}", reply_markup=commands_kb())
            # отправляет фото графика
            equation = ''
            cursor_id = 0
            await state.set_state(state=None)

        else:
            await msg.answer(f'ваше текущее уравнение: {equation}. Вы ввели что-то не так, попробуйте еще раз')
            # для случаев неправильно ввода
