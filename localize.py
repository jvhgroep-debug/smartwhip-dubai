from pathlib import Path
from html.parser import HTMLParser
from html import escape
from urllib.parse import quote,urlparse,parse_qs
import json,re
root=Path(__file__).parent/'dist';origin='https://creamchargersdubai.com'
rows='''ABOUT|OVER ONS|À PROPOS
PRODUCTS|PRODUCTEN|PRODUITS
DELIVERY|BEZORGING|LIVRAISON
FAQ|VEELGESTELDE VRAGEN|FAQ
PREMIUM CREAM CHARGERS|PREMIUM SLAGROOMPATRONEN|CARTOUCHES DE CRÈME PREMIUM
NITROUS OXIDE (N2O) · CULINARY USE · DUBAI|LACHGAS (N2O) · CULINAIR GEBRUIK · DUBAI|PROTOXYDE D’AZOTE (N2O) · USAGE CULINAIRE · DUBAÏ
Cream Chargers &|Slagroompatronen &|Cartouches de crème &
Laughing Gas Dubai.|Lachgas in Dubai.|Gaz hilarant à Dubaï.
Nitrous oxide (N2O), also known as laughing gas or lachgas, for culinary cream whipping. Discover Smartwhip & Cream Deluxe for cafés, restaurants and creative kitchens.|Lachgas (N2O), in het Engels nitrous oxide of laughing gas, voor het culinair bereiden van slagroom. Ontdek Smartwhip en Cream Deluxe voor cafés, restaurants en creatieve keukens.|Le protoxyde d’azote (N2O), également appelé gaz hilarant ou lachgas en néerlandais, pour la préparation culinaire de crème fouettée. Découvrez Smartwhip et Cream Deluxe pour les cafés, restaurants et cuisines créatives.
Order via WhatsApp ↗|Bestel via WhatsApp ↗|Commander via WhatsApp ↗
View products →|Bekijk producten →|Voir les produits →
Order on WhatsApp. Pay cash at your door.|Bestel via WhatsApp. Betaal contant aan de deur.|Commandez sur WhatsApp. Payez en espèces à la livraison.
WHATSAPP ORDERING|BESTELLEN VIA WHATSAPP|COMMANDE SUR WHATSAPP
DUBAI DELIVERY|BEZORGING IN DUBAI|LIVRAISON À DUBAÏ
CASH ON DELIVERY|CONTANT BIJ BEZORGING|PAIEMENT EN ESPÈCES À LA LIVRAISON
THE COLLECTION|HET ASSORTIMENT|LA COLLECTION
N2O cylinders in Dubai.|N2O-cilinders in Dubai.|Cylindres N2O à Dubaï.
Explore cream chargers and cylinders for your kitchen. Message us to confirm the right variant, stock and delivery.|Ontdek slagroompatronen en cilinders voor je keuken. Stuur ons een bericht om de juiste variant, voorraad en bezorging te bevestigen.|Découvrez les cartouches et cylindres pour votre cuisine. Contactez-nous pour confirmer le modèle, le stock et la livraison.
CULINARY COLLECTION|CULINAIR ASSORTIMENT|COLLECTION CULINAIRE
Premium cream chargers for whipped cream and culinary foams.|Premium slagroompatronen voor slagroom en culinaire schuimen.|Cartouches de crème premium pour crème fouettée et mousses culinaires.
A practical cylinder format for regular culinary use.|Een praktisch cilinderformaat voor regelmatig culinair gebruik.|Un format de cylindre pratique pour un usage culinaire régulier.
Discuss your requirements for 3kg, 5kg and 10kg tanks.|Bespreek je wensen voor tanks van 3 kg, 5 kg en 10 kg.|Discutez de vos besoins en réservoirs de 3 kg, 5 kg et 10 kg.
Ask for price|Vraag de prijs op|Demander le prix
Explore product →|Bekijk product →|Découvrir le produit →
FOR CREATIVE KITCHENS|VOOR CREATIEVE KEUKENS|POUR LES CUISINES CRÉATIVES
Nitrous oxide cream chargers|Lachgas-slagroompatronen|Cartouches de crème au protoxyde d’azote
for Dubai kitchens.|voor keukens in Dubai.|pour les cuisines de Dubaï.
Whipped cream, light foams and aerated recipes: the right culinary equipment helps your team prepare consistent creations.|Slagroom, lichte schuimen en luchtige recepten: de juiste culinaire apparatuur helpt je team consistente creaties te bereiden.|Crème fouettée, mousses légères et recettes aérées : le bon équipement culinaire aide votre équipe à obtenir des résultats réguliers.
Whether you run a café in Dubai Marina, a restaurant in Downtown Dubai or a catering kitchen, tell us what you need. We will help you confirm the cylinder, capacity and fittings before you order.|Of je nu een café in Dubai Marina, een restaurant in Downtown Dubai of een cateringkeuken hebt, vertel ons wat je nodig hebt. We helpen je vóór je bestelling de cilinder, inhoud en aansluitingen te controleren.|Que vous gériez un café à Dubai Marina, un restaurant à Downtown Dubai ou une cuisine de traiteur, indiquez-nous vos besoins. Nous vous aidons à vérifier le cylindre, la capacité et les raccords avant la commande.
Find the right product →|Vind het juiste product →|Trouver le bon produit →
SIMPLE FROM START TO FINISH|EENVOUDIG VAN BEGIN TOT EIND|SIMPLE DU DÉBUT À LA FIN
WhatsApp. Delivery.|WhatsApp. Bezorging.|WhatsApp. Livraison.
Cash at your door.|Contant aan de deur.|Espèces à votre porte.
Choose your product|Kies je product|Choisissez votre produit
Browse the collection and open WhatsApp from your preferred product.|Bekijk het assortiment en open WhatsApp bij het gewenste product.|Parcourez la collection et ouvrez WhatsApp depuis le produit choisi.
Confirm your order|Bevestig je bestelling|Confirmez votre commande
Send the quantity and your delivery location. We confirm availability, delivery timing, any delivery charge and your total before dispatch.|Stuur het aantal en je bezorgadres. We bevestigen vóór verzending de beschikbaarheid, bezorgtijd, eventuele bezorgkosten en het totaalbedrag.|Envoyez la quantité et votre adresse. Nous confirmons la disponibilité, le délai, les éventuels frais et le montant total avant l’expédition.
Pay on arrival|Betaal bij ontvangst|Payez à la réception
Receive your order at the agreed address and pay cash on delivery. No online payment is required.|Ontvang je bestelling op het afgesproken adres en betaal contant bij bezorging. Online betalen is niet nodig.|Recevez votre commande à l’adresse convenue et payez en espèces à la livraison. Aucun paiement en ligne n’est nécessaire.
Dubai delivery is arranged via WhatsApp. For other emirates, ask us to confirm service availability. Delivery times are confirmed for each order.|Bezorging in Dubai regel je via WhatsApp. Vraag voor andere emiraten naar de mogelijkheden. De bezorgtijd wordt per bestelling bevestigd.|La livraison à Dubaï est organisée sur WhatsApp. Pour les autres émirats, demandez confirmation de la disponibilité. Le délai est confirmé pour chaque commande.
GOOD TO KNOW|GOED OM TE WETEN|BON À SAVOIR
Your questions, answered.|Antwoorden op je vragen.|Les réponses à vos questions.
What are nitrous oxide, N2O, laughing gas and lachgas?|Wat zijn nitrous oxide, N2O, laughing gas en lachgas?|Que sont le protoxyde d’azote, le N2O, le laughing gas et le lachgas ?
Nitrous oxide is the gas referred to by the formula N2O. Laughing gas is its common English name; lachgas is the Dutch name. The cylinders listed here are intended for culinary cream whipping with compatible equipment.|Lachgas is het gas met de formule N2O. Nitrous oxide en laughing gas zijn Engelse namen. De cilinders op deze site zijn bedoeld voor het culinair bereiden van slagroom met geschikte apparatuur.|Le protoxyde d’azote est le gaz de formule N2O. Laughing gas est son nom courant anglais et lachgas son nom néerlandais. Les cylindres présentés sont destinés à la préparation culinaire de crème fouettée avec un équipement compatible.
How do I place an order?|Hoe plaats ik een bestelling?|Comment passer commande ?
Select Order via WhatsApp, then send your product, quantity and delivery address. We will confirm your order details and total.|Klik op Bestel via WhatsApp en stuur je product, aantal en bezorgadres. We bevestigen de bestelgegevens en het totaalbedrag.|Cliquez sur Commander via WhatsApp, puis envoyez le produit, la quantité et l’adresse. Nous confirmerons les détails et le montant total.
Can I pay cash on delivery?|Kan ik contant betalen bij bezorging?|Puis-je payer en espèces à la livraison ?
Yes. Orders are paid in cash when delivered. Your total and any delivery charge are confirmed in advance.|Ja. Je betaalt contant bij bezorging. Het totaalbedrag en eventuele bezorgkosten worden vooraf bevestigd.|Oui. Vous payez en espèces à la livraison. Le montant total et les éventuels frais sont confirmés à l’avance.
How long does delivery take?|Hoe lang duurt de bezorging?|Quel est le délai de livraison ?
Message us with your location and product. Availability and a delivery window will be confirmed before dispatch.|Stuur ons je locatie en product. Beschikbaarheid en een bezorgmoment worden vóór verzending bevestigd.|Envoyez-nous votre localisation et le produit. La disponibilité et le créneau de livraison seront confirmés avant l’expédition.
Which cylinder fits my dispenser?|Welke cilinder past op mijn slagroomspuit?|Quel cylindre convient à mon siphon ?
Send us your dispenser model and fittings before ordering. Cylinders require suitable equipment; follow the manufacturer’s compatibility instructions.|Stuur vóór je bestelling het model en de aansluitingen van je slagroomspuit. Cilinders vereisen geschikte apparatuur; volg de compatibiliteitsinstructies van de fabrikant.|Envoyez le modèle et les raccords de votre siphon avant de commander. Les cylindres nécessitent un équipement adapté ; suivez les instructions de compatibilité du fabricant.
Can I discuss bulk or repeat orders?|Kan ik grotere of terugkerende bestellingen bespreken?|Puis-je discuter de commandes en gros ou régulières ?
Yes. Send the products, quantities and your business requirements via WhatsApp for a quote.|Ja. Stuur de producten, aantallen en zakelijke wensen via WhatsApp voor een offerte.|Oui. Envoyez les produits, les quantités et vos besoins professionnels sur WhatsApp pour un devis.
What are these products intended for?|Waarvoor zijn deze producten bedoeld?|À quoi servent ces produits ?
Culinary use, including whipping cream and preparing aerated recipes with appropriate equipment. Handle, store and use cylinders according to the manufacturer’s instructions.|Voor culinair gebruik, zoals slagroom en luchtige recepten met geschikte apparatuur. Hanteer, bewaar en gebruik de cilinders volgens de instructies van de fabrikant.|Pour un usage culinaire, notamment la crème fouettée et les recettes aérées avec un équipement adapté. Manipulez, stockez et utilisez les cylindres selon les instructions du fabricant.
LET’S GET YOUR KITCHEN READY|MAAK JE KEUKEN KLAAR|PRÉPAREZ VOTRE CUISINE
Ready to order?|Klaar om te bestellen?|Prêt à commander ?
Message us on +31 6 84227916.|Stuur ons een bericht op +31 6 84227916.|Contactez-nous au +31 6 84227916.
Chat on WhatsApp ↗|Chat via WhatsApp ↗|Discuter sur WhatsApp ↗
Premium cream chargers · Culinary use only|Premium slagroompatronen · Alleen culinair gebruik|Cartouches de crème premium · Usage culinaire uniquement
Privacy|Privacy|Confidentialité
Delivery & payment|Bezorging en betaling|Livraison et paiement
WhatsApp · Order now ↗|WhatsApp · Bestel nu ↗|WhatsApp · Commander ↗
Home|Home|Accueil
Products|Producten|Produits
NITROUS OXIDE · CULINARY COLLECTION|LACHGAS · CULINAIR ASSORTIMENT|PROTOXYDE D’AZOTE · COLLECTION CULINAIRE
Elevate your culinary creations with the Cream Deluxe Cylinder. This culinary N2O cylinder is intended for whipping cream, preparing velvety foams and creating aerated recipes with appropriate equipment.|Til je culinaire creaties naar een hoger niveau met de Cream Deluxe-cilinder. Deze culinaire N2O-cilinder is bedoeld voor slagroom, fluweelzachte schuimen en luchtige recepten met geschikte apparatuur.|Sublimez vos créations avec le cylindre Cream Deluxe. Ce cylindre N2O culinaire est destiné à la crème fouettée, aux mousses veloutées et aux recettes aérées avec un équipement adapté.
Nitrous oxide (N2O) — also known as laughing gas or lachgas — for culinary use.|Lachgas (N2O), ook bekend als nitrous oxide of laughing gas, voor culinair gebruik.|Protoxyde d’azote (N2O), également appelé gaz hilarant ou lachgas, pour usage culinaire.
Culinary whipping and foams|Culinaire slagroom en schuimen|Crème fouettée et mousses culinaires
Confirm equipment compatibility before ordering|Controleer de compatibiliteit vóór je bestelling|Vérifiez la compatibilité avant de commander
WhatsApp ordering · Cash on delivery|Bestellen via WhatsApp · Contant bij bezorging|Commande sur WhatsApp · Espèces à la livraison
Quantity|Aantal|Quantité
Confirm the exact cylinder variant, stock, delivery charge and total via WhatsApp.|Bevestig de exacte cilinder, voorraad, bezorgkosten en het totaal via WhatsApp.|Confirmez le modèle exact, le stock, les frais de livraison et le total sur WhatsApp.
Product Description|Productomschrijving|Description du produit
Buy Cream Deluxe Cylinder in Dubai|Koop een Cream Deluxe-cilinder in Dubai|Acheter un cylindre Cream Deluxe à Dubaï
Kitchens that go through whipped cream and N2O every day need a supplier they can reorder from without fuss. We make it simple to buy a Cream Deluxe cylinder in Dubai for professional use. The Cream Deluxe N2O cylinder is a culinary gas cylinder for whipping cream and preparing light, aerated recipes. It gives busy teams a practical alternative to handling large numbers of single-use cream chargers.|Keukens die dagelijks slagroom en N2O gebruiken, hebben een leverancier nodig waar ze eenvoudig opnieuw kunnen bestellen. Bij ons koop je eenvoudig een Cream Deluxe-cilinder in Dubai voor professioneel gebruik. De Cream Deluxe N2O-cilinder is een culinaire gascilinder voor slagroom en lichte, luchtige recepten. Voor drukke teams is dit een praktisch alternatief voor veel kleine wegwerppatronen.|Les cuisines qui utilisent chaque jour de la crème fouettée et du N2O ont besoin d’un fournisseur permettant de commander simplement. Nous facilitons l’achat d’un cylindre Cream Deluxe à Dubaï pour un usage professionnel. Ce cylindre de gaz culinaire sert à fouetter la crème et à préparer des recettes légères et aérées. Il offre aux équipes occupées une alternative pratique aux nombreuses petites cartouches jetables.
This page is for buyers who already know what they need: a Cream Deluxe cylinder sourced in Dubai or elsewhere in the UAE from a supplier that focuses on cream charger and N2O products.|Deze pagina is voor kopers die weten wat ze nodig hebben: een Cream Deluxe-cilinder in Dubai of elders in de VAE van een leverancier gericht op slagroompatronen en N2O-producten.|Cette page s’adresse aux acheteurs qui savent ce qu’ils recherchent : un cylindre Cream Deluxe à Dubaï ou ailleurs aux Émirats auprès d’un fournisseur spécialisé dans les cartouches de crème et les produits N2O.
Cream Deluxe Cylinder for Professional Use|Cream Deluxe-cilinder voor professioneel gebruik|Cylindre Cream Deluxe pour usage professionnel
A cylinder suits businesses that use N2O often and want a steadier supply during service. Typical buyers include:|Een cilinder past bij bedrijven die vaak N2O gebruiken en tijdens hun dienstverlening een constantere voorraad wensen. Typische kopers zijn:|Un cylindre convient aux entreprises qui utilisent souvent du N2O et souhaitent un approvisionnement plus régulier pendant le service. Les acheteurs comprennent :
Restaurants and professional kitchens|Restaurants en professionele keukens|Restaurants et cuisines professionnelles
Cafés and dessert shops|Cafés en dessertwinkels|Cafés et boutiques de desserts
Bakeries and patisseries|Bakkerijen en patisserieën|Boulangeries et pâtisseries
Hotels and hospitality businesses|Hotels en horecabedrijven|Hôtels et établissements d’accueil
Catering companies and event kitchens|Cateringbedrijven en evenementkeukens|Traiteurs et cuisines événementielles
Commercial food-service operations|Commerciële horecakeukens|Services de restauration professionnels
For these teams, the appeal is practical. A single cylinder can mean fewer changeovers during a shift and simpler storage and stock tracking. Staff can also work from one clearly identified item instead of managing many small units.|Voor deze teams zijn de voordelen praktisch. Eén cilinder kan minder wisselingen tijdens een dienst en eenvoudiger opslag en voorraadbeheer betekenen. Medewerkers werken met één duidelijk herkenbaar product in plaats van veel kleine eenheden.|Pour ces équipes, l’intérêt est pratique. Un seul cylindre peut réduire les changements pendant le service et simplifier le stockage et le suivi du stock. Le personnel utilise un produit clairement identifié au lieu de gérer de nombreuses petites unités.
Cream Deluxe Cylinder Features|Kenmerken van de Cream Deluxe-cilinder|Caractéristiques du cylindre Cream Deluxe
Cream Deluxe N2O cylinder for culinary applications|Cream Deluxe N2O-cilinder voor culinaire toepassingen|Cylindre Cream Deluxe N2O pour applications culinaires
Cylinder format for regular, repeat use in commercial settings|Cilinderformaat voor regelmatig gebruik in professionele omgevingen|Format de cylindre pour un usage régulier en milieu professionnel
Suitable for whipping cream and other N2O-based kitchen preparations, when used with appropriate equipment|Geschikt voor slagroom en andere keukenbereidingen met N2O bij gebruik van geschikte apparatuur|Adapté à la crème fouettée et aux préparations culinaires au N2O avec un équipement approprié
Available to order for Dubai delivery; ask about other UAE locations|Te bestellen voor bezorging in Dubai; vraag naar andere locaties in de VAE|Disponible pour livraison à Dubaï ; renseignez-vous pour les autres lieux aux Émirats
Before ordering, check the size and variant options with our team. If you need details on capacity, fittings or compatibility with your equipment, message us and we will help you confirm the right choice.|Controleer vóór je bestelling de formaten en varianten met ons team. Voor informatie over inhoud, aansluitingen of compatibiliteit met je apparatuur stuur je ons een bericht. We helpen je de juiste keuze te bevestigen.|Vérifiez les tailles et les modèles avec notre équipe avant de commander. Pour les détails de capacité, de raccords ou de compatibilité, envoyez-nous un message : nous vous aiderons à confirmer le bon choix.
As with any pressurised product, cylinders should be handled, stored and used according to the manufacturer’s instructions and only for their intended culinary purpose.|Zoals bij elk product onder druk moeten cilinders volgens de instructies van de fabrikant worden gehanteerd, bewaard en gebruikt, uitsluitend voor het bedoelde culinaire doel.|Comme tout produit sous pression, les cylindres doivent être manipulés, stockés et utilisés selon les instructions du fabricant et uniquement pour leur usage culinaire prévu.
Cream Deluxe Cylinder Dubai and UAE|Cream Deluxe-cilinder in Dubai en de VAE|Cylindre Cream Deluxe à Dubaï et aux Émirats
Dubai’s hospitality sector depends on suppliers that are easy to work with and easy to reorder from. Many buyers searching for a Cream Deluxe supplier in Dubai want one place to check product details, ask questions and place an order.|De horeca in Dubai heeft behoefte aan leveranciers waarmee prettig werken en eenvoudig opnieuw bestellen mogelijk is. Veel kopers die een Cream Deluxe-leverancier in Dubai zoeken, willen één plek voor productinformatie, vragen en bestellingen.|Le secteur de l’hôtellerie-restauration de Dubaï a besoin de fournisseurs faciles à contacter et auprès desquels renouveler les commandes. Les acheteurs recherchant Cream Deluxe à Dubaï souhaitent un interlocuteur unique pour les informations, les questions et les commandes.
If you want to buy a Cream Deluxe cylinder in the UAE for a single outlet or several, our team can talk through your requirements and confirm delivery availability. Businesses comparing a Cream Deluxe cylinder’s price in Dubai can review the current listing on this page or contact us for the latest details.|Wil je een Cream Deluxe-cilinder kopen in de VAE voor één of meerdere vestigingen? Ons team bespreekt je wensen en bevestigt de bezorgmogelijkheden. Vergelijk de prijs in Dubai op deze pagina of vraag ons naar de actuele gegevens.|Vous souhaitez acheter un cylindre Cream Deluxe aux Émirats pour un ou plusieurs établissements ? Notre équipe étudie vos besoins et confirme les possibilités de livraison. Consultez le prix affiché sur cette page ou contactez-nous pour les dernières informations.
Buyers looking for Cream Deluxe cream chargers in Dubai alongside cylinders can also browse the rest of our range and discuss their order with one team.|Kopers die naast cilinders ook Cream Deluxe-slagroompatronen in Dubai zoeken, kunnen ons overige assortiment bekijken en hun bestelling met één team bespreken.|Les acheteurs recherchant des cartouches Cream Deluxe en complément des cylindres peuvent consulter le reste de la gamme et discuter de leur commande avec une seule équipe.
Order Cream Deluxe Cylinder Online|Bestel een Cream Deluxe-cilinder online|Commander un cylindre Cream Deluxe en ligne
Ready to buy? Confirm the product options, then order your Cream Deluxe cylinder online through WhatsApp. If you need help choosing a size, or want to discuss larger or repeat orders for your business, contact us and we will point you in the right direction.|Klaar om te kopen? Bevestig de productopties en bestel je Cream Deluxe-cilinder online via WhatsApp. Neem contact op voor hulp bij het formaat of om grotere of terugkerende zakelijke bestellingen te bespreken.|Prêt à acheter ? Confirmez les options, puis commandez votre cylindre Cream Deluxe en ligne sur WhatsApp. Contactez-nous pour choisir la taille ou discuter de commandes professionnelles plus importantes ou régulières.
Shop Cream Deluxe today and arrange an N2O supply for your Dubai or UAE kitchen. Pay cash on delivery.|Bestel Cream Deluxe en regel je N2O-voorraad voor je keuken in Dubai of de VAE. Betaal contant bij bezorging.|Commandez Cream Deluxe et organisez votre approvisionnement N2O pour votre cuisine à Dubaï ou aux Émirats. Payez en espèces à la livraison.
Discuss your requirements for whipped cream and aerated recipes with our team. Before ordering, confirm the exact variant, capacity, fittings and compatibility with your dispenser.|Bespreek je wensen voor slagroom en luchtige recepten met ons team. Controleer vóór je bestelling de exacte variant, inhoud, aansluitingen en compatibiliteit met je slagroomspuit.|Discutez de vos besoins en crème fouettée et recettes aérées avec notre équipe. Avant de commander, confirmez le modèle, la capacité, les raccords et la compatibilité avec votre siphon.
Ordering and delivery|Bestellen en bezorgen|Commande et livraison
Send your quantity and delivery address through WhatsApp. We confirm the product, current price, availability and delivery details before dispatch. Pay cash at your door.|Stuur je aantal en bezorgadres via WhatsApp. We bevestigen product, actuele prijs, beschikbaarheid en bezorggegevens vóór verzending. Betaal contant aan de deur.|Envoyez la quantité et l’adresse sur WhatsApp. Nous confirmons le produit, le prix actuel, la disponibilité et les détails de livraison avant l’expédition. Payez en espèces à votre porte.
Use and storage|Gebruik en opslag|Utilisation et stockage
For intended culinary use only. Follow the manufacturer’s handling, storage and operating instructions and use suitable compatible equipment.|Uitsluitend voor het bedoelde culinaire gebruik. Volg de instructies van de fabrikant voor hantering, opslag en gebruik en gebruik geschikte compatibele apparatuur.|Uniquement pour l’usage culinaire prévu. Suivez les instructions du fabricant pour la manipulation, le stockage et l’utilisation, avec un équipement compatible adapté.
Orders are handled via WhatsApp. When you contact us, you provide the contact and order details you choose to share, such as your name, phone number, delivery address and requested products. These details are used to respond to your enquiry and arrange your order and delivery.|Bestellingen verlopen via WhatsApp. Wanneer je contact opneemt, deel je de contact- en bestelgegevens die je zelf verstrekt, zoals je naam, telefoonnummer, bezorgadres en gewenste producten. Deze gegevens gebruiken we om je vraag te beantwoorden en je bestelling en bezorging te regelen.|Les commandes sont traitées sur WhatsApp. Lorsque vous nous contactez, vous partagez les coordonnées et détails choisis, comme votre nom, votre numéro, l’adresse de livraison et les produits souhaités. Ces informations servent à répondre à votre demande et à organiser votre commande et la livraison.
WhatsApp is a third-party service and its own privacy terms apply. This website has no account registration or online payment form. Contact us via WhatsApp for questions about your order information.|WhatsApp is een dienst van een derde partij met eigen privacyvoorwaarden. Deze website heeft geen accountregistratie of online betaalformulier. Neem via WhatsApp contact op voor vragen over je bestelgegevens.|WhatsApp est un service tiers soumis à ses propres conditions de confidentialité. Ce site ne propose ni inscription ni formulaire de paiement en ligne. Contactez-nous sur WhatsApp pour toute question concernant les informations de commande.'''
M={}
for row in rows.splitlines():
 en,nl,fr=row.split('|');M[en]={'nl':nl,'fr':fr}
# Product descriptions are included in every product-specific WhatsApp link.
product_info={
 'Smartwhip Silver':{'en':'Premium nitrous oxide (N2O) cream charger for whipped cream and culinary foams. Confirm cylinder size and equipment compatibility. Price on request.','nl':'Premium lachgas-slagroomcilinder (N2O) voor slagroom en culinaire schuimen. Formaat en compatibiliteit vooraf bevestigen. Prijs op aanvraag.','fr':'Cylindre de crème au protoxyde d’azote (N2O) pour crème fouettée et mousses culinaires. Taille et compatibilité à confirmer. Prix sur demande.'},
 'Cream Deluxe Cylinder':{'en':'Cream Deluxe culinary N2O cylinder for whipped cream, velvety foams and aerated recipes with appropriate equipment. Listed price: AED 600 (previously AED 800). Confirm the exact size and fittings.','nl':'Cream Deluxe N2O-cilinder voor slagroom, fluweelzachte schuimen en luchtige recepten met geschikte apparatuur. Getoonde prijs: AED 600 (voorheen AED 800). Formaat en aansluitingen bevestigen.','fr':'Cylindre Cream Deluxe N2O pour crème fouettée, mousses veloutées et recettes aérées avec équipement adapté. Prix affiché : 600 AED (auparavant 800 AED). Taille et raccords à confirmer.'},
 'Cream Charger Tanks':{'en':'Culinary nitrous oxide (N2O) cream charger tanks. Ask about 3kg, 5kg and 10kg options, current stock, fittings and compatibility. Price on request.','nl':'Culinaire lachgastanks (N2O). Vraag naar varianten van 3 kg, 5 kg en 10 kg, voorraad, aansluitingen en compatibiliteit. Prijs op aanvraag.','fr':'Réservoirs de protoxyde d’azote (N2O) à usage culinaire. Renseignez-vous sur les options 3 kg, 5 kg et 10 kg, le stock, les raccords et la compatibilité. Prix sur demande.'}}
def msg(product,lang,qty=1):
 desc=product_info[product][lang]
 if lang=='nl':return f'Hallo, ik wil bestellen:\nProduct: {product}\nProductomschrijving: {desc}\nAantal: {qty}\nBezorglocatie: Dubai\nBetaling: contant bij bezorging.\nGraag beschikbaarheid, bezorgtijd, bezorgkosten en totaal bevestigen.'
 if lang=='fr':return f'Bonjour, je souhaite commander :\nProduit : {product}\nDescription : {desc}\nQuantité : {qty}\nLivraison : Dubaï\nPaiement : en espèces à la livraison.\nMerci de confirmer la disponibilité, le délai, les frais et le total.'
 return f'Hello, I would like to order:\nProduct: {product}\nProduct description: {desc}\nQuantity: {qty}\nDelivery location: Dubai\nPayment: cash on delivery.\nPlease confirm availability, delivery time, delivery fees and total.'
def trans(t,lang):
 if lang=='en':return t
 v=t.strip()
 if v in M:return t.replace(v,M[v][lang])
 for name in product_info:
  if v==name+' for culinary kitchens':return name+(' voor culinaire keukens' if lang=='nl' else ' pour cuisines professionnelles')
  if v=='Order '+name+' ↗':return ('Bestel ' if lang=='nl' else 'Commander ')+name+' ↗'
 return t
originals=[p for p in root.rglob('*.html') if p.relative_to(root).parts[0] not in ('nl','fr','blog') and not p.relative_to(root).parts[0].startswith('cream-chargers-')]
slugs=['','smartwhip-silver/','cream-deluxe-cylinder/','cream-charger-tanks/','privacy/']
class Localize(HTMLParser):
 def __init__(self,lang,slug):super().__init__(convert_charrefs=True);self.lang=lang;self.slug=slug;self.out=[];self.tag='';self.in_script=False;self.current_product=next((n for n,s in [('Smartwhip Silver','smartwhip-silver/'),('Cream Deluxe Cylinder','cream-deluxe-cylinder/'),('Cream Charger Tanks','cream-charger-tanks/')] if s==slug),None)
 def handle_decl(self,d):self.out.append('<!'+d+'>')
 def handle_starttag(self,tag,attrs):
  self.tag=tag
  if tag=='html':attrs=[(k,self.lang if k=='lang' else v) for k,v in attrs]
  new=[]
  for k,v in attrs:
   if v is None:new.append((k,v));continue
   if k=='href' and v.startswith('https://wa.me/'):
    text=parse_qs(urlparse(v).query).get('text',[''])[0];prod=self.current_product or next((n for n in product_info if 'order '+n in text),None)
    if prod:v='https://wa.me/31684227916?text='+quote(msg(prod,self.lang))
    elif self.lang!='en':v='https://wa.me/31684227916?text='+quote('Hallo, ik wil slagroompatronen bestellen voor bezorging in Dubai en contant betalen. Graag voorraad, bezorgtijd en totaal bevestigen.' if self.lang=='nl' else 'Bonjour, je souhaite commander des cartouches de crème à Dubaï et payer en espèces à la livraison. Merci de confirmer le stock, le délai et le total.')
   if k=='href' and v.startswith('/') and not v.startswith('/style') and not v.startswith('/favicon'):
    v=('/'+self.lang if self.lang!='en' else '')+v
   if k=='content' and self.lang!='en':
    if 'nitrous oxide' in v.lower() or 'laughing gas' in v.lower():v=('Lachgas (N2O) en slagroompatronen in Dubai. Smartwhip en Cream Deluxe voor culinair gebruik. Bestel via WhatsApp en betaal contant bij bezorging.' if self.lang=='nl' else 'Protoxyde d’azote (N2O), gaz hilarant et cartouches de crème à Dubaï. Smartwhip et Cream Deluxe pour usage culinaire. WhatsApp et paiement en espèces à la livraison.')
   if k=='alt' and 'Dubai skyline' in v:v=('Slagroomcilinders en desserts met de skyline van Dubai' if self.lang=='nl' else 'Cylindres de crème et desserts devant Dubaï')
   new.append((k,v))
  self.out.append('<'+tag+''.join(' '+k+('="'+escape(v,quote=True)+'"' if v is not None else '') for k,v in new)+'>')
  if tag=='script':self.in_script=True
 def handle_endtag(self,tag):
  if tag=='head':
   for lang in ['en','nl','fr']:
    url=origin+('/'+lang if lang!='en' else '')+'/'+self.slug
    self.out.append(f'<link rel="alternate" hreflang="{lang}" href="{url}">')
   self.out.append(f'<link rel="canonical" href="{origin}{"/"+self.lang if self.lang!="en" else ""}/{self.slug}">')
  if tag=='nav':
   self.out.append('</nav><div class="languages" aria-label="Language">')
   for lang in ['en','nl','fr']:
    self.out.append(f'<a href="{"/"+lang if lang!="en" else ""}/{self.slug}" lang="{lang}" class="{"active" if lang==self.lang else ""}">{lang.upper()}</a>')
   self.out.append('</div>');return
  self.out.append('</'+tag+'>')
  if tag=='script':self.in_script=False
 def handle_data(self,data):
  if self.in_script and self.current_product:
   # Quantity changes retain the full description in the selected language.
   message=msg(self.current_product,self.lang,'__QTY__')
   data="document.getElementById('qty').addEventListener('input',function(){const n=Math.max(1,Math.min(1000,Number(this.value)||1));document.getElementById('product-order').href='https://wa.me/31684227916?text='+encodeURIComponent("+json.dumps(message,ensure_ascii=False)+".replace('__QTY__',String(n)));});"
  elif self.tag=='title' and self.lang!='en':
   if self.current_product:data=self.current_product+(' Dubai | Lachgas N2O & Slagroompatronen' if self.lang=='nl' else ' Dubaï | Protoxyde d’azote N2O & Crème')
   elif self.slug=='privacy/':data='Privacybeleid | Smartwhip Dubai' if self.lang=='nl' else 'Confidentialité | Smartwhip Dubai'
   else:data='Lachgas & Slagroompatronen Dubai | Smartwhip' if self.lang=='nl' else 'Gaz hilarant & Cartouches de crème Dubaï | Smartwhip'
  elif not self.in_script:data=escape(trans(data,self.lang))
  self.out.append(data)
for file in originals:
 slug=str(file.relative_to(root).parent);slug='' if slug=='.' else slug+'/'
 source=file.read_text()
 for lang in ['en','nl','fr']:
  parser=Localize(lang,slug);parser.feed(source)
  target=root/((lang+'/' if lang!='en' else '')+slug)/'index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(''.join(parser.out))
with (root/'style.css').open('a') as f:f.write('\n.languages{display:flex;gap:9px;font-size:11px;font-weight:bold;flex-shrink:0}.languages a{padding:3px 4px;color:#a8b8cc}.languages a.active{color:#e9c361;border-bottom:1px solid #e9c361}.nav{gap:22px}@media(max-width:800px){.nav{gap:10px;flex-wrap:wrap}.nav .languages{order:3;margin-left:auto}.nav>.btn{padding:7px 10px}}')
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+origin+('/'+lang if lang!='en' else '')+'/'+slug+'</loc></url>' for lang in ['en','nl','fr'] for slug in slugs)+'</urlset>')
print('Created 15 pages in EN/NL/FR, language links, canonical and hreflang tags, and full WhatsApp product messages.')
