from django.apps import AppConfig


class DiaryConfig(AppConfig):
    name = 'diary'

    def ready(self):
        import diary.signals
