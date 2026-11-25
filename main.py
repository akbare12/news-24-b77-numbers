import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
SERIF=lambda s:F("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",s)
SANS=lambda s:F("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
SANSB=lambda s:F("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",s)
CREAM=(247,242,231);INK=(20,20,20);RED=(178,34,34);NAVY=(27,58,88);GOLD=(176,141,60);TEAL=(18,110,105);CHIP={"CONFIRMED":(34,120,60),"OFFICIAL":(30,90,160),"REPORTED":(90,100,115),"CLAIM":(200,110,20)}
def wrap(d,t,f,w):
    ls=[];cur=""
    for wd in t.split():
        s=(cur+" "+wd).strip()
        if d.textlength(s,font=f)<=w: cur=s
        else:
            if cur: ls.append(cur)
            cur=wd
    if cur: ls.append(cur)
    return ls
def chip(d,x,y,s):
    c=CHIP[s];w=d.textlength(s,font=SANSB(8))+10;d.rounded_rectangle([x,y,x+w,y+13],radius=3,fill=c);d.text((x+5,y+2),s,font=SANSB(8),fill=(255,255,255));return w
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi hot-pot blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
NUM=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow close"),("+8.99%","Taiex record"),("25","killed or missing in Yemen"),("26","Cikande fire toll"),("10/12","Huawei guilty counts"),("96","drones launched at Ukraine")]
REG=[("Europe",9,(27,58,88)),("Middle East",8,(178,34,34)),("Asia",8,(176,141,60)),("Africa",2,(18,110,105)),("Americas",7,(90,60,140)),("World/Space",4,(90,100,115))]
HERO=[("1 RIYADH \u00b7 MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","The PIF tower is hit for the second time in a week; 11 are hurt, including 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians.","Saudi officials","riyadh"),("2 SHANGHAI \u00b7 ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, faces a probe over serious violations, the fourth Politburo member to fall.","CCDI","shanghai"),("3 NEW YORK \u00b7 US/TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US jury convicts Huawei on trade-secret theft and bank fraud, clearing it of racketeering. Sentencing is set for September 2027.","US court","huawei")]
CARD=[(4,"ZAPORIZHZHIA \u00b7 EUROPE/WAR","REPORTED","Russian attacks kill 9 across Ukraine in a day","Nine killed and 81 hurt as 96 drones are launched and 73 are shot down or jammed.","Kyiv officials","drone"),(5,"CAS \u00b7 AFRICA/SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","Morocco forfeit 3-0, so Senegal win 1-0 and take the trophy back.","CAS","trophy"),(6,"HORMUZ \u00b7 MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","Navigation is cut at 18:58 UTC and a no-go area is set north of Khasab, Oman.","UKMTO","ship"),(7,"NEW YORK \u00b7 WORLD/MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow ends at 50,018 while the Taiex jumps a record 8.99 percent.","NYSE close","chart"),(8,"REDMOND \u00b7 WORLD/TECH","REPORTED","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, recovery is targeted in one hour with five workstreams.","Reuters","server"),(9,"ESKISEHIR \u00b7 EUROPE","REPORTED","Turkish military helicopter crash kills 5","An AS-532 helicopter comes down in Eskisehir at 19:52 UTC, killing five.","Turkish officials","heli"),(10,"CARTAGENA \u00b7 AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","Five elderly women are freed and airport landings are halted for about 45 minutes.","Colombian officials","shop"),(11,"ADEN \u00b7 MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advance to within 60 km of Aden in Yemen at 16:51 UTC.","Wires","desert"),(12,"LAHJ \u00b7 MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","A bus and truck are hit in Wadi Maabaq, Lahj, at 10:42 UTC, killing 25.","Yemeni officials","truck"),(13,"JIUQUAN \u00b7 WORLD/SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","Muhammad Zeeshan Ali of Pakistan joins Tang Hongbo and Wu Yi on Shenzhou-24.","CMSA","rocket")]
ALSO=[(14,"Ankara: Haftar visits Turkey for the first time.","REPORTED"),(15,"London: UK sanctions Houthis + 4 officials.","OFFICIAL"),(16,"Villavicencio: Car bomb injures 23.","REPORTED"),(17,"Gaza: Israel kills Hamas internal security chief.","REPORTED"),(18,"Baghdad: Iraq takes control of Kurdish oilfields.","OFFICIAL"),(19,"Gaza: Meningitis alert, 272 cases in October.","OFFICIAL"),(20,"DR Congo: Missing Cessna 208, rebels claim shootdown.","CLAIM"),(21,"Hanoi: Hot-pot blast kills at least 6.","REPORTED"),(22,"Gulf of Finland: Ukraine hits Russian ship Sparta II.","REPORTED"),(23,"Kuala Lumpur: Malaysia to return thousands of migrants.","OFFICIAL"),(24,"Ulleungdo: S. Korea shelter order as jets enter ADIZ.","OFFICIAL"),(25,"Dhaka: Hasina plans return on 16 Dec.","REPORTED"),(26,"The Hague: 14 nations back ICJ Myanmar ruling.","REPORTED"),(27,"Jakarta: Indonesia nominates 2 VP candidates.","OFFICIAL"),(28,"Beijing: China sentences official Ma to death for spying.","OFFICIAL"),(29,"Brussels: NATO vows defence against space threat.","OFFICIAL"),(30,"Mexico City: US drone aided El Chapo capture, Fri 20 Nov.","REPORTED"),(31,"San Salvador: Bukele names 3 soldiers killed in Haiti.","OFFICIAL"),(32,"Ottawa: Pentagon rebukes Canada; only 41.9% of air fleet ready.","REPORTED"),(33,"Washington: US adds Megaspeed to trade blacklist.","OFFICIAL"),(34,"Kyiv: Zelensky urges Ukraine-Russia-US-Europe talks.","REPORTED"),(35,"Ras Al Khaimah: Bus-truck crash kills 13.","REPORTED"),(36,"London: England record 5,258 heat deaths in summer 2026.","OFFICIAL"),(37,"Kourou: Ariane 6 lofts 36 Amazon satellites.","OFFICIAL"),(38,"Cikande: Factory-fire toll rises to 26.","REPORTED")]
PINS={1:(46.7,24.7,"Riyadh"),2:(121.5,31.2,"Shanghai"),3:(-74.0,40.7,"New York"),4:(35.2,47.8,"Zaporizhzhia"),5:(-17.4,14.7,"Dakar"),6:(56.3,26.5,"Hormuz"),7:(-74.0,40.7,"New York"),8:(-122.1,47.7,"Redmond"),9:(30.5,39.8,"Eskisehir"),10:(-75.5,10.4,"Cartagena"),11:(45.0,12.8,"Aden"),12:(44.9,13.0,"Lahj"),13:(98.5,39.7,"Jiuquan")}
OFF={7:(16,14),12:(-18,16),6:(12,-14),9:(14,10)}
LAND=[[(-168,66),(-155,71),(-140,70),(-130,71),(-125,60),(-124,49),(-120,34),(-114,29),(-105,23),(-97,26),(-90,21),(-86,16),(-83,9),(-79,9),(-81,13),(-87,15),(-92,15),(-97,16),(-94,18),(-90,19),(-86,21),(-80,25),(-76,35),(-74,40),(-70,42),(-68,45),(-65,44),(-60,47),(-55,47),(-60,52),(-65,58),(-68,58),(-78,62),(-85,66),(-92,66),(-95,69),(-110,68),(-125,70),(-140,70),(-155,71),(-168,66)],[(-58,64),(-52,60),(-43,60),(-40,64),(-32,68),(-25,70),(-20,74),(-25,76),(-35,77),(-50,76),(-58,74),(-60,70),(-58,64)],[(-79,9),(-77,4),(-80,-3),(-81,-6),(-77,-12),(-72,-18),(-70,-23),(-70,-30),(-72,-37),(-73,-44),(-74,-50),(-70,-54),(-66,-55),(-65,-45),(-62,-41),(-57,-38),(-52,-33),(-48,-28),(-41,-23),(-39,-17),(-35,-9),(-35,-6),(-40,-3),(-44,-2),(-50,0),(-52,4),(-60,8),(-62,9),(-68,11),(-72,12),(-77,8),(-79,9)],[(-17,15),(-17,21),(-15,27),(-10,31),(-5,35),(0,36),(10,37),(11,34),(20,32),(30,31),(32,31),(34,28),(35,23),(37,18),(40,15),(43,11),(48,11),(51,11),(51,2),(48,-2),(42,-5),(40,-10),(40,-16),(36,-20),(33,-26),(28,-33),(20,-35),(17,-32),(15,-27),(12,-18),(13,-12),(9,-1),(9,4),(4,6),(-8,5),(-13,8),(-17,12),(-17,15)],[(-10,36),(-9,43),(-2,44),(-1,46),(-4,48),(-1,49),(2,51),(5,53),(8,57),(10,59),(5,60),(5,62),(10,64),(18,69),(25,71),(32,70),(40,68),(50,69),(60,69),(68,73),(75,73),(80,73),(90,75),(100,77),(110,74),(120,73),(130,72),(140,72),(150,70),(158,69),(162,66),(170,67),(178,65),(178,62),(170,60),(162,60),(158,56),(150,59),(142,55),(140,50),(135,44),(130,42),(127,40),(122,38),(120,32),(122,28),(118,25),(110,20),(108,18),(105,10),(103,8),(100,8),(98,12),(94,16),(92,21),(89,22),(86,20),(82,17),(80,13),(77,8),(75,12),(73,16),(70,21),(66,25),(62,25),(58,26),(56,27),(52,26),(50,29),(48,30),(44,29),(40,28),(39,24),(38,20),(35,18),(34,15),(36,12),(39,12),(43,12),(45,13),(48,14),(50,16),(52,16),(55,17),(58,19),(59,22),(57,25),(54,26),(52,25),(50,26),(48,28),(-10,36)],[(-10,36),(-10,50),(-5,50),(-3,53),(-5,56),(-2,58),(0,53),(2,51),(-10,36)],[(-2,36),(0,39),(3,42),(7,44),(10,44),(12,42),(14,40),(16,38),(18,40),(15,44),(12,45),(8,44),(3,43),(0,40),(-2,36)],[(114,-22),(114,-30),(115,-35),(120,-34),(124,-33),(129,-32),(132,-32),(135,-35),(138,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(150,-22),(146,-19),(142,-15),(142,-11),(137,-12),(135,-17),(132,-12),(130,-13),(126,-14),(122,-17),(118,-20),(114,-22)],[(95,5),(98,3),(100,0),(104,-2),(106,-6),(110,-7),(114,-8),(119,-9),(120,-10),(116,-9),(112,-7),(108,-6),(104,-5),(100,0),(95,5)]]
def scene(d,x,y,w,h,k):
    d.rectangle([x,y,x+w,y+h],fill=(208,220,230))
    if k=="riyadh":
        d.rectangle([x,y,x+w,y+h],fill=(18,28,52));d.ellipse([x+w-52,y+8,x+w-22,y+38],fill=(240,230,180))
        for i,(bx,bw,bh) in enumerate([(0,26,44),(30,22,62),(56,30,80),(90,20,52),(114,24,66),(142,20,48),(166,26,58),(196,22,44),(222,24,60),(250,20,50),(276,26,70),(302,18,46)]): d.rectangle([x+bx,y+h-bh,x+bx+bw,y+h],fill=(52,68,104))
        d.rectangle([x+138,y+6,x+182,y+h],fill=(120,140,180));d.polygon([(x+138,y+6),(x+182,y+6),(x+160,y-14)],fill=(150,170,205));d.rectangle([x+158,y+20,x+162,y+h],fill=(240,200,90))
        for yy in range(y+26,y+h-10,14): d.rectangle([x+146,yy,x+152,yy+6],fill=(255,220,120));d.rectangle([x+168,yy,x+174,yy+6],fill=(255,220,120))
        d.ellipse([x+196,y+34,x+232,y+58],fill=(120,120,120));d.ellipse([x+206,y+26,x+238,y+50],fill=(150,150,150));d.ellipse([x+216,y+18,x+246,y+40],fill=(180,180,180));d.polygon([(x+252,y+30),(x+272,y+36),(x+252,y+42)],fill=(220,80,60));d.rectangle([x+238,y+34,x+252,y+38],fill=(40,40,40))
    elif k=="shanghai":
        d.rectangle([x,y,x+w,y+h],fill=(140,30,30));d.rectangle([x,y+h-26,x+w,y+h],fill=(90,20,20));d.rectangle([x+40,y+18,x+w-40,y+34],fill=(200,170,80));d.rectangle([x+60,y+34,x+90,y+h-26],fill=(120,25,25));d.rectangle([x+w-90,y+34,x+w-60,y+h-26],fill=(120,25,25));d.rectangle([x+110,y+34,x+w-110,y+h-26],fill=(60,15,15));d.ellipse([x+w//2-28,y+44,x+w//2+28,y+100],fill=(200,170,80));d.rectangle([x+w//2-18,y+60,x+w//2+18,y+h-26],fill=(240,220,160));d.rectangle([x+16,y+h-58,x+86,y+h-30],fill=(255,255,255));d.line([x+22,y+h-50,x+80,y+h-50],fill=RED,width=2);d.line([x+22,y+h-42,x+80,y+h-42],fill=INK,width=1);d.line([x+22,y+h-36,x+62,y+h-36],fill=INK,width=1);d.ellipse([x+70,y+h-56,x+84,y+h-42],fill=RED)
    elif k=="huawei":
        d.rectangle([x,y,x+w,y+h],fill=(27,58,88));d.rectangle([x,y+h-22,x+w,y+h],fill=(180,180,170));d.rectangle([x+30,y+34,x+w-30,y+52],fill=(240,235,220));d.polygon([(x+22,y+34),(x+w-22,y+34),(x+34,y+18),(x+w-34,y+18)],fill=(200,190,170))
        for cx in [70,130,190,250]:
            d.rectangle([x+cx-6,y+52,x+cx+6,y+h-22],fill=(240,235,220))
        d.ellipse([x+w//2-34,y+62,x+w//2+34,y+96],fill=(255,255,255));d.text((x+w//2-26,y+72),"HUAWEI",font=SANSB(11),fill=RED);d.rectangle([x+18,y+h-40,x+120,y+h-30],fill=(120,80,40));d.rectangle([x+52,y+h-52,x+86,y+h-40],fill=(90,60,30));d.ellipse([x+236,y+h-44,x+296,y+h-28],fill=(240,200,90))
    elif k=="drone":
        d.rectangle([x,y,x+w,y+h],fill=(18,28,52));d.polygon([(x+20,y+h-6),(x+60,y+10),(x+100,y+h-6)],fill=(70,90,120));d.polygon([(x+110,y+h-6),(x+150,y+16),(x+188,y+h-6)],fill=(50,70,100));d.ellipse([x+120,y+4,x+140,y+18],fill=(220,220,220));d.line([x+110,y+11,x+150,y+11],fill=(220,220,220),width=2);d.ellipse([x+30,y+8,x+44,y+18],fill=(255,200,90))
    elif k=="trophy":
        d.rectangle([x,y,x+w,y+h],fill=(18,110,105));d.ellipse([x+w//2-16,y+4,x+w//2+16,y+26],fill=(240,200,90));d.rectangle([x+w//2-5,y+24,x+w//2+5,y+30],fill=(240,200,90));d.rectangle([x+w//2-14,y+30,x+w//2+14,y+34],fill=(200,170,60));d.rectangle([x+8,y+8,x+30,y+20],fill=(34,120,60));d.rectangle([x+w-30,y+8,x+w-8,y+20],fill=(178,34,34))
    elif k=="ship":
        d.rectangle([x,y,x+w,y+h],fill=(150,190,210));d.rectangle([x,y+h-10,x+w,y+h],fill=(30,80,130));d.polygon([(x+40,y+h-10),(x+150,y+h-10),(x+140,y+h-22),(x+50,y+h-22)],fill=(178,34,34));d.rectangle([x+70,y+h-32,x+120,y+h-22],fill=(240,240,240));d.rectangle([x+94,y+2,x+98,y+12],fill=(200,200,200));d.rectangle([x+150,y+6,x+170,y+h-10],fill=(90,90,90))
    elif k=="chart":
        d.rectangle([x,y,x+w,y+h],fill=(255,255,255));d.line([x+8,y+h-8,x+w-8,y+6],fill=(34,120,60),width=3);d.line([x+8,y+h-8,x+60,y+h-16,x+120,y+h-22,x+w-8,y+6],fill=(34,120,60),width=2);d.text((x+10,y+2),"50,018",font=SANSB(12),fill=(34,120,60));d.line([x+8,y+12,x+w-8,y+12],fill=(200,60,60),width=1)
    elif k=="server":
        d.rectangle([x,y,x+w,y+h],fill=(40,40,48));d.rectangle([x+20,y+6,x+w-20,y+h-6],fill=(70,70,80));d.rectangle([x+30,y+10,x+w-30,y+16],fill=(200,60,60));d.text((x+34,y+9),"CODE RED",font=SANSB(9),fill=(255,255,255));d.rectangle([x+30,y+20,x+w-30,y+26],fill=(30,120,200));d.rectangle([x+30,y+28,x+w-30,y+32],fill=(30,120,200))
    elif k=="heli":
        d.rectangle([x,y,x+w,y+h],fill=(180,200,220));d.polygon([(x+20,y+h-4),(x+70,y+h-4),(x+60,y+h-16),(x+30,y+h-16)],fill=(90,110,90));d.ellipse([x+60,y+8,x+130,y+26],fill=(60,80,60));d.rectangle([x+128,y+14,x+168,y+20],fill=(60,80,60));d.line([x+40,y+4,x+150,y+4],fill=(40,40,40),width=2);d.rectangle([x+90,y+26,x+100,y+30],fill=(60,80,60))
    elif k=="shop":
        d.rectangle([x,y,x+w,y+h],fill=(240,220,180));d.rectangle([x+10,y+8,x+w-10,y+16],fill=(178,34,34));d.rectangle([x+20,y+16,x+w-20,y+h-4],fill=(255,250,240));d.rectangle([x+30,y+22,x+70,y+30],fill=(30,90,160));d.rectangle([x+110,y+22,x+150,y+30],fill=(34,120,60));d.rectangle([x+40,y+26,x+60,y+32],fill=(120,120,120))
    elif k=="desert":
        d.rectangle([x,y,x+w,y+h],fill=(230,200,140));d.polygon([(x,y+h),(x+80,y+10),(x+160,y+h)],fill=(200,170,110));d.polygon([(x+100,y+h),(x+170,y+16),(x+w,y+h)],fill=(190,160,100));d.ellipse([x+w-40,y+4,x+w-10,y+22],fill=(255,220,120))
    elif k=="truck":
        d.rectangle([x,y,x+w,y+h],fill=(200,210,220));d.rectangle([x+16,y+12,x+110,y+h-10],fill=(178,34,34));d.rectangle([x+110,y+16,x+150,y+h-10],fill=(240,240,240));d.ellipse([x+40,y+h-12,x+58,y+h-2],fill=(30,30,30));d.ellipse([x+120,y+h-12,x+138,y+h-2],fill=(30,30,30));d.rectangle([x+116,y+20,x+138,y+28],fill=(150,190,210))
    elif k=="rocket":
        d.rectangle([x,y,x+w,y+h],fill=(18,28,52));d.polygon([(x+w//2-8,y+2),(x+w//2+8,y+2),(x+w//2+12,y+24),(x+w//2-12,y+24)],fill=(255,255,255));d.ellipse([x+w//2-5,y+8,x+w//2+5,y+16],fill=(150,190,210));d.polygon([(x+w//2-12,y+22),(x+w//2-20,y+32),(x+w//2-8,y+28)],fill=(200,60,60));d.polygon([(x+w//2+12,y+22),(x+w//2+20,y+32),(x+w//2+8,y+28)],fill=(200,60,60));d.polygon([(x+w//2-4,y+24),(x+w//2+4,y+24),(x+w//2,y+34)],fill=(255,180,60))
def main():
    im=Image.new("RGB",(W,H),CREAM);d=ImageDraw.Draw(im)
    d.text((16,8),"THE WORLD ON ONE PAGE",font=SANSB(11),fill=RED);d.text((1024-16-d.textlength("38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS",font=SANSB(11)),8),"38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS",font=SANSB(11),fill=INK)
    d.text((16,26),"Tuesday 24 November 2026",font=SERIF(34),fill=INK);d.line([16,64,1008,64],fill=RED,width=2)
    d.text((16,68),"Riyadh tower hit again  \u00b7  Shanghai party chief probed  \u00b7  Huawei guilty on 10 of 12 counts.",font=SERIF(13),fill=RED)
    bx=16
    for name,n,c in REG:
        w=int(992*n/38);d.rectangle([bx,88,bx+w,104],fill=c);d.text((bx+4,90),f"{name} {n}",font=SANSB(9),fill=(255,255,255));bx+=w
    d.text((16,110),"THE DAY IN UTC",font=SANSB(10),fill=RED)
    for i,(t,s) in enumerate(UTC):
        x=16+i*142; d.rectangle([x,124,x+138,152],fill=(255,255,255),outline=(200,200,190));d.text((x+5,126),t,font=SANSB(10),fill=RED);d.text((x+5,138),s,font=SANS(8),fill=INK)
    d.text((16,158),"THE DAY IN NUMBERS",font=SANSB(10),fill=RED)
    for i,(n,s) in enumerate(NUM):
        x=16+i*124; d.text((x,172),n,font=SERIF(20),fill=RED);d.text((x,194),s,font=SANS(8),fill=INK)
    d.line([16,214,1008,214],fill=(200,190,170),width=1)
    for i,(kick,ch,hl,deck,src,k) in enumerate(HERO):
        x=16+i*336; scene(d,x,222,320,100,k);d.text((x,324),kick,font=SANSB(10),fill=RED);w=chip(d,x,340,ch);d.text((x+w+6,341),src,font=SANS(8),fill=(110,110,110))
        yy=354
        for ln in wrap(d,hl,SERIF(15),320): d.text((x,yy),ln,font=SERIF(15),fill=INK);yy+=18
        yy+=2
        for ln in wrap(d,deck,SANS(10),320): d.text((x,yy),ln,font=SANS(10),fill=INK);yy+=12
    for j,(n,kick,ch,hl,deck,src,k) in enumerate(CARD):
        r=j//5;c=j%5;x=16+c*200;y=434+r*118; d.rectangle([x,y,x+188,y+112],fill=(255,255,255),outline=(200,190,170));scene(d,x+1,y+1,186,34,k);d.text((x+5,y+38),kick,font=SANSB(8),fill=RED);yy=y+50
        for ln in wrap(d,hl,SANSB(10),178)[:2]: d.text((x+5,yy),ln,font=SANSB(10),fill=INK);yy+=12
        for ln in wrap(d,deck,SANS(8),178)[:2]: d.text((x+5,yy),ln,font=SANS(8),fill=(60,60,60));yy+=10
        chip(d,x+5,y+98,ch);d.text((x+5+chip(d,x+5,y+98,ch)+0,y+98),"",font=SANS(8),fill=INK);d.text((x+120,y+99),src,font=SANS(7),fill=(110,110,110))
    d.text((16,672),"WORLD MAP \u00b7 13 STORIES PINNED",font=SANSB(10),fill=RED);d.text((452,672),"MAP KEY",font=SANSB(10),fill=RED);d.text((588,672),"ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES",font=SANSB(10),fill=RED)
    MX,MY,MW,MH=16,690,430,215;d.rectangle([MX,MY,MX+MW,MY+MH],fill=(190,215,228),outline=(120,120,110))
    def px(lon): return MX+(lon+180)/360*MW
    def py(lat): return MY+(90-lat)/180*MH
    for poly in LAND:
        d.polygon([(px(lo),py(la)) for lo,la in poly],fill=(202,192,142),outline=(150,140,110))
    for n,(lon,lat,city) in PINS.items():
        tx,ty=px(lon),py(lat);ox,oy=OFF.get(n,(0,0));cx,cy=tx+ox,ty+oy
        if (ox,oy)!=(0,0): d.line([tx,ty,cx,cy],fill=RED,width=1)
        d.ellipse([cx-8,cy-8,cx+8,cy+8],fill=RED,outline=(255,255,255));d.text((cx-3 if n<10 else cx-6,cy-6),str(n),font=SANSB(8),fill=(255,255,255))
    for n,(lon,lat,city) in PINS.items():
        y=690+(n-1)*16;cx=452;d.ellipse([cx,y,cx+13,y+13],fill=RED);d.text((cx+4 if n<10 else cx+1,y+2),str(n),font=SANSB(8),fill=(255,255,255));d.text((cx+17,y+1),city,font=SANS(9),fill=INK)
    for j,(n,s,ch) in enumerate(ALSO):
        col=j//13;row=j%13;x=588+col*212;y=690+row*16;d.ellipse([x,y+1,x+8,y+9],fill=CHIP[ch]);yy=y
        for ln in wrap(d,s,SANS(7),196)[:2]: d.text((x+11,yy),ln,font=SANS(7),fill=INK);yy+=7
    d.rectangle([16,912,1008,990],fill=(255,240,240),outline=RED)
    d.text((24,918),"DATE CHECK",font=SANSB(10),fill=RED);yy=932
    for ln in wrap(d,"Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.",SANSB(9),960): d.text((24,yy),ln,font=SANSB(9),fill=INK);yy+=11
    for ln in wrap(d,"LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) \u00b7 Huang returns as Nvidia CEO (Mon 23 Nov) \u00b7 EU sanctions package 22 (Mon 23 Nov) \u00b7 COP31 ends with no deal (Sun 22 Nov) \u00b7 Merkury sinks (Sat 22 Nov) \u00b7 El Chapo Isidro arrested (Fri 20 Nov) \u00b7 Cikande fire starts (Sat 21 Nov) \u00b7 Trump hush-money appeal ruling (Mon 23 Nov) \u00b7 ATP Finals (Sun 22 Nov) \u00b7 Las Vegas GP (Sat 21 Nov).",SANS(9),960): d.text((24,yy),ln,font=SANS(9),fill=INK);yy+=11
    for ln in wrap(d,"NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) \u00b7 MPR session to pick VP (11 Dec) \u00b7 Huawei sentencing (Sep 2027) \u00b7 Hasina returns to Bangladesh (16 Dec) \u00b7 COP32 final decision and venue (not set).",SANS(9),960): d.text((24,yy),ln,font=SANS(9),fill=INK);yy+=11
    d.text((16,996),"Sources: Saudi officials \u00b7 CCDI \u00b7 US court \u00b7 Kyiv officials \u00b7 CAS \u00b7 UKMTO \u00b7 NYSE \u00b7 Reuters \u00b7 CMSA \u00b7 wires. Scenes are drawn illustrations, not photographs.",font=SANS(8),fill=(110,110,110))
    d.text((16,1008),"Chips: CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one party's claim. \u00b7 = certainty chip on every ALSO item.",font=SANS(8),fill=(110,110,110))
    out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png");os.makedirs(os.path.dirname(out) or ".",exist_ok=True);im.save(out)
if __name__=="__main__": main()
