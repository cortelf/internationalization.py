from internationalization import Localization

localization = Localization("example", "locales")
localization.initialize()

english = localization.get_language("en")
italian = localization.get_language("it")
spanish = localization.get_language("es")

print("English:", english.hello_world)
print("Italian:", italian.hello_world)
print("Spanish:", spanish.hello_world)
