import log


class Example:

    def __init__(self):
        self.__log = log.Log().get_logger('LOG_FILE_EXAMPLE.log')

    def run(self):
        print('Tipos de logs: Revisa su estructura')

        self.__log.info('Esto es para simplemente informar')

        self.__log.warning('Esto para dar aviso de peligro')

        self.__log.error('Esto es un error')

        print(f'Ahora revisa el archivo LOG_FILE_EXAMPLE.log')


if __name__ == '__main__':
    example = Example()
    example.run()