def delete_cookie(key: str):
    """Delete cookie."""
    _init_cookie_client()
    run_js("document.cookie = key + '=; Max-Age=0; path=/;';", key=key)
