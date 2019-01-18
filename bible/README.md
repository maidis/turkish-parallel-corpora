## bible

- author: Anıl Özbek
- last update: 18.01.2019
- status: quite clean
- alignment: almost perfect (merged verses must be checked separately, currently all verses that aren't available in other languages are automatically merged with the verse above)
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
