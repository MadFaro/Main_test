create or replace PROCEDURE             "KUZ_SEND_MAIL"(addressee in varchar2, text in varchar2, theme in varchar2)
is
cnt number;
FUNCTION MIMEHEADER_ENCODE( s_string VARCHAR2 )
    RETURN VARCHAR2
  IS
  BEGIN
    RETURN '=?windows-1251?B?' || utl_raw.cast_to_varchar2( utl_encode.base64_encode
    ( utl_raw.cast_to_raw( convert( s_string, 'CL8MSWIN1251' ) ) ) ) || '?=';
  END;
begin
  
  
  sys.send_mail_cvm2_new(p_to => addressee,
  p_from => 'DirBO-DWH',
  p_subject => theme,
  p_text_msg =>  translate(text, 'йцукенгшщзхъфывапролджэячсмитьбю', 'icukengsszx_fivaproldjaacsmit_bu'),
  p_smtp_host => '0.0.0.0');
end ;
