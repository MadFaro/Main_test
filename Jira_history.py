if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    start_server(hello_world, host='127.0.0.1', port=8080)
