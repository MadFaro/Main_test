create or replace PROCEDURE             "KUZ_SEND_MAIL"(addressee in varchar2, text in varchar2, theme in varchar2)
is
cnt number;
begin
  
    SYS.SEND_MAIL_REL2(p_to => addressee,
  p_from => 'an@an.ru',
  p_subject => theme,
  p_text_msg => text,
  p_smtp_host => '10'); 
  
        exception
        when others then                      
                SYS.SEND_MAIL_REL2(p_to => 'an@an.ru',
                  p_from => 'an@an.ru',
                  p_subject => theme,
                  p_text_msg => text,
                  p_smtp_host => '10'); 
        
  
end kuz_send_mail;
