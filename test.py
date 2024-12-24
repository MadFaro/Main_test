IF v_cur_state IN ('chatting') AND v_start_time <> 0 THEN
            SET v_end_time = (
                SELECT created
                FROM chatmessage
                WHERE threadid = v_cur_threadid
                  AND kind in (2, 10, 13)
                  AND created >= v_cur_time
                ORDER BY created
                LIMIT 1
            );
        END IF;
