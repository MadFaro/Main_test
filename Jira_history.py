
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav  


CREATE OR REPLACE PROCEDURE p_service_level IS
BEGIN
    FOR cur_rec IN (
        WITH thread_history_cte AS (
            SELECT cth.threadid, cth.departmentid, cth.state, dtm
            FROM chatthreadhistory cth
            JOIN chatthread ct ON ct.threadid = cth.threadid
            WHERE ct.offline = 0
            AND dtm BETWEEN p_dtmfrom AND p_dtmto
        )
        SELECT threadid, departmentid, state, dtm
        FROM thread_history_cte
        ORDER BY threadid, dtm
    ) LOOP
        -- Reset for each new thread
        IF cur_rec.threadid <> cur_rec.threadid THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        -- Consider queue time after bot if chat initially went to a bot
        -- Do not consider dialogue if it was not in the chatting state and was closed by the operator
        IF cur_rec.state IN ('chatting_with_robot', 'closed_by_operator') THEN
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;

        IF cur_rec.state = 'queue' AND v_start_time IS NULL THEN
            v_start_time := cur_rec.dtm;
        END IF;

        IF cur_rec.state = 'chatting' AND v_start_time IS NOT NULL THEN
            SELECT MIN(created) INTO v_end_time
            FROM chatmessage
            WHERE threadid = cur_rec.threadid
              AND kind IN (2, 10, 13)
              AND created > cur_rec.dtm;

            -- Handling if no records found
            EXCEPTION
                WHEN NO_DATA_FOUND THEN
                    v_end_time := NULL;
        END IF;

        IF v_start_time IS NOT NULL AND v_end_time IS NOT NULL THEN
            INSERT INTO tmp_stats_service_level (
                threadid,
                department_id,
                got_into_common_queue_time,
                start_chatting_time
            ) VALUES (
                cur_rec.threadid,
                cur_rec.departmentid,
                v_start_time,
                v_end_time
            );
            v_start_time := NULL;
            v_end_time := NULL;
        END IF;
    END LOOP;
END;
/
