from pathlib import Path
from html import escape,unescape
import re,json
root=Path(__file__).parent/'dist';origin='https://creamchargersdubai.com'
D={
'en':dict(home=('Cream Chargers Dubai | Smartwhip & Cream Deluxe','Cream Chargers Dubai – Smartwhip & Cream Deluxe','Cream chargers delivered across Dubai. Smartwhip and Cream Deluxe, 24/7 WhatsApp contact and cash on delivery. Cream Deluxe: AED 600 or 3 for AED 1,500.'),products=['Smartwhip Silver','Cream Deluxe Cylinder','Cream Charger Tanks'],suffix='Dubai',delivery='Fast delivery across Dubai – available 24/7',faq='Cream charger ordering and delivery FAQs',ready='Order cream chargers via WhatsApp',blog='Cream Charger Blog Dubai | Delivery & Product Guides',blogdesc='Read our Dubai cream charger guides: Smartwhip, Cream Deluxe, WhatsApp ordering, delivery and the 3-cylinder offer.',privacy='How we handle contact and delivery information for WhatsApp cream charger orders in Dubai.',offer='Cream Deluxe: AED 600 each or 3 for AED 1,500. Contact us 24/7 on WhatsApp for fast Dubai delivery. Stock, timing, delivery fees and final total are confirmed before dispatch.',areahead='Delivery details for {area}',areabase='For delivery to {area}, send the product, quantity, exact address, building or villa name and a map pin. Add access instructions and a contact number so we can arrange the handover. We are available 24/7; confirm the delivery window and any delivery charge before dispatch.',guide='Dubai delivery and Cream Deluxe offers'),
'nl':dict(home=('Slagroompatronen Dubai | Smartwhip & Cream Deluxe','Slagroompatronen Dubai – Smartwhip & Cream Deluxe','Slagroompatronen in heel Dubai. Smartwhip en Cream Deluxe, 24/7 bereikbaar via WhatsApp en contant betalen. Cream Deluxe: AED 600 of 3 voor AED 1.500.'),products=['Smartwhip Silver','Cream Deluxe-cilinder','N2O-slagroomcilinders'],suffix='in Dubai',delivery='Snelle bezorging in heel Dubai – 24/7 bereikbaar',faq='Veelgestelde vragen over slagroompatronen en bezorging',ready='Bestel slagroompatronen via WhatsApp',blog='Blog over slagroompatronen Dubai | Bezorging en producten',blogdesc='Lees over Smartwhip, Cream Deluxe, bestellen via WhatsApp, bezorging in Dubai en de aanbieding van 3 cilinders.',privacy='Lees hoe wij contact- en bezorggegevens verwerken bij WhatsApp-bestellingen van slagroompatronen in Dubai.',offer='Cream Deluxe: AED 600 per stuk of 3 voor AED 1.500. Bereik ons 24/7 via WhatsApp voor snelle bezorging in Dubai. Voorraad, bezorgtijd, bezorgkosten en totaal worden vóór vertrek bevestigd.',areahead='Bezorggegevens voor {area}',areabase='Voor bezorging in {area} stuur je het product, aantal, exacte adres, gebouw- of villanaam en een locatiepin. Voeg toegangsinstructies en een telefoonnummer toe om de overdracht af te spreken. Wij zijn 24/7 bereikbaar; bevestig vóór vertrek de bezorgtijd en eventuele bezorgkosten.',guide='Bezorging in Dubai en Cream Deluxe-aanbiedingen'),
'fr':dict(home=('Cartouches de crème Dubaï | Smartwhip & Cream Deluxe','Cartouches de crème à Dubaï – Smartwhip & Cream Deluxe','Cartouches de crème dans tout Dubaï. Smartwhip et Cream Deluxe, contact WhatsApp 24 h/24 et paiement à la livraison. Cream Deluxe : 600 AED ou 3 pour 1 500 AED.'),products=['Smartwhip Silver','Cylindre Cream Deluxe','Réservoirs N2O pour crème'],suffix='à Dubaï',delivery='Livraison rapide dans tout Dubaï – disponible 24 h/24',faq='Questions sur les cartouches et la livraison',ready='Commander des cartouches sur WhatsApp',blog='Blog cartouches de crème Dubaï | Livraison et produits',blogdesc='Découvrez Smartwhip, Cream Deluxe, les commandes WhatsApp, la livraison à Dubaï et l’offre de 3 cylindres.',privacy='Découvrez le traitement de vos coordonnées et informations de livraison lors des commandes WhatsApp de cartouches de crème à Dubaï.',offer='Cream Deluxe : 600 AED par cylindre ou 3 pour 1 500 AED. Contactez-nous sur WhatsApp 24 h/24 pour une livraison rapide à Dubaï. Stock, délai, frais et total sont confirmés avant le départ.',areahead='Informations de livraison à {area}',areabase='Pour une livraison à {area}, envoyez le produit, la quantité, l’adresse exacte, le nom du bâtiment ou de la villa et un point de localisation. Ajoutez les consignes d’accès et un numéro de contact pour organiser la remise. Disponibles 24 h/24, nous confirmons le créneau et les éventuels frais avant le départ.',guide='Livraison à Dubaï et offres Cream Deluxe')}
slugs=['smartwhip-silver','cream-deluxe-cylinder','cream-charger-tanks']
area_notes={
'dubai-marina':['For an apartment delivery, include the tower name, apartment number and reception instructions.','Vermeld voor een appartement de torennaam, het appartementnummer en instructies voor de receptie.','Pour un appartement, indiquez la tour, le numéro d’appartement et les consignes de réception.'],
'downtown-dubai':['For a hotel or restaurant order, identify the receiving contact and whether delivery should go to reception or another agreed entrance.','Geef bij een hotel of restaurant de contactpersoon en de afgesproken ingang of receptie door.','Pour un hôtel ou restaurant, précisez le contact et l’entrée ou la réception convenue.'],
'business-bay':['For a business delivery, include the company name, office or kitchen unit and the person who will receive the order.','Vermeld voor een zakelijke levering de bedrijfsnaam, kantoor- of keukeneenheid en ontvanger.','Pour une entreprise, indiquez le nom, le bureau ou local de cuisine et le destinataire.'],
'jbr':['Send the building name as well as the location pin, and confirm where you would like to receive your cylinders.','Stuur naast de locatiepin de gebouwnaam en spreek af waar je de cilinders ontvangt.','Envoyez le nom du bâtiment et le point de localisation, puis confirmez le lieu de remise.'],
'jumeirah':['For a villa order, include the villa number, street and any gate instructions rather than only the neighbourhood name.','Vermeld bij een villa het villanummer, de straat en toegangsinstructies, naast de wijknaam.','Pour une villa, indiquez son numéro, la rue et les consignes d’accès en plus du quartier.'],
'palm-jumeirah':['Specify the property name and the exact receiving point. Include any access instructions supplied by your building or venue.','Vermeld de naam van de locatie en de exacte ontvangplek, met toegangsinstructies van het gebouw of de locatie.','Précisez le nom de la propriété et le point de remise exact, avec les consignes d’accès du lieu.'],
'al-barsha':['Include the full address and location pin so your delivery enquiry identifies the intended building or villa clearly.','Stuur het volledige adres en een locatiepin zodat duidelijk is bij welk gebouw of welke villa je bestelling moet aankomen.','Ajoutez l’adresse complète et un point de localisation pour identifier clairement le bâtiment ou la villa.'],
'deira':['For shop or kitchen deliveries, send the shop name, unit number and receiving contact along with your product list.','Stuur voor een winkel of keuken de winkelnaam, het nummer en de contactpersoon mee met je productlijst.','Pour un magasin ou une cuisine, envoyez le nom, le numéro du local et le contact avec la liste des produits.']}
def plain(s):return unescape(re.sub('<[^>]+>',' ',s)).strip()
def meta(s,key,val):return re.sub('(<meta '+key+' content=")[^"]*',lambda m:m[1]+escape(val,quote=True),s)
def heading(s,old,new):return re.sub(r'<h2>'+re.escape(old)+r'</h2>','<h2>'+escape(new)+'</h2>',s)
for p in root.rglob('index.html'):
 rel=p.relative_to(root).parent.as_posix();parts=[] if rel=='.' else rel.split('/');lang=parts.pop(0) if parts and parts[0] in ['nl','fr'] else 'en';path='/'.join(parts);v=D[lang];s=p.read_text();title=plain(re.search('<title>(.*?)</title>',s)[1]);desc=unescape(re.search('<meta name="description" content="([^"]*)',s)[1]);schemas=[]
 url=origin+'/'+('' if rel=='.' else rel+'/')
 if not path:
  title,h1,desc=v['home'];s=re.sub('<h1[^>]*>.*?</h1>','<h1>'+escape(h1)+'</h1>',s)
  for old in ['WhatsApp. Delivery.<br><span class="gold">Cash at your door.</span>','WhatsApp. Bezorging.<br><span class="gold">Contant aan de deur.</span>','WhatsApp. Livraison.<br><span class="gold">Espèces à votre porte.</span>']:s=heading(s,old,v['delivery'])
  for old in ['Your questions, answered.','Antwoorden op je vragen.','Les réponses à vos questions.']:s=heading(s,old,v['faq'])
  for old in ['Ready to order?','Klaar om te bestellen?','Prêt à commander ?']:s=heading(s,old,v['ready'])
  if '<!-- SEO OFFER -->' not in s:s=s.replace('</main>','<!-- SEO OFFER --><section class="section"><h2>'+escape(v['delivery'])+'</h2><p>'+escape(v['offer'])+'</p></section></main>')
 if path in slugs:
  idx=slugs.index(path);name=v['products'][idx];h1=name+' '+v['suffix'];title=h1+' | Smartwhip Dubai'
  desc={'en':f'{name} for culinary kitchens in Dubai. Order via WhatsApp, contact us 24/7 and pay cash on delivery. Confirm equipment compatibility before ordering.','nl':f'{name} voor culinaire keukens in Dubai. Bestel via WhatsApp, 24/7 bereikbaar en contant betalen bij bezorging. Controleer passende apparatuur.','fr':f'{name} pour les cuisines à Dubaï. Commandez sur WhatsApp, contact 24 h/24 et espèces à la livraison. Vérifiez la compatibilité du matériel.'}[lang]
  s=re.sub('<h1[^>]*>.*?</h1>','<h1>'+escape(h1)+'</h1>',s)
  for label in ['Product Description','Productomschrijving','Description du produit']:s=s.replace('<h2>'+label+'</h2>','')
  if '<!-- SEO OFFER -->' not in s:s=s.replace('</article>','<!-- SEO OFFER --><h2>'+escape(v['delivery'])+'</h2><p>'+escape(v['offer'])+'</p></article>')
  prod={'@context':'https://schema.org','@type':'Product','@id':url+'#product','name':name,'url':url,'image':origin+'/assets/'+['smartwhip','deluxe','tank'][idx]+'.webp','description':desc,'brand':{'@type':'Brand','name':'Cream Deluxe' if idx==1 else 'Smartwhip' if idx==0 else 'Cream Charger Tanks'}}
  if idx==2:prod.pop('brand')
  if idx==1:prod['offers']={'@type':'Offer','price':'600','priceCurrency':'AED','url':url}
  schemas.append(prod)
 if path=='blog':title=v['blog'];desc=v['blogdesc']
 if path=='privacy':desc=v['privacy']
 if path.startswith('cream-chargers-'):
  area_slug=path.removeprefix('cream-chargers-');area=plain(re.search('<h1[^>]*>.*?<em>(.*?)</em>',s)[1])
  h1={'en':f'Cream Charger Delivery in {area}','nl':f'Slagroompatronen bezorgen in {area}','fr':f'Livraison de cartouches de crème à {area}'}[lang];s=re.sub('<h1[^>]*>.*?</h1>','<h1>'+escape(h1)+'</h1>',s)
  if area_slug in area_notes and '<!-- SEO LOCAL -->' not in s:
   para=v['areabase'].format(area=area)+' '+area_notes[area_slug][['en','nl','fr'].index(lang)]
   prefix='' if lang=='en' else '/'+lang
   block='<!-- SEO LOCAL --><section class="section"><h2>'+escape(v['areahead'].format(area=area))+'</h2><p>'+escape(para)+'</p><h2>'+escape(v['guide'])+'</h2><p>'+escape(v['offer'])+'</p><a class="text-link" href="'+prefix+'/blog/dubai-delivery-24-7-cream-deluxe-offer/">'+escape(v['guide'])+' →</a></section>'
   s=s.replace('</main>',block+'</main>')
 s=re.sub('<title>.*?</title>','<title>'+escape(title)+'</title>',s);s=meta(s,'name="description"',desc);s=meta(s,'property="og:title"',title);s=meta(s,'property="og:description"',desc)
 s=re.sub(r'<br\s*/?>', ' <br>',s)
 if not path:schemas.append({'@context':'https://schema.org','@type':'Organization','@id':origin+'/#organization','name':'Smartwhip Dubai','url':origin+'/','telephone':'+31684227916','areaServed':{'@type':'City','name':'Dubai'}})
 if path:
  home={'en':'Home','nl':'Home','fr':'Accueil'}[lang];prefix='' if lang=='en' else '/'+lang
  items=[{'@type':'ListItem','position':1,'name':home,'item':origin+prefix+'/'}]
  if path.startswith('blog/') :items.append({'@type':'ListItem','position':2,'name':'Blog','item':origin+prefix+'/blog/'})
  items.append({'@type':'ListItem','position':len(items)+1,'name':plain(re.search('<h1[^>]*>(.*?)</h1>',s)[1]),'item':url})
  if '<!-- SEO BREADCRUMBS -->' not in s:s=s.replace('<main','<!-- SEO BREADCRUMBS --><div class="section crumb" style="padding-top:20px;padding-bottom:0">'+' / '.join('<a href="'+it['item']+'">'+escape(it['name'])+'</a>' for it in items)+'</div><main',1)
  schemas.append({'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':items})
 s=re.sub('<!-- SEO SCHEMA -->.*?<!-- SEO SCHEMA END -->','',s,flags=re.S)
 if schemas:s=s.replace('</head>','<!-- SEO SCHEMA -->'+''.join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False)+'</script>' for x in schemas)+'<!-- SEO SCHEMA END --></head>')
 def image_size(m):
  tag=m[0];src=re.search('src="([^"]+)"',tag)
  if src and src[1].startswith('/'):
   file=root/src[1].lstrip('/')
   if file.exists():
    w,h={'/assets/deluxe.webp': (114, 305), '/assets/hero.webp': (880, 680), '/assets/smartwhip.webp': (92, 307), '/assets/tank.webp': (76, 292), '/assets/flyer.webp': (1600, 900)}[src[1]]
    if 'width=' not in tag:tag=tag[:-1]+f' width="{w}" height="{h}">'
  return tag
 s=re.sub('<img[^>]*>',image_size,s);p.write_text(s)
(root/'404.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Page not found | Smartwhip Dubai</title><link rel="stylesheet" href="/style.css"></head><body><main class="section"><h1>Page not found</h1><p>This page could not be found. / Deze pagina bestaat niet. / Cette page est introuvable.</p><a class="btn" href="/">Home</a></main></body></html>')
print('SEO updated: titles, descriptions, localized headings, local delivery guidance, schemas, image dimensions and 404.')
