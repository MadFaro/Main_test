import pandas as pd
from jira import JIRA




# Пишем JQL запрос для выборки нужных нам заявок для импорта
# Запрос ниже выгружаете данные за вчера по выбранным проектам
JQL = 'project in (yourpoject_1, yourpoject_2) AND Updated>=startOfDay(-1d) AND Updated<=startOfDay(0d)'
# Создаем подключение к серверу
jira = JIRA(
                options={'server': 'https://yourjiraserver'}, 
                basic_auth=('username', 'password')
            )
# Выгружаем список задач по нашему JQL запросу
# maxResults - максимальное количество выгружаемых задач
jira_key = jira.search_issues(JQL, maxResults=1000)
# Перебираем циклом список задач, получаем их ID и записывам в history_log
history_log = []
for keyid in range(len(jira_key)):
    issue = jira.issue(str(jira_key[keyid]), expand='changelog')
    changelog = issue.changelog
    for history in changelog.histories:
        for change in history.items:
            if change.field == 'status':
                statuses = {}
                statuses['ID'] = str(jira_key[keyid])
                statuses['fromString'] = change.fromString
                statuses['toString'] = change.toString
                statuses['created'] = history.created
                statuses['author'] = history.author.displayName
                history_log.append(statuses)
# Сохраняем histiry_log как файл Excel
pd.DataFrame(history_log).to_excel('jira.xlsx', index=False)