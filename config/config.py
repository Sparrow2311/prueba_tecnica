from configparser import ConfigParser


def config(filename='config/data.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Sección {0} no encontrada en el {1} fichero'.format(section, filename))

    return db