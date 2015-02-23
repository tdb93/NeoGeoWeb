import csv

with open('calgarycsv.csv','r') as f:
    geog_csv = csv.reader(f)
    for row in geog_csv:
        if row[2]=="Price":
            continue
        var1=int(row[2])
        print type(var1)
        if var1<=2000:
            print ("<Placemark>\n    <name/>\n    <styleUrl>#style1</styleUrl>\n    <description/>\n    <ExtendedData>\n        <Data name='price'>\n            <value>%s</value>\n        </Data>\n        <Data name='bed'>\n            <value>%s</value>\n        </Data>\n        <Data name='bath'>\n            <value>%s</value>\n        </Data>\n        <Data name='sqfoot'>\n            <value>%s</value>\n        </Data>\n        <Data name='image'>\n            <value>%s</value>\n        </Data>\n        <Data name='outputaddress'>\n            <value>%s</value>\n        </Data>\n        <Data name='URL'>\n            <value>%s</value>\n        </Data>\n    </ExtendedData>\n    <Point>\n        <coordinates>\n            %s,%s\n        </coordinates>\n    </Point>\n</Placemark>\n"%(row[2],row[5],row[6],row[7],row[8],row[11],row[1],row[10],row[9]))
        else:
            print ("<Placemark>\n    <name/>\n    <styleUrl>#style2</styleUrl>\n    <description/>\n    <ExtendedData>\n        <Data name='price'>\n            <value>%s</value>\n        </Data>\n        <Data name='bed'>\n            <value>%s</value>\n        </Data>\n        <Data name='bath'>\n            <value>%s</value>\n        </Data>\n        <Data name='sqfoot'>\n            <value>%s</value>\n        </Data>\n        <Data name='image'>\n            <value>%s</value>\n        </Data>\n        <Data name='outputaddress'>\n            <value>%s</value>\n        </Data>\n        <Data name='URL'>\n            <value>%s</value>\n        </Data>\n    </ExtendedData>\n    <Point>\n        <coordinates>\n            %s,%s\n        </coordinates>\n    </Point>\n</Placemark>\n"%(row[2],row[5],row[6],row[7],row[8],row[11],row[1],row[10],row[9]))

