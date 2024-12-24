IF v_cur_state IN ('chatting') AND v_start_time <> 0 THEN
    SELECT created
    INTO v_end_time
    FROM chatmessage
    WHERE threadid = v_cur_threadid
      AND kind IN (2, 10, 13)
      AND created >= v_cur_time
    ORDER BY created
    FETCH FIRST 1 ROW ONLY; -- Альтернатива ROWNUM
END IF;
