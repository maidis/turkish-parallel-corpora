# turkish-parallel-corpora

Turkish Parallel Corpora - Some English-Turkish parallel texts/corpus/corpora for use in machine translation systems.

Please let me know if the README.md file isn't sufficiently descriptive.

## kde4 and kde5

- author: Anıl Özbek
- last update: 24.11.2018
- status: not cleaned (html tags, etc.)
- alignment: perfect
- resource: [KDE](https://www.kde.org/)
- license: same with [KDE localization](https://l10n.kde.org/) files

First get Turkish KDE translations. You can use `svn co` commands yourself or run kde_tr_yapılandır.sh script from @vgezer's [translationTools](https://github.com/vgezer/translationTools) project.

```bash
$ svn co -q svn://anonsvn.kde.org/home/kde/trunk/l10n-kde4/tr/ kde4_tr_trunk
$ svn co -q svn://anonsvn.kde.org/home/kde/trunk/l10n-kf5/tr/ kde5_tr_trunk
```

Make a list all po files to use with [msgcat](https://www.gnu.org/software/gettext/manual/html_node/msgcat-Invocation.html):

```bash
$ find . -name "*.po" > kde4pofiles.txt
$ find . -name "*.po" > kde5pofiles.txt
```

Merge all po files into one huge po file (if you can do this without using a separate file list, please let me know how you did it):

```bash
$ msgcat --files-from=kde4pofiles.txt --less-than=2  --output-file=kde4_tr_trunk_20181124.po
$ msgcat --files-from=kde5pofiles.txt --less-than=2  --output-file=kde5_tr_trunk_20181124.po
```

Convert two po files to tmx with [po2tmx](http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/po2tmx.html):

```bash
$ po2tmx kde4_tr_trunk_20181124.po -o kde4_tr_trunk_20181124.tmx -l tr
$ po2tmx kde5_tr_trunk_20181124.po -o kde5_tr_trunk_20181124.tmx -l tr
```

Using one of [MosesSuite](https://github.com/leohacker/MosesSuite)'s recently updated forks convert tmx files to two separate parallel text:

```bash
$ tmx2txt.py kde4_tr_trunk_20181124.tmx en tr
$ tmx2txt.py kde5_tr_trunk_20181124.tmx en tr
```

## lonweb

- author: Anıl Özbek
- last update: 24.11.2018
- status: clean
- alignment: perfect
- resource: [lonweb.org](http://www.lonweb.org/)
- license: Some are public domain (documents, laws), some are copyrighted by lonweb.org like the charming Daisy Stories used worldwide for education and entertainment.

First open all Turkish parallel text links. Copy all tables and paste into a text file. There will be Turkish content in odd lines and English in even lines. Check file. Look through the document quickly and make sure it is in this format. Resources section may cause problems. Some titles may also cause problems.

Delete empty lines with sed:

```bash
$ sed -i '/^$/d' lonweb.org.txt
```

Export odd lines as Turkish translation:

```bash
$ sed 'n; d' lonweb.org.txt > lonweb.org.tr
```

Export even lines as English text:

```bash
$ sed '1d; n; d' lonweb.org.txt > lonweb.org.en
```

