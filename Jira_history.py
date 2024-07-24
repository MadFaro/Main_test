select
    a.hour as hour,
    a.chat_count as on_hold_count,
    coalesce(b.chat_count, 0) as from_on_hold_count,
    coalesce(c.chat_count, 0) as on_hold_without_operator_message,
    coalesce(d.chat_count, 0) as on_hold_after_operator_reply
from
    (
        select
            trunc(dtm, 'hh') as hour,
            count(distinct threadid) as chat_count
        from
            your_table_name
        where
            state = 'on_hold' and event = 'sys.hold_chat'
        group by
            trunc(dtm, 'hh')
    ) a
left join
    (
        select
            trunc(a.dtm, 'hh') as hour,
            count(distinct a.threadid) as chat_count
        from
            your_table_name a
        join
            your_table_name b on a.threadid = b.threadid and a.number_ = b.number_ - 1
        where
            a.state = 'on_hold' and a.event = 'sys.hold_chat'
            and b.state = 'chatting' and b.event = 'operator.accept'
        group by
            trunc(a.dtm, 'hh')
    ) b on a.hour = b.hour
left join
    (
        select
            trunc(dtm, 'hh') as hour,
            count(distinct threadid) as chat_count
        from
            your_table_name a
        where
            state = 'on_hold' and event = 'sys.hold_chat'
            and not exists (
                select 1
                from your_table_name b
                where a.threadid = b.threadid
                and b.state = 'chatting'
                and b.event = 'operator.accept'
                and b.number_ < a.number_
            )
        group by
            trunc(dtm, 'hh')
    ) c on a.hour = c.hour
left join
    (
        select
            trunc(a.dtm, 'hh') as hour,
            count(distinct a.threadid) as chat_count
        from
            your_table_name a
        join
            your_table_name b on a.threadid = b.threadid and a.number_ > b.number_
        where
            a.state = 'on_hold' and a.event = 'sys.hold_chat'
            and b.state = 'chatting' and b.event = 'operator.accept'
        group by
            trunc(a.dtm, 'hh')
    ) d on a.hour = d.hour
order by
    a.hour;

