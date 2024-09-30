from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict()
    port: str = "30052"
    max_worker: int = 10
    p2v_model_path: str = '/Users/henrychou/Sources/ailabs/hualien-music/prompt-to-vector/models/gte-large-en-v1.5'
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)
        return cls.instance
    