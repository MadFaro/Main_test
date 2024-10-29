def delete_cookie(key: str):
    """Delete cookie using JavaScript."""
    run_js(f"document.cookie = '{key}=; Max-Age=0; path=/;';")  # Удаляем куку
