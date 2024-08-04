class Config:
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    SECRET_KEY = 'a3d9fbbd1e24f2a89cf3d29210b3ae5c16e3d65e45a6e8490bbd2b9d8a56e0cd'
    JWT_SECRET_KEY = 'f2a43fba1e18a2b93cde9a82f5b1ae4e92c3e79e49a9fbd7c8b6b9d9a8f7e2c5'
