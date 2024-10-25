Traceback (most recent call last):
  File "test.py", line 48, in <module>
    send_email_with_shortcut(admin_email, 'Ваш ярлык для входа', 'Вот ваш ярлык для входа на сайт.', shortcut_filename)
  File "test.py", line 36, in send_email_with_shortcut
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 1034, in __init__
    SMTP.__init__(self, host, port, local_hostname, timeout,
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 253, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 339, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\smtplib.py", line 1042, in _get_socket
    new_socket = self.context.wrap_socket(new_socket,
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\ssl.py", line 1040, in _create
    self.do_handshake()
  File "C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
