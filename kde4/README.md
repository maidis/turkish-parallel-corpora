## kde4 and kde5

- author: Anıl Özbek
- last update: 24.11.2018
- status: not cleaned (html tags, etc.)
- alignment: perfect
- resource: [KDE](https://www.kde.org/)
- license: same with [KDE localization](https://l10n.kde.org/) files

First get Turkish KDE translations. You can use `svn co` commands yourself or run `kde_tr_yapılandır.sh` script from @vgezer's [translationTools](https://github.com/vgezer/translationTools) project.

```bash
$ svn co -q svn://anonsvn.kde.org/home/kde/trunk/l10n-kde4/tr/ kde4_tr_trunk
```

Make a list all po files to use with [msgcat](https://www.gnu.org/software/gettext/manual/html_node/msgcat-Invocation.html):

```bash
$ find . -name "*.po" > kde4pofiles.txt
```

Merge all po files into one huge po file (if you can do this without using a separate file list, please let me know how you did it):

```bash
$ msgcat --files-from=kde4pofiles.txt --less-than=2  --output-file=kde4_tr_trunk_20181124.po
```

Convert two po files to tmx with [po2tmx](http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/po2tmx.html):

```bash
$ po2tmx kde4_tr_trunk_20181124.po -o kde4_tr_trunk_20181124.tmx -l tr
```

Using one of [MosesSuite](https://github.com/leohacker/MosesSuite)'s recently updated forks convert tmx files to two separate parallel text:

```bash
$ tmx2txt.py kde4_tr_trunk_20181124.tmx en tr
```
