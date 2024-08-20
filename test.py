with open(css_path, 'r') as f:
        css_content = f.read()

    # Подключаем CSS стили в приложении PyWebIO
    put_html(f'<style>{css_content}</style>')
put_html('<i class="fa-regular fa-window"></i> This is a check circle icon!')
