from ..app import render_template


class HomeController:
    def __init__(self):
        pass

    @staticmethod
    def home():
        return render_template('pages/home.html')

    @staticmethod
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @staticmethod
    def server_error(error):
        return render_template('errors/500.html'), 500
