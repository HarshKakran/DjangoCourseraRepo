import csv
from unesco.models import Category, ISO, Region, State, Site
def run():
    fhand = open('scripts/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    ISO.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()
    k=[]

    for row in reader:
        print(row)
        k.append(row)
        with open('listfile.txt', 'w') as filehandle:
            for listitem in k:
                filehandle.write('%s' % listitem)

        s, created = State.objects.get_or_create(name=row[8])
        c, created = Category.objects.get_or_create(name=row[7])
        i, created = ISO.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            a = int(row[6])
        except:
            a = None


        Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=row[4],latitude=row[5],
                 area_hect=a,category=c,states=s,region=r,iso=i).save()
