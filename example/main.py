from internationalization import Internationalization
from internationalization.loaders import YAMLLoader

i18n = Internationalization()
i18n.initialize(YAMLLoader(directory="locales"))

english = i18n.get_language("en")
italian = i18n.get_language("it")
spanish = i18n.get_language("es")

print("English:", english.hello_world)
print("Italian:", italian.hello_world)
print("Spanish:", spanish.hello_world)
