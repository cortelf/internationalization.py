# Internationalization.py
Provides simple and powerful i18n realization

## Installation

#### With pip
```shell
pip install internationalization.py
```
#### Via Git
```shell
git clone https://github.com/cortelf/internationalization.py
cd internationalization.py
python setup.py install
```

## Usage
#### Create directory for yaml files
```shell
mkdir yourdirectory
```
#### Write your yaml files
You can use .yml or .yaml file extensions
```shell
en.yml
```
```yaml
hello_world: Hello World!
```
```shell
it.yml
```
```yaml
hello_world: Ciao mondo!
```
#### In root of your app initialize singleton
```python
from internationalization import Internationalization
from internationalization.loaders import YAMLLoader

i18n = Internationalization()
i18n.initialize(YAMLLoader("yourdirectory"))
```
#### It's ready to use in any place
```python
from internationalization import Internationalization

i18n = Internationalization()
english = i18n.get_language("en")
italian = i18n.get_language("it")

print("English:", english.hello_world)
print("Italian:", italian.hello_world)
```