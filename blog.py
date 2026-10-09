from pathlib import Path
from html import escape
from urllib.parse import quote
import re,json
root=Path(__file__).parent/'dist';origin='https://creamchargersdubai.com';slug='blog/cream-charger-delivery-dubai/'
def route(l,p=''):return ('/'+l if l!='en' else '')+'/'+p
D={
'en':{
 'title':'Cream Charger Delivery in Dubai: Order via WhatsApp',
 'desc':'We deliver Smartwhip and Cream Deluxe cream chargers in Dubai. Discover how to order via WhatsApp, confirm delivery and pay cash at your door.',
 'label':'DELIVERY GUIDE · 5 OCTOBER 2026','read':'Read the article →','index':'The Dubai Kitchen Journal','lead':'Need cream chargers for your kitchen in Dubai? We arrange delivery of Smartwhip, Cream Deluxe and culinary N2O cylinders through WhatsApp, with cash payment when your order arrives.',
 'sections':[
 ('Cream chargers delivered to your Dubai address','From a café preparing its next dessert service to a catering team planning an order, clear product details make ordering easier. Tell us which cream charger or cylinder you need, how many you would like and where the order should be delivered. We confirm availability and the delivery arrangements before dispatch.'),
 ('Smartwhip, Cream Deluxe and N2O cylinders','Our collection includes Smartwhip Silver, Cream Deluxe cylinders and cream charger tanks. These products are intended for culinary cream whipping and aerated recipes with appropriate equipment. Nitrous oxide (N2O) is also known as laughing gas or lachgas. Before ordering, confirm the exact cylinder size, regulator, fittings and compatibility with your dispenser.'),
 ('How to order on WhatsApp','Open your preferred product page and select Order via WhatsApp. The prepared message includes the product name, description and quantity. Add your full delivery address and any building access instructions, then send the message. We will confirm the product variant, stock, delivery window, any delivery charge and the final total. Your order is arranged directly in the conversation.'),
 ('Pay cash on delivery','You do not need to pay online. Once your order and delivery details are agreed, you can pay in cash when the order is delivered to your address. Ask for the total before dispatch so you know the amount to prepare.'),
 ('Delivery enquiries across Dubai','We accept delivery enquiries for Dubai Marina, Downtown Dubai, Business Bay, JBR, Jumeirah, Palm Jumeirah, Al Barsha and Deira. Send your precise address so we can confirm the available service for your location. Delivery timing and charges are agreed for each order; contact us before planning around a specific arrival time.'),
 ('Ordering for a café, restaurant or catering business?','For larger or repeat orders, send a product list and quantities together with your delivery location. This helps us discuss current pricing and the right cylinder format for your kitchen. Use and store all cylinders according to the manufacturer’s instructions and only for their intended culinary purpose.')],
 'products':'Explore the products','area':'Delivery information by area','cta':'Arrange your Dubai delivery','button':'Order via WhatsApp ↗','message':'Hello, I read your Dubai delivery blog and would like to order culinary cream chargers. Please confirm products, availability, delivery timing, fees and the total. I will pay cash on delivery.'},
'nl':{
 'title':'Slagroompatronen bezorgen in Dubai: bestel via WhatsApp',
 'desc':'Wij bezorgen Smartwhip en Cream Deluxe in Dubai. Lees hoe je via WhatsApp bestelt, de bezorging afspreekt en contant betaalt aan de deur.',
 'label':'BEZORGGIDS · 5 OKTOBER 2026','read':'Lees het artikel →','index':'Nieuws voor je keuken in Dubai','lead':'Slagroompatronen nodig voor je keuken in Dubai? Wij regelen bezorging van Smartwhip, Cream Deluxe en culinaire N2O-cilinders via WhatsApp. Je betaalt contant wanneer je bestelling aankomt.',
 'sections':[
 ('Slagroompatronen bezorgd op je adres in Dubai','Van een café dat de volgende dessertservice voorbereidt tot een cateringteam dat voorraad bestelt: duidelijke productgegevens maken bestellen eenvoudiger. Vertel welke slagroompatronen of cilinder je nodig hebt, hoeveel je wilt en waar we de bestelling moeten bezorgen. We bevestigen beschikbaarheid en bezorgafspraken vóór verzending.'),
 ('Smartwhip, Cream Deluxe en N2O-cilinders','Ons assortiment bevat Smartwhip Silver, Cream Deluxe-cilinders en lachgastanks voor slagroom. Deze producten zijn bedoeld voor culinaire slagroom en luchtige recepten met geschikte apparatuur. Lachgas (N2O) heet in het Engels nitrous oxide of laughing gas. Controleer vóór je bestelling het exacte formaat, de regelaar, aansluitingen en compatibiliteit met je slagroomspuit.'),
 ('Zo bestel je via WhatsApp','Open de gewenste productpagina en kies Bestel via WhatsApp. Het voorbereide bericht bevat de productnaam, omschrijving en het aantal. Voeg je volledige bezorgadres en eventuele toegangsinstructies toe en verstuur het bericht. We bevestigen de variant, voorraad, bezorgtijd, eventuele bezorgkosten en het totaalbedrag. Je regelt de bestelling rechtstreeks in het gesprek.'),
 ('Contant betalen bij bezorging','Je hoeft niet online te betalen. Nadat de bestelling en bezorggegevens zijn afgesproken, betaal je contant wanneer de bestelling op je adres wordt bezorgd. Vraag het totaalbedrag vóór verzending, zodat je weet welk bedrag je moet klaarleggen.'),
 ('Bezorgaanvragen in Dubai','Je kunt bezorging aanvragen voor Dubai Marina, Downtown Dubai, Business Bay, JBR, Jumeirah, Palm Jumeirah, Al Barsha en Deira. Stuur je precieze adres, zodat we de mogelijkheden voor jouw locatie bevestigen. Bezorgtijd en kosten spreken we per bestelling af. Neem contact op voordat je rekent op een specifieke aankomsttijd.'),
 ('Bestellen voor een café, restaurant of cateringbedrijf?','Stuur voor grotere of terugkerende bestellingen een productlijst, aantallen en je bezorglocatie. Zo bespreken we de actuele prijzen en het passende cilinderformaat voor je keuken. Gebruik en bewaar alle cilinders volgens de instructies van de fabrikant en uitsluitend voor het bedoelde culinaire doel.')],
 'products':'Bekijk de producten','area':'Bezorginformatie per gebied','cta':'Regel je bezorging in Dubai','button':'Bestel via WhatsApp ↗','message':'Hallo, ik heb jullie blog over bezorging in Dubai gelezen en wil culinaire slagroompatronen bestellen. Graag producten, voorraad, bezorgtijd, kosten en totaal bevestigen. Ik betaal contant bij bezorging.'},
'fr':{
 'title':'Livraison de cartouches de crème à Dubaï : commandez sur WhatsApp',
 'desc':'Nous livrons Smartwhip et Cream Deluxe à Dubaï. Découvrez comment commander sur WhatsApp, organiser la livraison et payer en espèces à votre porte.',
 'label':'GUIDE DE LIVRAISON · 5 OCTOBRE 2026','read':'Lire l’article →','index':'Le journal des cuisines de Dubaï','lead':'Besoin de cartouches de crème pour votre cuisine à Dubaï ? Nous organisons la livraison de Smartwhip, Cream Deluxe et de cylindres N2O culinaires sur WhatsApp, avec paiement en espèces à la réception.',
 'sections':[
 ('Des cartouches livrées à votre adresse à Dubaï','Qu’il s’agisse d’un café préparant son prochain service de desserts ou d’un traiteur organisant ses achats, des informations précises facilitent la commande. Indiquez les cartouches ou le cylindre souhaités, la quantité et l’adresse. Nous confirmons la disponibilité et les modalités de livraison avant l’expédition.'),
 ('Smartwhip, Cream Deluxe et cylindres N2O','Notre collection comprend Smartwhip Silver, les cylindres Cream Deluxe et les réservoirs N2O pour crème. Ces produits sont destinés à la crème fouettée et aux recettes aérées avec un équipement adapté. Le protoxyde d’azote (N2O) est aussi appelé gaz hilarant ou lachgas. Avant de commander, confirmez la taille, le régulateur, les raccords et la compatibilité avec votre siphon.'),
 ('Comment commander sur WhatsApp','Ouvrez la fiche du produit souhaité et choisissez Commander via WhatsApp. Le message préparé contient le nom, la description et la quantité du produit. Ajoutez votre adresse complète et les éventuelles consignes d’accès, puis envoyez le message. Nous confirmons le modèle, le stock, le créneau, les éventuels frais et le montant total. La commande est organisée directement dans la conversation.'),
 ('Payez en espèces à la livraison','Aucun paiement en ligne n’est nécessaire. Une fois la commande et les modalités convenues, vous pouvez payer en espèces à la réception à votre adresse. Demandez le montant total avant l’expédition pour préparer la somme.'),
 ('Demandes de livraison dans Dubaï','Nous acceptons les demandes pour Dubai Marina, Downtown Dubai, Business Bay, JBR, Jumeirah, Palm Jumeirah, Al Barsha et Deira. Envoyez l’adresse précise pour confirmer le service disponible à votre emplacement. Les délais et frais sont convenus pour chaque commande ; contactez-nous avant de prévoir une heure d’arrivée spécifique.'),
 ('Une commande pour un café, restaurant ou traiteur ?','Pour les commandes importantes ou régulières, envoyez les produits, les quantités et le lieu de livraison. Nous pourrons discuter des prix actuels et du format adapté à votre cuisine. Utilisez et stockez les cylindres conformément aux instructions du fabricant et uniquement pour leur usage culinaire prévu.')],
 'products':'Découvrir les produits','area':'Informations par quartier','cta':'Organisez votre livraison à Dubaï','button':'Commander via WhatsApp ↗','message':'Bonjour, j’ai lu votre article sur la livraison à Dubaï et souhaite commander des cartouches de crème culinaires. Merci de confirmer les produits, le stock, le délai, les frais et le total. Je paierai en espèces à la livraison.'}}
for l,v in D.items():
 basefile=root/route(l).lstrip('/')/'index.html';base=basefile.read_text();prefix=base.split('<main>')[0];footer=base[base.index('<footer'):]
 def header(path,title,desc,article=False):
  s=re.sub(r'<title>.*?</title>','<title>'+escape(title)+'</title>',prefix)
  for prop,value in [('name="description"',desc),('property="og:title"',title),('property="og:description"',desc)]:s=re.sub('(<meta '+prop+' content=")[^"]*',lambda m:m[1]+escape(value,quote=True),s)
  s=re.sub(r'<link rel="(?:alternate|canonical)"[^>]*>','',s)
  tags=''.join(f'<link rel="alternate" hreflang="{lang}" href="{origin}{route(lang,path)}">' for lang in D)+f'<link rel="canonical" href="{origin}{route(l,path)}">'
  if article:
   data={'@context':'https://schema.org','@type':'BlogPosting','headline':title,'description':desc,'datePublished':'2026-10-05T10:50:20+04:00','dateModified':'2026-10-05T10:50:20+04:00','inLanguage':l,'author':{'@type':'Organization','name':'Smartwhip Dubai'},'image':origin+'/assets/hero.webp','mainEntityOfPage':origin+route(l,path)}
   tags+='<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script>'
  s=s.replace('</head>',tags+'</head>')
  for lang in D:s=s.replace(f'href="{route(lang)}" lang="{lang}"',f'href="{route(lang,path)}" lang="{lang}"')
  return s
 wa='https://wa.me/31684227916?text='+quote(v['message'])
 body=f'<main><article class="article blog-article"><div class="eyebrow">{v["label"]}</div><h1>{v["title"]}</h1><p class="blog-lead">{v["lead"]}</p><img class="poster blog-image" src="/assets/hero.webp" alt="Smartwhip & Cream Deluxe · Dubai">'
 for h,p in v['sections']:body+=f'<h2>{h}</h2><p>{p}</p>'
 body+=f'<h2>{v["products"]}</h2><div class="area-links">'+''.join(f'<a href="{route(l,path+"/")}">{name} →</a>' for name,path in [('Smartwhip Silver','smartwhip-silver'),('Cream Deluxe','cream-deluxe-cylinder'),('N2O Tanks','cream-charger-tanks')])+'</div>'
 body+=f'<h2>{v["area"]}</h2><div class="area-links">'+''.join(f'<a href="{route(l,"cream-chargers-"+path+"/")}">{name} →</a>' for name,path in [('Dubai Marina','dubai-marina'),('Downtown Dubai','downtown-dubai'),('Business Bay','business-bay')])+'</div>'
 body+=f'<h2>{v["cta"]}</h2><a class="btn" href="{wa}">{v["button"]}</a></article></main>'
 dest=root/route(l,slug).lstrip('/');dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(header(slug,v['title'],v['desc'],True)+body+footer)
 card=f'<article class="blog-card"><img src="/assets/hero.webp" alt="Smartwhip & Cream Deluxe · Dubai" loading="lazy"><div><span class="eyebrow">{v["label"]}</span><h2>{v["title"]}</h2><p>{v["lead"]}</p><a class="btn outline" href="{route(l,slug)}">{v["read"]}</a></div></article>'
 listing=root/route(l,'blog/').lstrip('/');listing.mkdir(parents=True,exist_ok=True);(listing/'index.html').write_text(header('blog/',v['index']+' | Smartwhip Dubai',v['desc'])+f'<main class="section"><span class="eyebrow">BLOG</span><h1>{v["index"]}</h1>{card}</main>'+footer)
 base=re.sub(r'<!-- BLOG START -->.*?<!-- BLOG END -->','',base,flags=re.S);base=base.replace('</main>','<!-- BLOG START --><section class="section"><span class="eyebrow">BLOG</span>'+card+'</section><!-- BLOG END --></main>');basefile.write_text(base)
# Add a Blog link to the header on all pages, preserving every existing route.
for f in root.rglob('index.html'):
 s=f.read_text();parts=f.relative_to(root).parts;l=parts[0] if parts[0] in ['nl','fr'] else 'en';u=route(l,'blog/')
 if f'href="{u}">BLOG</a>' not in s:s=s.replace('</nav>',f'<a href="{u}">BLOG</a></nav>')
 f.write_text(s)
css=root/'style.css';extra='\n.blog-article{padding-top:65px}.blog-article h1{font-size:clamp(36px,4.5vw,56px);letter-spacing:-1.6px;line-height:1.12}.blog-lead{font-size:20px;color:#d2deec}.blog-image{height:340px;object-fit:cover;margin:24px 0}.blog-card{display:grid;grid-template-columns:1fr 1.2fr;gap:40px;align-items:center}.blog-card img{width:100%;height:300px;object-fit:cover;border-radius:8px}.blog-card h2{font-size:32px}@media(max-width:800px){.blog-card{grid-template-columns:1fr;gap:22px}.blog-article{padding-top:40px}.blog-lead{font-size:17px}.blog-image{height:240px}}'
s=css.read_text()
if extra not in s:css.write_text(s+extra)
urls=[origin+'/'+('' if str(p.relative_to(root).parent)=='.' else str(p.relative_to(root).parent)+'/') for p in root.rglob('index.html')]
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in sorted(urls))+'</urlset>')
print('Created first Dubai delivery blog and blog index in EN/NL/FR, homepage previews, header links and sitemap.')
