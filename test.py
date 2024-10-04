# Функция для дарения баллов
async def gift_my_balance(tab, fio, balans):
    popup('Перевод баланса',[
        put_html(f"Для перевода доступно {balans}"), 
        put_select(name='gift_people', label='Выберите кому:', options=['', 'Петя', 'Дима', 'Коля', 'Антон', 'Алексей']),
        put_html('<br>'),
        put_button("ОТПРАВИТЬ", onclick=lambda: toast("Функционал в разработке"), color='info', outline=True)
        ], size='normal')
