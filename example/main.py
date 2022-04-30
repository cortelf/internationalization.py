from internationalization import Internationalization

i18n = Internationalization("example", "locales")
i18n.initialize()

english = i18n.get_language("en")
italian = i18n.get_language("it")
spanish = i18n.get_language("es")

print("English:", english.hello_world)
print("Italian:", italian.hello_world)
print("Spanish:", spanish.hello_world)
