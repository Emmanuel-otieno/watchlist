class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{550}?api_key={30109d7c5df50138697943d76cea3e61}'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration Child class

    Args:
        Config The parent configuration Class with General configuration settings
    '''


    DEBUG = True    