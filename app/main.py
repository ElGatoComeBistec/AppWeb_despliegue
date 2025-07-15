import web

# Rutas disponibles
urls = (
    '/', 'Index'
)

# App web
app = web.application(urls, globals())

# Controlador para la ruta /
class Index:
    def GET(self):
        return render.index()

# Plantillas HTML
render = web.template.render('templates/')

if __name__ == "__main__":
    app.run()

