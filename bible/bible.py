import xml.etree.ElementTree as ET

langs = ['bibleTurkish', 'bibleEnglish']

for lang in langs:
    root = ET.fromstring(open(lang + '.xml').read())

    with open(lang + '.txt', 'w', encoding='utf-8') as out:
        for n in root.iter('seg'):
            out.write(n.get('id') + "\t" + n.text.strip() + '\n')
