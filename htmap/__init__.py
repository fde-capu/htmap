from .htmap import Htmap
app = Krita.instance()
extension = Htmap(parent = app)
app.addExtension(extension)
