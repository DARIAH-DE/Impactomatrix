# Vorgehen zur Erstellung der statischen Seiten

Github das Hosten von HTML-Seiten an. Die der Impactomatrix sind auf (https://dariah-de.github.io/Impactomatrix/)[https://dariah-de.github.io/Impactomatrix/] zu finden. Am einfachsten geht es, wenn es im Projekt einen Branch mit dem Namen `gh-pages` gibt. Dort gespeicherte HTML-Dateien werden dann unter obiger Adresse angezeigt.

Für die praktische Arbeit ist es gut, in zwei verschiedenen Verzeichnissen auf der Festplatte die beiden Branches (`master` (oder ein davon abgezweigter Entwicklungsbranch) und `gh-pages`) vorliegen zu haben. Die statischen Seiten werden dann im `master`-Branch erzeugt und in den `gh-pages`-Branch kopiert und dann ins Remote-Repository gepusht.

# Arbeit mit Templates

Die Templates werden mit der Python-Bibliothek _jinja2_ ((https://pypi.python.org/pypi/Jinja2/2.8)[PyPi], Debian/Ubuntu-Paket `python-jinja2`) erstellt. Die muß also auf dem System installiert sein. In der Datei `settings.py` werden die zu generierenden Dateien angegeben sowie Ein- und Ausgabeverzeichnisse festgelegt.

Die Templates befinden sich allesamt im Verzeichnis `impactomatrix_templates`. Dabei ist `base.html` die Datei, die den grundlegenden Seitenaufbau bereitstellt, die restlichen Dateien referenzieren die `base.html` und modifizieren die dort angegebenen Blöcke `main` und gegebenenfalls `footer`. Der Inhalt der Seiten kann also in diesen Template-Dateien leicht und übersichtlich angepaßt werden.

Die Generierung der Seiten passiert also mit `python compile_templates.py`, und die fertigen Seiten werden im Verzeichnis `static_impactomatrix` abgelegt. In diesem Verzeichnis liegen auch die Stildateien für das Framework (`resources` und `old_resources`). Sollten diese modifiziert werden, müssen die auch in den `gh-pages`-Branch kopiert werden.

Ansonsten müssen nur die generierten HTML-Seiten nach `gh-pages` kopiert werden und dann entsprechend gepusht werden, damit die Änderungen online zu sehen sind.

 
