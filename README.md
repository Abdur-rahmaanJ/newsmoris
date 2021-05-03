# newsmoris


```python
>>> from newsmoris import DefiMedia
>>> DefiMedia.top_news()
[
    {
        'title': '2ème phase de déconfinement : 82 % des fonctionnaires ont repris du service ce lundi\xa0', 
        'link': 'https://defimedia.info/2eme-phase-de-deconfinement-82-des-fonctionnaires-ont-repris-du-service-ce-lundi'
    },
    {
        'title': 'Saisie record de drogue : Ritesh Gurroby provisoirement inculpé devant la justice', 
        'link': 'https://defimedia.info/saisie-record-de-drogue-ritesh-gurroby-provisoirement-inculpe-devant-la-justice'
    }, 
    {
        'title': 'SC-HSC : quelles seront les considérations spéciales pour les candidats ?\xa0', 
        'link': 'https://defimedia.info/sc-hsc-quelles-seront-les-considerations-speciales-pour-les-candidats'
    }, 
    {
        'title': 'Bangladesh : 26 morts dans une collision de bateaux', 
        'link': 'https://defimedia.info/bangladesh-26-morts-dans-une-collision-de-bateaux'
    },
    ...
]
>>> DefiMedia.article('https://defimedia.info/bangladesh-26-morts-dans-une-collision-de-bateaux')
{
    'author': 'WWW. DEFIMEDIA.INFO', 
    'paragraphs': [
        "Des policiers inspectent un bateau rapide qui transportait des passagers lorsqu'il est entré en collision avec un bateau transportant du sable, tuant au moins 26 personnes, à Madaripur le 3 mai 2021 ", 
        'Au moins 26 personnes ont trouvé la mort et cinq autres ont été blessées lundi matin dans une collision entre deux bateaux sur un fleuve dans le centre du Bangladesh, selon la police.', 
        "La collision s'est produite entre une vedette rapide en provenance de la ville de Mawa, transportant une trentaine de passagers, et une barge chargée de sable sur le fleuve Padma, près de Shibchar.", 
        '"Les victimes ont toutes été heurtées à la tête. Nous avons jusqu\'à présent récupéré 26 corps, dont une femme. Nous avons également secouru cinq personnes blessées dont trois enfants", a déclaré à l\'AFP l\'inspecteur de police Amir Hossain.\xa0', 'Selon M. Hossain, la proue du bateau de passagers a été complètement détruite dans la collision avant de sombrer aussitôt dans le fleuve.\xa0', 
        '"La police, les pompiers et les équipes de secours de l\'armée sont sur place et mènent des opérations de recherche et de sauvetage", a-t-il précisé. La police a déclaré que des agents ont été immédiatement dépêchés sur place.', "Selon Abdur Rahman, témoin de l'accident, les bateaux sont entrés en collision dans un grand fracas et ont chaviré.\xa0", '"Nous nous sommes précipités sur place, où nous avons trouvé la vedette rapide coupée en deux. Des centaines de villageois ont immédiatement commencé à aider au sauvetage avant d\'être rejoints par la police et les pompiers", a-t-il raconté.', 
        "Le Bangladesh construit son plus grand pont routier et ferroviaire non loin du lieu de l'accident.\xa0", 
        ...
        ]
}
>>> DefiMedia.page('actualites', 0)
[
    {
        'title': 'Deuxième phase de réouverture : les ralentissements de la circulation sont de retour', 
        'link': 'https://defimedia.info/deuxieme-phase-de-reouverture-les-ralentissements-de-la-circulation-sont-de-retour'
    }, 
    {
        'title': 'Grand Journal de Radio Plus et Au Cœur de l’Info : retour aux horaires habituels', 
        'link': 'https://defimedia.info/grand-journal-de-radio-plus-et-au-coeur-de-linfo-retour-aux-horaires-habituels'
    },
    {
        'title': 'Zone rouge : les 560 bénéficiaires percevront leurs pensions à domicile', 
        'link': 'https://defimedia.info/zone-rouge-les-560-beneficiaires-percevront-leurs-pensions-domicile'
    },
    ...
]
>>> DefiMedia.page('actualites', 5) # category, page number
>>> DefiMedia.page('actualites', 100)
>>> DefiMedia.page('explikouka', 0)
>>> DefiMedia.page('faits-divers', 0)
>>> DefiMedia.page('defi-zen', 0)
>>> DefiMedia.page('politique', 0)
>>> DefiMedia.page('people', 0)
>>> DefiMedia.page('magazine', 0)
>>> DefiMedia.page('people', 0)
>>> DefiMedia.page('news-sunday', 0)
>>> DefiMedia.page('techno', 0)
```