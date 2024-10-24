pandas.errors.DatabaseError: Execution failed on sql '
               SELECT id,
                    date_time,
                    fio,
                    offer,
                    state
               FROM offer_box
               where login = 'TOLOG'
               union
               SELECT id,
                    date_time,
                    fio,
                    mood as offer,
                    state,
                    login
               FROM mood_box
               where login = 'TOLOG'
               union
               SELECT id,
                    date_time,
                    fio,
                    msg as offer,
                    state
               FROM question
               where login = 'TOLOG'
    ': SELECTs to the left and right of UNION do not have the same number of result columns
