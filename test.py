CREATE OR REPLACE PROCEDURE KUZ_SEND_MAIL (
    addressee IN VARCHAR2,
    text IN VARCHAR2,
    theme IN VARCHAR2
) IS
    FUNCTION MIMEHEADER_ENCODE(s_string VARCHAR2) RETURN VARCHAR2 IS
    BEGIN
        RETURN '=?UTF-8?B?' || UTL_RAW.CAST_TO_VARCHAR2(
            UTL_ENCODE.BASE64_ENCODE(UTL_RAW.CAST_TO_RAW(s_string))
        ) || '?=';
    END;
BEGIN
    -- Конвертация темы в MIME-заголовок для корректной кодировки
    sys.send_mail_cvm2_new(
        p_to => addressee,
        p_from => 'DirBO-DWH',
        p_subject => MIMEHEADER_ENCODE(theme), -- Кодируем тему письма
        p_text_msg => text,                     -- Используем текст без трансляции
        p_smtp_host => '0.0.0.0'
    );
END;
