from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from PIL import Image

BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'output/pdf/Web3-Carnival-Design-Presentation.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
W,H=1280,800
C=canvas.Canvas(str(OUT),pagesize=(W,H))
C.setTitle('Web3 Carnival | A complete responsive event experience')
C.setAuthor('Web3 Carnival redesign concept')
INK='#151513'; PAPER='#EFEEE6'; SOFT='#B6B8AD'; ORANGE='#FF653D'
page_no=0

def txt(text,x,y,size=16,color=PAPER,font='Helvetica'):
 C.setFillColor(HexColor(color));C.setFont(font,size);C.drawString(x,y,text)
def para(text,x,y,width,size=17,color=SOFT,leading=None):
 st=ParagraphStyle('body',fontName='Helvetica',fontSize=size,leading=leading or size*1.45,textColor=HexColor(color))
 p=Paragraph(text,st);_,h=p.wrap(width,H);p.drawOn(C,x,y-h);return y-h
def start(title,subtitle):
 global page_no
 page_no+=1;C.setFillColor(HexColor(INK));C.rect(0,0,W,H,fill=1,stroke=0)
 txt('WEB3 CARNIVAL',40,760,12,ORANGE,'Helvetica-Bold')
 txt('RESPONSIVE WEBSITE REDESIGN',860,760,10,SOFT)
 txt(title,40,706,36,PAPER,'Helvetica-Bold');para(subtitle,42,681,1170,15)
 C.setStrokeColor(HexColor('#3C3D36'));C.line(40,48,1240,48)
 txt('INDEPENDENT DESIGN CONCEPT  /  CONTENT BASELINE: WEB3CARNIVAL.WORLD',40,27,9,SOFT)
 txt(f'{page_no:02}',1210,27,10,ORANGE,'Helvetica-Bold')
def shot(name,x,y,w,h,folder='lab'):
 p=BASE/folder/name
 with Image.open(p) as im:iw,ih=im.size
 scale=min(w/iw,h/ih);dw,dh=iw*scale,ih*scale
 C.drawImage(ImageReader(str(p)),x+(w-dw)/2,y+(h-dh)/2,dw,dh,mask='auto')
def note(title,body,x,y,w=275):
 txt(title,x,y,17,ORANGE,'Helvetica-Bold');return para(body,x,y-17,w,15)-27
def end():C.showPage()

start('The future happens IRL.','An interactive festival programme for a global Web3 community. Designed and built with Scroll Craft.')
shot('desktop-hero.png',40,85,920,555)
y=605
y=note('THE IDEA','Make the people behind Web3 the reason to come. Documentary imagery, bold type and a physical passport give the event a human identity.',985,y,250)
y=note('THE EXPERIENCE','Discover the event, collect your interests, meet past speakers and leave with a personal Carnival Passport.',985,y,250)
note('THE DELIVERABLE','A working responsive website plus this presentation of the complete visitor journey.',985,y,250)
end()

start('A journey with somewhere to go.','The structure answers the visitor’s questions, then gives them a useful next step.')
stages=[('ARRIVE','What is it?','Festival masthead, original brand marks and immediate invitation.'),('UNDERSTAND','What is happening next?','Next-edition status, organiser contact and source-attributed community figures.'),('DISCOVER','What is here for me?','Seven original event tracks. Select interests and build a personal passport.'),('TRUST','Who is in the room?','Searchable historical speakers, profiles, event editions and ecosystem partners.'),('BELONG','Where do I fit?','Builder, founder, investor and explorer routes; speaker, media and volunteer enquiries.'),('ACT','What do I do next?','A three-step registration preview, a downloadable plan and an organiser enquiry.')]
for i,(tag,q,body) in enumerate(stages):
 x=40+(i%3)*410;y=595-(i//3)*245
 C.setStrokeColor(HexColor('#3C3D36'));C.line(x,y+15,x+365,y+15)
 txt(tag,x,y-16,12,ORANGE,'Helvetica-Bold');txt(q,x,y-55,22,PAPER,'Helvetica-Bold');para(body,x,y-78,350,17)
end()

start('The next edition, without the guesswork.','Historical dates stay in the archive. A future event is never presented as confirmed when it is not.')
shot('desktop-experience.png',40,88,880,550)
y=602;y=note('CLEAR EVENT INFORMATION','The next chapter is explicitly marked to be announced, with no fabricated date, venue, ticket price or capacity.',950,y)
y=note('CREDIBLE SOCIAL PROOF','The community figures come from the current official website and link to that source. They are not a forecast for the next event.',950,y)
note('A DIRECT NEXT STEP','The visitor can begin a passport immediately, or use the real organiser contact paths.',950,y)
end()

start('Your interests become your invitation.','The signature interaction: track selections visibly stamp a personal Carnival Passport.')
shot('desktop-passport.png',40,82,895,565)
y=603;y=note('SEVEN REAL TRACKS','Blockchain, DeFi, DAOs, GameFi, ZK/security, enterprise blockchain and NFTs retain the original event’s thematic breadth.',960,y)
y=note('STATE THAT MATTERS','Selections stay in the browser and carry into the registration preview and downloadable plan. Clear them with one control.',960,y)
note('BUILT FOR ACCESS','The same choices work by pointer, touch or keyboard. Reduced motion keeps the complete meaning and available controls.',960,y)
end()

start('Real people. Real reasons to connect.','Historical speaker profiles preserve names, portraits and source-listed affiliations.')
shot('desktop-speakers.png',40,78,905,570)
y=601;y=note('EXPLORE THE ROSTER','Search names, organisations or topics. Expand the directory, open a profile and follow its original professional link.',970,y,260)
y=note('A HUMAN VISUAL LANGUAGE','Large portraits replace a wall of small logos. Colour returns on hover, while the information remains visible without hovering.',970,y,260)
note('HONEST CONTEXT','Every profile is labelled as historical. Past affiliations are not presented as current employment or a future speaker commitment.',970,y,260)
end()

start('A growing story, across borders.','The archive turns a list of old links into a useful event discovery experience.')
shot('desktop-editions.png',40,80,895,565)
y=600;y=note('FILTER BY PLACE','India, Singapore and Dubai filters immediately update the visible editions. Native horizontal scrolling works on touch and keyboard.',960,y)
y=note('ORIGINAL EVENT ARTWORK','Bitcoin Pizza Day, Founders & Funders, DeGen Summit and World Web3 Consortium use the source website’s own artwork.',960,y)
note('CLEAR HISTORICAL STATUS','Dates are shown on every edition, with links to original listings. No old event is advertised as upcoming.',960,y)
end()

start('From the crowd to your community.','Photography provides the emotional context; useful routes help visitors find their place.')
shot('community.png',40,333,730,307,'lab/presentation');shot('partners.png',40,80,730,240,'lab/presentation')
y=600;y=note('MORE THAN THE STAGE','The natural-flow photographic reveal introduces the social side of the experience, with imagery reused from the brand website.',820,y,405)
y=note('AN ECOSYSTEM, NOT A LOGO WALL','Past supporter names and the organiser mark provide concise proof. The partnership CTA leads to the organiser’s booking page.',820,y,405)
note('BRAND + NEW DIRECTION','The existing event mark, source content and Threeway Studio relationship remain. Orange is a proposed redesign accent, replacing the original purple-led treatment.',820,y,405)
end()

start('Everyone has a way in.','Involvement is designed around people’s intentions, not a long undifferentiated application list.')
shot('involved.png',40,248,800,390,'lab/presentation');shot('faq.png',40,75,800,170,'lab/presentation')
y=600;y=note('CHOOSE YOUR PERSPECTIVE','Builder, founder, investor and explorer tabs change the supporting content and recommended tracks.',885,y,335)
y=note('CARRY THE ROUTE FORWARD','One action adds the suggested tracks to the passport. Your earlier interests remain selected.',885,y,335)
y=note('REAL CONTACT PATHS','Speaker, community, volunteer and media links prepare an email enquiry for the visitor to review and send.',885,y,335)
note('QUESTIONS ANSWERED','FAQs explain experience level, next-edition status, passport limitations and how to get involved.',885,y,335)
end()

start('A registration flow that feels like an invitation.','The working prototype moves from intent to details to a personalised outcome. It never claims a booking was made.')
for i,(name,title,body) in enumerate([('step-one.png','01  FIND YOUR STARTING POINT','Choose a role. Selected interests carry forward from the website.'),('step-two.png','02  MAKE IT PERSONAL','Name, email and a clear prototype acknowledgement. Required-field and email validation.'),('step-three.png','03  TAKE YOUR PASSPORT','Download a personal plan or prepare an organiser enquiry in your own mail app.')]):
 x=40+i*415;shot(name,x,280,390,345,'lab/presentation');txt(title,x,245,13,ORANGE,'Helvetica-Bold');para(body,x,226,365,16)
para('Privacy by design: name and email are not stored or transmitted. Closing the preview clears them. Only interests and theme are browser preferences. No wallet connection, payment, booking or blockchain transaction occurs.',40,123,1190,15)
end()

start('Designed for the screen in your hand.','Separate mobile composition, touch-sized track rows, a native event rail and a compact registration flow.')
for i,(name,label) in enumerate([('mobile-home.png','ARRIVE'),('mobile-passport.png','PERSONALISE'),('mobile-speakers.png','DISCOVER'),('mobile-form.png','TAKE ACTION')]):
 x=55+i*310;shot(name,x,95,230,505,'lab/presentation');txt(label,x,620,11,ORANGE,'Helvetica-Bold')
end()

start('Motion with a purpose.','Four distinct device families support the journey. Scrolling remains native throughout.')
shot('desktop-light.png',40,80,800,557)
y=602;y=note('DEPTH, NOT DISTRACTION','Independent photo parallax and restrained pointer movement establish the opening. Counters, a photographic reveal and staggered portraits vary the pacing.',885,y,335)
y=note('THE PEAK','Curiosity becomes agency when interests accumulate as passport stamps. The tracks have the largest content span; the ending resolves with a stable invitation.',885,y,335)
y=note('TWO COHERENT THEMES','Light/dark switching retains the same hierarchy and orange accent. Theme preference is local to the browser.',885,y,335)
note('REDUCED MOTION','Motion preferences remove positional animation while preserving text, images, choices, navigation and registration.',885,y,335)
end()

start('Complete journey. Clear handoff.','A functional design prototype, checked across desktop, tablet and phone layouts.')
left=[('COVERAGE','Homepage; next-event information; all seven tracks; past speakers; editions; attendee routes; partners; registration; contact; social footer.'),('INTERACTIONS','Track selection and persistence, speaker search and profiles, event filtering and rail navigation, keyboard role tabs, registration validation and passport download.'),('VISUAL VERIFICATION','167 Scroll Craft samples across desktop, mobile and reduced motion. Additional 360px, 390px, 768px and 1440px layout checks, interaction screenshots and image loading checks.')]
y=605
for title,body in left:y=note(title,body,40,y,550)
y=605
for title,body in [('WHAT IS READY','The complete static website runs locally and can be hosted from its dist folder. This PDF demonstrates the desktop/mobile journey, including the registration flow.'),('WHAT STILL NEEDS THE ORGANISER','Confirmed future event details; production registration, ticketing and email delivery; approval for public use of brand assets. The current build is a clearly labelled independent concept.'),('LIMITS OF TESTING','Browser-emulated phone views were tested, not physical iPhone/Android hardware. No live registration was submitted and no public deployment is claimed.')]:y=note(title,body,685,y,550)
txt('CONTENT & IMAGE SOURCE',40,139,11,ORANGE,'Helvetica-Bold');para('<link href="https://www.web3carnival.world/" color="#B6B8AD">https://www.web3carnival.world/</link> | User-supplied two-page challenge brief | Archivo by Omnibus-Type',40,122,1160,14)
end();C.save();print(OUT)
