put_button(" Письмо ", onclick=lambda: put_html(f'''
                                                                                                    <script>
                                                                                                        var mailtoLink = "mailto:{df["login_customer"].iloc[0]}?subject=Заказ {product_id}&body=Привет!<br>{html_json}";
                                                                                                        var link = document.createElement("a");
                                                                                                        link.href = mailtoLink;
                                                                                                        link.style.display = "none"; // Скрыть элемент
                                                                                                        document.body.appendChild(link);
                                                                                                        link.click();
                                                                                                        document.body.removeChild(link);
                                                                                                    </script>
                                                                                                '''), color='success', outline=True)
