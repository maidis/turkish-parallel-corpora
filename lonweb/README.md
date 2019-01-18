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
