async def box_question(sdep, tab, fio, id):
    popup('Задать вопрос',[
        put_textarea(name='box_question', label='Напиши свой вопрос', maxlength=1000, minlength=100),
        put_select(name='question_category', label='Выберите категорию:', options=['Заработная плата', 'Рабочие процессы', 'Корпоративная жизнь', 'Условия труда', 'Другое']),
        put_html('<br>'),
        put_button("ОТПРАВИТЬ ВОПРОС", onclick=lambda: box_question_send(sdep, tab, fio, id), color='danger', outline=True)
        ], size='normal')
    
# Отправить вопрос
async def box_question_send(sdep, tab, fio, id):
    try:
        close_popup()
    except:
        pass
    question_categoru = await pin['question_category']
    question_text = await pin['box_question']
    BotDS.add_box_question(fio=fio, msg=question_text, state='Создан', category = question_categoru)
    toast('Вопрос отправлен')
