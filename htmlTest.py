from jinja2 import Template

class BibleVerse(object):
    def __init__(self, text, reference):
        self.text = text
        self.reference = reference

class PrayerDay(object):
    def __init__(self, date, prayer_points):
        self.date = date
        self.prayer_points = prayer_points

with open("/tmp/jinjaTest.html", 'w') as f:
    with open("template.html", 'r') as template_file:
        template = "\n".join(template_file.readlines())

        rendered_template = Template(template).render(
            title="St Ebbe's Prayer Diary",
            start_date="15th June",
            end_date="12th July",
            bible_verse = BibleVerse("Devote yourselves to prayer, being watchful and thankful", "Colossians 4:2"),
            prayer_days = [PrayerDay("Today", ["Foo", "Bar", "Baz"]), PrayerDay("Tomorrow", ["Qux", "Quux", "Bippy"])]
        )

        f.write(rendered_template)