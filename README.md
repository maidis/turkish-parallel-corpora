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

## bible

- author: Anıl Özbek
- last update: 18.01.2019
- status: quite clean
- alignment: perfect
- resource: [bible-corpus](https://github.com/christos-c/bible-corpus)
- license: same with bibleTurkish.xml and bibleEnglish.xml files from bible-corpus

Download English and Turkish versions of Bible from [bible-corpus](https://github.com/christos-c/bible-corpus):

```bash
wget https://raw.githubusercontent.com/christos-c/bible-corpus/master/bibles/Turkish.xml
wget https://raw.githubusercontent.com/christos-c/bible-corpus/master/bibles/English.xml
```

Rename files to have more specific names:

```bash
mv Turkish.xml bibleTurkish.xml
mv English.xml bibleEnglish.xml
```

Run `bible.py` to get text versions of XML files with `<verse_name><tab><verse>` format:

```python
import xml.etree.ElementTree as ET

langs = ['bibleTurkish', 'bibleEnglish']

for lang in langs:
    root = ET.fromstring(open(lang + '.xml').read())

    with open(lang + '.txt', 'w', encoding='utf-8') as out:
        for n in root.iter('seg'):
            out.write(n.get('id') + "\t" + n.text.strip() + '\n')
```

Modify above code and run again:

```python
import xml.etree.ElementTree as ET

langs = ['bibleTurkish', 'bibleEnglish']

for lang in langs:
    root = ET.fromstring(open(lang + '.xml').read())

    with open(lang + '_id' + '.txt', 'w', encoding='utf-8') as out:
        for n in root.iter('seg'):
            out.write(n.get('id') + '\n')
```

Get diff of those last two files:

```bash
diff -Naur bibleEnglish_id.txt bibleTurkish_id.txt > bible.diff
```

To figure out which verses need to be merged, run following [sed commands](https://unix.stackexchange.com/questions/223897/sed-how-to-remove-all-lines-that-do-not-match):

```bash
sed '/^-b/!d' bible.diff > mergedInEnglish.txt
sed '/^+b/!d' bible.diff > mergedInTurkish.txt
```

Get rid of `-` characters in `mergedInEnglish.txt` and `+` characters in `mergedInTurkish.txt` automatically or manually.

Create a text file named `code.txt` and add [following](https://stackoverflow.com/questions/9999934/sed-joining-lines-depending-on-the-second-one) into it:

```bash
sed -i 'N;s/\n\t/ /;P;D' bibleEnglish.txt
```

Then run following [sed command](https://unix.stackexchange.com/questions/81904/repeat-each-line-multiple-times) to dublicate this line 895 times:

```bash
sed -i 'h;:a;s/[^\n]\+/&/895;t;G;ba' code.txt
```

Open `mergedInEnglish.txt` text file and copy all line of it. Then open `code.txt` with Kate or any other text editor with block selection mode supoort. Select after `\n` at all lines and paste. This is how it should look:

```bash
sed -i 'N;s/\n-b.GEN.1.15\t/ /;P;D' bibleEnglish.txt
...
sed -i 'N;s/\n-b.REV.21.20\t/ /;P;D' bibleEnglish.txt
```

Make `code.txt` executable and run it. This will take some time. Be patient.

```bash
./code.txt
```

Using `mergedInTurkish.txt` do same thing for `bibleTurkish.txt`. You can do it manually because there are only two lines.

Get rid of all `<verse_name><tab>` in both `bibleTurkish.txt` and `bibleEnglish.txt` files. For this task you can use block selection mode or some other magic `sed` commands.

Remove all `‹‹` and `››` in `bibleTurkish.txt` file. Also replace all `‹` and `›` with `"` in same file.

Look at some random lines to check if the text is really parallel.
