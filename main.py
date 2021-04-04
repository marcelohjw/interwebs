import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        if not name:
            name = 'Mjj'
        return '<h1>Hello, ' + name + '!</h1>' + 'You are Surfing'


if __name__ == "__main__":
    app.run()
