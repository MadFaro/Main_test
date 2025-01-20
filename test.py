p_text_msg => UTL_RAW.CAST_TO_VARCHAR2(
            UTL_ENCODE.BASE64_ENCODE(UTL_RAW.CAST_TO_RAW(text))
        ),
