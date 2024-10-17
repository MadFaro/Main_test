async def discount_noadmin(sdep, tab, fio, id):
    try:
        clear()
    except:
        pass
    ban = open('discount/img/ban.jpg', 'rb').read()
    df_product = pd.read_sql(sql.sql_discount, connect("Convert/db/shop.db"))
    put_row([
    None,
    None,
    put_button("\U0001F3E0\n\r        Главная        ", onclick=lambda: game_noadmin(sdep, tab, fio, id), color='dark', outline=True).style('font-size: 2vh')]).style('padding:0.4em;background:rgb(255 255 255);grid-template-columns:0.1fr 1fr 0.1fr;')
    put_image(ban, width='auto', height='auto').style('display: block;margin-left: auto;margin-right: auto')


    put_html(f"""
        <footer class="footer">
        {fio}
        </footer>
       """).style("width:100%;z-index:2147483647;bottom:0px")
