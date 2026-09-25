#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de carnets CM2 :
1. Carnet_Eleve_Chasse_aux_fautes_CM2.pdf (10 pages A4)
2. Correctif_Parents_Chasse_aux_fautes_CM2.pdf (10 pages A4)
"""

import os
import subprocess
import sys

DATA_SEMAINES = [
    {
        "num": 1,
        "theme": "Mission Groupe Nominal",
        "sous_titre": "Les accords en genre et en nombre dans le groupe nominal",
        "regle": "Dans le groupe nominal, le déterminant, le nom et l'adjectif s'accordent en genre (masculin/féminin) et en nombre (singulier/pluriel). Attention aux pluriels en <em>-s</em>, <em>-x</em> et <em>-aux</em> (journal &rarr; journaux) et aux adjectifs placés avant ou après le nom !",
        "phrases": [
            {
                "id": 1,
                "nb_err": 3,
                "texte_err": "Les petit renards roux observent les oiseau dans les grand arbres.",
                "texte_corr": "Les petits renards roux observent les oiseaux dans les grands arbres.",
                "texte_annote": "Les <span class='err'>petit</span> <span class='fix'>petits</span> renards roux observent les <span class='err'>oiseau</span> <span class='fix'>oiseaux</span> dans les <span class='err'>grand</span> <span class='fix'>grands</span> arbres.",
                "explications": [
                    "<strong>petit &rarr; petits :</strong> L'adjectif qualificatif s'accorde au masculin pluriel avec le nom <em>renards</em>.",
                    "<strong>oiseau &rarr; oiseaux :</strong> Les noms en <em>-eau</em> prennent un <em>-x</em> au pluriel (déterminant <em>les</em>).",
                    "<strong>grand &rarr; grands :</strong> L'adjectif s'accorde au masculin pluriel avec le nom <em>arbres</em>."
                ],
                "indice": "Demande : « Avec quel nom s'accorde 'petit' ? Et que met-on à la fin des mots en '-eau' au pluriel ? »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Cette magnifique jument noir galope à travers les pré verdoyants.",
                "texte_corr": "Cette magnifique jument noire galope à travers les prés verdoyants.",
                "texte_annote": "Cette magnifique jument <span class='err'>noir</span> <span class='fix'>noire</span> galope à travers les <span class='err'>pré</span> <span class='fix'>prés</span> verdoyants.",
                "explications": [
                    "<strong>noir &rarr; noire :</strong> L'adjectif s'accorde au féminin singulier avec le nom <em>jument</em> (une jument noire).",
                    "<strong>pré &rarr; prés :</strong> Le nom prend la marque du pluriel <em>-s</em> derrière le déterminant <em>les</em>."
                ],
                "indice": "Demande : « Quel est le genre du mot 'jument' (masculin ou féminin) ? Regarde aussi le déterminant devant 'pré'. »"
            },
            {
                "id": 3,
                "nb_err": 3,
                "texte_err": "De curieuses et discret silhouettes traversent les ruelle sombre.",
                "texte_corr": "De curieuses et discrètes silhouettes traversent les ruelles sombres.",
                "texte_annote": "De curieuses et <span class='err'>discret</span> <span class='fix'>discrètes</span> silhouettes traversent les <span class='err'>ruelle</span> <span class='fix'>ruelles</span> <span class='err'>sombre</span> <span class='fix'>sombres</span>.",
                "explications": [
                    "<strong>discret &rarr; discrètes :</strong> Les deux adjectifs (<em>curieuses</em> et <em>discrètes</em>) s'accordent avec le nom féminin pluriel <em>silhouettes</em>.",
                    "<strong>ruelle &rarr; ruelles :</strong> Déterminant pluriel <em>les</em>, donc le nom prend un <em>-s</em>.",
                    "<strong>sombre &rarr; sombres :</strong> L'adjectif s'accorde au pluriel avec <em>ruelles</em>."
                ],
                "indice": "Demande : « Qui est discret ? Les silhouettes. Comment accorde-t-on cet adjectif au féminin pluriel ? »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Mon grand-père collectionne de vieux journales et de beau timbres rares.",
                "texte_corr": "Mon grand-père collectionne de vieux journaux et de beaux timbres rares.",
                "texte_annote": "Mon grand-père collectionne de vieux <span class='err'>journales</span> <span class='fix'>journaux</span> et de <span class='err'>beau</span> <span class='fix'>beaux</span> timbres rares.",
                "explications": [
                    "<strong>journales &rarr; journaux :</strong> Les noms en <em>-al</em> font leur pluriel en <em>-aux</em> (un journal &rarr; des journaux).",
                    "<strong>beau &rarr; beaux :</strong> L'adjectif prend un <em>-x</em> au masculin pluriel devant le nom <em>timbres</em>."
                ],
                "indice": "Demande : « Comment forme-t-on le pluriel d'un mot qui finit par '-al' comme journal ou cheval ? »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "Les vaillants chevaliers portent des armure étincelantes et de lourd boucliers.",
                "texte_corr": "Les vaillants chevaliers portent des armures étincelantes et de lourds boucliers.",
                "texte_annote": "Les vaillants chevaliers portent des <span class='err'>armure</span> <span class='fix'>armures</span> étincelantes et de <span class='err'>lourd</span> <span class='fix'>lourds</span> boucliers.",
                "explications": [
                    "<strong>armure &rarr; armures :</strong> Le déterminant <em>des</em> impose la marque du pluriel <em>-s</em> au nom <em>armures</em>.",
                    "<strong>lourd &rarr; lourds :</strong> L'adjectif s'accorde au masculin pluriel avec <em>boucliers</em>."
                ],
                "indice": "Demande : « Regarde le déterminant 'des' : combien y a-t-il d'armures ? Et comment accordes-tu 'lourd' avec les boucliers ? »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Ces délicieux gâteaux au chocolat dégagent de merveilleuses odeur printanière.",
                "texte_corr": "Ces délicieux gâteaux au chocolat dégagent de merveilleuses odeurs printanières.",
                "texte_annote": "Ces délicieux gâteaux au chocolat dégagent de merveilleuses <span class='err'>odeur</span> <span class='fix'>odeurs</span> <span class='err'>printanière</span> <span class='fix'>printanières</span>.",
                "explications": [
                    "<strong>odeur &rarr; odeurs :</strong> Précédé de <em>merveilleuses</em> (déterminant partitif pluriel <em>de</em>), le nom est au pluriel.",
                    "<strong>printanière &rarr; printanières :</strong> L'adjectif s'accorde au féminin pluriel avec le nom <em>odeurs</em>."
                ],
                "indice": "Demande : « Regarde l'adjectif 'merveilleuses' : est-il au singulier ou au pluriel ? Accorde le nom et le 2e adjectif ! »"
            }
        ],
        "vigilance": "Au CM2, l'erreur la plus fréquente dans le groupe nominal est l'oubli de l'accord de l'adjectif lorsqu'il est placé AVANT le nom (ex: <em>de grands arbres</em>)."
    },
    {
        "num": 2,
        "theme": "Mission Homophones Fondamentaux",
        "sous_titre": "Distinguer a/à, ont/on, et/est, son/sont",
        "regle": "Utilise les tests magiques de substitution dans le passé :<br>• <strong>a / à :</strong> remplace par <em>avait</em> (si oui &rarr; <strong>a</strong> sans accent, sinon &rarr; <strong>à</strong>).<br>• <strong>on / ont :</strong> remplace par <em>avaient</em> (si oui &rarr; <strong>ont</strong>, sinon &rarr; <strong>on</strong>).<br>• <strong>et / est :</strong> remplace par <em>était</em> (si oui &rarr; <strong>est</strong>, sinon &rarr; <strong>et</strong>).<br>• <strong>son / sont :</strong> remplace par <em>étaient</em> (si oui &rarr; <strong>sont</strong>, sinon &rarr; <strong>son</strong> = mon).",
        "phrases": [
            {
                "id": 1,
                "nb_err": 3,
                "texte_err": "Léo à oublié son manteau et il et parti a l'école sans son écharpe.",
                "texte_corr": "Léo a oublié son manteau et il est parti à l'école sans son écharpe.",
                "texte_annote": "Léo <span class='err'>à</span> <span class='fix'>a</span> oublié son manteau et il <span class='err'>et</span> <span class='fix'>est</span> parti <span class='err'>a</span> <span class='fix'>à</span> l'école sans son écharpe.",
                "explications": [
                    "<strong>à &rarr; a :</strong> Verbe avoir. Test : « Léo <em>avait</em> oublié » (donc pas d'accent).",
                    "<strong>et &rarr; est :</strong> Verbe être. Test : « il <em>était</em> parti » (donc e-s-t).",
                    "<strong>a &rarr; à :</strong> Préposition de lieu. On ne peut pas dire « parti <em>avait</em> l'école »."
                ],
                "indice": "Demande : « Essaie de remplacer chaque mot par 'avait' ou par 'était' pour vérifier si c'est un verbe. »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "On sonne a la porte mais ils son partis faire des courses au marché.",
                "texte_corr": "On sonne à la porte mais ils sont partis faire des courses au marché.",
                "texte_annote": "On sonne <span class='err'>a</span> <span class='fix'>à</span> la porte mais ils <span class='err'>son</span> <span class='fix'>sont</span> partis faire des courses au marché.",
                "explications": [
                    "<strong>a &rarr; à :</strong> Préposition. On ne peut pas dire « on sonne <em>avait</em> la porte ».",
                    "<strong>son &rarr; sont :</strong> Verbe être au pluriel. Test : « ils <em>étaient</em> partis » (donc s-o-n-t)."
                ],
                "indice": "Demande : « Peut-on dire 'ils étaient partis' ? Si oui, le verbe s'écrit avec un 't'. »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Les enfants on préparé une tarte et son parfum et délicieux.",
                "texte_corr": "Les enfants ont préparé une tarte et son parfum est délicieux.",
                "texte_annote": "Les enfants <span class='err'>on</span> <span class='fix'>ont</span> préparé une tarte et son parfum <span class='err'>et</span> <span class='fix'>est</span> délicieux.",
                "explications": [
                    "<strong>on &rarr; ont :</strong> Verbe avoir (3e pers. pluriel). Test : « les enfants <em>avaient</em> préparé ».",
                    "<strong>et &rarr; est :</strong> Verbe être. Test : « son parfum <em>était</em> délicieux »."
                ],
                "indice": "Demande : « Mets la phrase à l'imparfait : 'Les enfants ... préparé et le parfum ... délicieux'. »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Sarah a prêté sont vélo a son meilleur ami pour le week-end.",
                "texte_corr": "Sarah a prêté son vélo à son meilleur ami pour le week-end.",
                "texte_annote": "Sarah a prêté <span class='err'>sont</span> <span class='fix'>son</span> vélo <span class='err'>a</span> <span class='fix'>à</span> son meilleur ami pour le week-end.",
                "explications": [
                    "<strong>sont &rarr; son :</strong> Déterminant possessif. Test : « elle a prêté <em>mon</em> vélo » (donc s-o-n).",
                    "<strong>a &rarr; à :</strong> Préposition. On ne peut pas dire « prêté vélo <em>avait</em> son ami »."
                ],
                "indice": "Demande : « Peut-on remplacer 'sont' par 'mon' ? Si oui, c'est le possessif sans 't'. »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "Tout le monde et d'accord : on à rarement vu un orage d'une telle violence.",
                "texte_corr": "Tout le monde est d'accord : on a rarement vu un orage d'une telle violence.",
                "texte_annote": "Tout le monde <span class='err'>et</span> <span class='fix'>est</span> d'accord : on <span class='err'>à</span> <span class='fix'>a</span> rarement vu un orage d'une telle violence.",
                "explications": [
                    "<strong>et &rarr; est :</strong> Verbe être. Test : « tout le monde <em>était</em> d'accord ».",
                    "<strong>à &rarr; a :</strong> Verbe avoir. Test : « on <em>avait</em> rarement vu »."
                ],
                "indice": "Demande : « Essaie de remplacer par 'était' au début et par 'avait' ensuite. Que constates-tu ? »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Mes voisins on un beau potager et ils son très fiers de leurs légumes.",
                "texte_corr": "Mes voisins ont un beau potager et ils sont très fiers de leurs légumes.",
                "texte_annote": "Mes voisins <span class='err'>on</span> <span class='fix'>ont</span> un beau potager et ils <span class='err'>son</span> <span class='fix'>sont</span> très fiers de leurs légumes.",
                "explications": [
                    "<strong>on &rarr; ont :</strong> Verbe avoir. Test : « mes voisins <em>avaient</em> un beau potager ».",
                    "<strong>son &rarr; sont :</strong> Verbe être. Test : « ils <em>étaient</em> très fiers »."
                ],
                "indice": "Demande : « Dans les deux cas, ce sont des verbes au pluriel ! Quelles sont leurs lettres finales ? »"
            }
        ],
        "vigilance": "Le piège classique : confondre le pronom sujet <em>on</em> (qui peut se remplacer par <em>il</em>) et le verbe <em>ont</em> (remplaçable par <em>avaient</em>)."
    },
    {
        "num": 3,
        "theme": "Mission Accord Sujet-Verbe Délicat",
        "sous_titre": "Sujet inversé, éloigné ou composé de plusieurs personnes",
        "regle": "Pose toujours la question : <strong>« Qui est-ce qui + verbe ? »</strong>.<br>• <strong>Le piège du pronom écran :</strong> dans <em>« Il les regarde »</em>, le sujet est <strong>il</strong> (singulier), pas <em>les</em> !<br>• <strong>Sujet inversé :</strong> cherche le sujet placé après le verbe (<em>« Au loin résonnent les cloches »</em>).<br>• <strong>Moi + quelqu'un = nous</strong> (-ons) ; <strong>Toi + quelqu'un = vous</strong> (-ez).",
        "phrases": [
            {
                "id": 1,
                "nb_err": 2,
                "texte_err": "Dans la forêt silencieuse rôde trois loups affamé sous la lune.",
                "texte_corr": "Dans la forêt silencieuse rôdent trois loups affamés sous la lune.",
                "texte_annote": "Dans la forêt silencieuse <span class='err'>rôde</span> <span class='fix'>rôdent</span> trois loups <span class='err'>affamé</span> <span class='fix'>affamés</span> sous la lune.",
                "explications": [
                    "<strong>rôde &rarr; rôdent :</strong> Le sujet est inversé : « Qui rôde ? » &rarr; <em>trois loups</em> (3e pers. du pluriel, terminaison <em>-ent</em>).",
                    "<strong>affamé &rarr; affamés :</strong> Accord de l'adjectif au masculin pluriel avec <em>loups</em>."
                ],
                "indice": "Demande : « Qui est-ce qui rôde ? Le sujet est placé après le verbe ! Et comment accordes-tu 'affamé' ? »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Le renard observent les mulots puis il les attrapent avec agilité.",
                "texte_corr": "Le renard observe les mulots puis il les attrape avec agilité.",
                "texte_annote": "Le renard <span class='err'>observent</span> <span class='fix'>observe</span> les mulots puis il les <span class='err'>attrapent</span> <span class='fix'>attrape</span> avec agilité.",
                "explications": [
                    "<strong>observent &rarr; observe :</strong> Le sujet est <em>Le renard</em> (singulier, 3e pers.).",
                    "<strong>attrapent &rarr; attrape :</strong> Le sujet est le pronom <em>il</em> (singulier). <em>Les</em> est un pronom complément (COD), ce n'est PAS le sujet !"
                ],
                "indice": "Demande : « Dans 'il les attrape', qui fait l'action d'attraper ? Est-ce 'il' ou 'les' ? Ne te fais pas piéger par 'les' ! »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Le maître et son élève regarde attentivement les carte du ciel.",
                "texte_corr": "Le maître et son élève regardent attentivement les cartes du ciel.",
                "texte_annote": "Le maître et son élève <span class='err'>regarde</span> <span class='fix'>regardent</span> attentivement les <span class='err'>carte</span> <span class='fix'>cartes</span> du ciel.",
                "explications": [
                    "<strong>regarde &rarr; regardent :</strong> Sujet coordonné : « Le maître et son élève » équivaut à <em>ils</em> (pluriel).",
                    "<strong>carte &rarr; cartes :</strong> Le nom prend un <em>-s</em> derrière le déterminant pluriel <em>les</em>."
                ],
                "indice": "Demande : « Combien de personnes font l'action de regarder ? Deux ! Donc le verbe doit être au pluriel. »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Derrière la haute colline surgit soudain deux cavaliers masqué.",
                "texte_corr": "Derrière la haute colline surgissent soudain deux cavaliers masqués.",
                "texte_annote": "Derrière la haute colline <span class='err'>surgit</span> <span class='fix'>surgissent</span> soudain deux cavaliers <span class='err'>masqué</span> <span class='fix'>masqués</span>.",
                "explications": [
                    "<strong>surgit &rarr; surgissent :</strong> Sujet inversé : qui surgit ? « Deux cavaliers » (3e pers. du pluriel).",
                    "<strong>masqué &rarr; masqués :</strong> Accord de l'adjectif au masculin pluriel avec <em>cavaliers</em>."
                ],
                "indice": "Demande : « Pose la question : 'Qui est-ce qui surgit derrière la colline ?' »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "Les feuilles dorées que le vent d'automne emportent tourbillonne dans l'allée.",
                "texte_corr": "Les feuilles dorées que le vent d'automne emporte tourbillonnent dans l'allée.",
                "texte_annote": "Les feuilles dorées que le vent d'automne <span class='err'>emportent</span> <span class='fix'>emporte</span> <span class='err'>tourbillonne</span> <span class='fix'>tourbillonnent</span> dans l'allée.",
                "explications": [
                    "<strong>emportent &rarr; emporte :</strong> Le sujet du verbe <em>emporter</em> est « le vent d'automne » (singulier).",
                    "<strong>tourbillonne &rarr; tourbillonnent :</strong> Le sujet du verbe <em>tourbillonner</em> est « Les feuilles dorées » (pluriel)."
                ],
                "indice": "Demande : « Qui emporte ? Le vent. Et qui tourbillonne dans l'allée ? Les feuilles ! »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Mon frère et moi vont au stade pendant que toi et Julie finit votre dessin.",
                "texte_corr": "Mon frère et moi allons au stade pendant que toi et Julie finissez votre dessin.",
                "texte_annote": "Mon frère et moi <span class='err'>vont</span> <span class='fix'>allons</span> au stade pendant que toi et Julie <span class='err'>finit</span> <span class='fix'>finissez</span> votre dessin.",
                "explications": [
                    "<strong>vont &rarr; allons :</strong> « Mon frère et moi » = <strong>nous</strong> (1re personne du pluriel).",
                    "<strong>finit &rarr; finissez :</strong> « Toi et Julie » = <strong>vous</strong> (2e personne du pluriel)."
                ],
                "indice": "Demande : « Par quel pronom remplaces-tu 'Mon frère et moi' ? Et 'Toi et Julie' ? »"
            }
        ],
        "vigilance": "Le piège absolu du CM2 : accorder le verbe avec le pronom qui le précède immédiatement (ex: <em>il les mangent</em> au lieu de <em>il les mange</em>)."
    },
    {
        "num": 4,
        "theme": "Mission Participe Passé ou Infinitif",
        "sous_titre": "Choisir entre -é, -ée, -és, -ées et la terminaison en -er",
        "regle": "Utilise l'astuce magique <strong>« mordre / mordu »</strong> (ou <em>vendre / vendu</em>) :<br>• Si tu peux dire <strong>mordre</strong> &rarr; verbe à l'infinitif en <strong>-er</strong> (souvent après préposition : à, de, pour, sans).<br>• Si tu peux dire <strong>mordu</strong> &rarr; participe passé en <strong>-é</strong>.<br>• <strong>Attention :</strong> avec l'auxiliaire <strong>être</strong>, le participe passé s'accorde TOUJOURS avec le sujet en genre et en nombre !",
        "phrases": [
            {
                "id": 1,
                "nb_err": 2,
                "texte_err": "Après avoir marcher pendant deux heures, nous avons décider de nous reposer.",
                "texte_corr": "Après avoir marché pendant deux heures, nous avons décidé de nous reposer.",
                "texte_annote": "Après avoir <span class='err'>marcher</span> <span class='fix'>marché</span> pendant deux heures, nous avons <span class='err'>décider</span> <span class='fix'>décidé</span> de nous reposer.",
                "explications": [
                    "<strong>marcher &rarr; marché :</strong> Test : « après avoir <em>mordu</em> », donc participe passé en <em>-é</em>.",
                    "<strong>décider &rarr; décidé :</strong> Test : « nous avons <em>mordu</em> », participe passé avec avoir."
                ],
                "indice": "Demande : « Dit-on 'après avoir mordu' ou 'après avoir mordre' ? »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Les fillettes sont arriver tôt pour répété leur poésie préférée.",
                "texte_corr": "Les fillettes sont arrivées tôt pour répéter leur poésie préférée.",
                "texte_annote": "Les fillettes sont <span class='err'>arriver</span> <span class='fix'>arrivées</span> tôt pour <span class='err'>répété</span> <span class='fix'>répéter</span> leur poésie préférée.",
                "explications": [
                    "<strong>arriver &rarr; arrivées :</strong> Participe passé employé avec l'auxiliaire <em>être</em> (sont) : accord avec le sujet féminin pluriel <em>les fillettes</em>.",
                    "<strong>répété &rarr; répéter :</strong> Infinitif après la préposition <em>pour</em>. Test : « pour <em>mordre</em> »."
                ],
                "indice": "Demande : « Quel est l'auxiliaire devant arriver ? C'est être (sont), donc on accorde avec les fillettes ! »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Le charpentier a commencer à coupé les grosses poutres du grenier.",
                "texte_corr": "Le charpentier a commencé à couper les grosses poutres du grenier.",
                "texte_annote": "Le charpentier a <span class='err'>commencer</span> <span class='fix'>commencé</span> à <span class='err'>coupé</span> <span class='fix'>couper</span> les grosses poutres du grenier.",
                "explications": [
                    "<strong>commencer &rarr; commencé :</strong> Participe passé avec avoir (a <em>mordu</em>).",
                    "<strong>coupé &rarr; couper :</strong> Infinitif après la préposition <em>à</em> (à <em>mordre</em>)."
                ],
                "indice": "Demande : « Fais le test : 'a mordu à mordre'. Quel verbe est à l'infinitif ? »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Les hirondelles sont revenu au printemps pour réparer leur nid abîmer.",
                "texte_corr": "Les hirondelles sont revenues au printemps pour réparer leur nid abîmé.",
                "texte_annote": "Les hirondelles sont <span class='err'>revenu</span> <span class='fix'>revenues</span> au printemps pour réparer leur nid <span class='err'>abîmer</span> <span class='fix'>abîmé</span>.",
                "explications": [
                    "<strong>revenu &rarr; revenues :</strong> Participe passé avec l'auxiliaire <em>être</em>, accord au féminin pluriel avec <em>les hirondelles</em>.",
                    "<strong>abîmer &rarr; abîmé :</strong> Participe passé employé comme adjectif (un nid <em>mordu</em>, pas un nid mordre)."
                ],
                "indice": "Demande : « Une hirondelle est féminin. Avec l'auxiliaire être, quelle marque ajoute-t-on ? »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "Pour réussir ce délicieux gâteau, il faut bien mélangé la pâte sans la renversé.",
                "texte_corr": "Pour réussir ce délicieux gâteau, il faut bien mélanger la pâte sans la renverser.",
                "texte_annote": "Pour réussir ce délicieux gâteau, il faut bien <span class='err'>mélangé</span> <span class='fix'>mélanger</span> la pâte sans la <span class='err'>renversé</span> <span class='fix'>renverser</span>.",
                "explications": [
                    "<strong>mélangé &rarr; mélanger :</strong> Infinitif après <em>faut</em> (« il faut <em>mordre</em> »).",
                    "<strong>renversé &rarr; renverser :</strong> Infinitif après la préposition <em>sans</em> (« sans la <em>mordre</em> »)."
                ],
                "indice": "Demande : « Remplace par le verbe battre : 'il faut bien battre la pâte sans la battre'. Ce sont deux infinitifs ! »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Toutes les fenêtres du château sont resté ouvert après le violent orage.",
                "texte_corr": "Toutes les fenêtres du château sont restées ouvertes après le violent orage.",
                "texte_annote": "Toutes les fenêtres du château sont <span class='err'>resté</span> <span class='fix'>restées</span> <span class='err'>ouvert</span> <span class='fix'>ouvertes</span> après le violent orage.",
                "explications": [
                    "<strong>resté &rarr; restées :</strong> Participe passé avec l'auxiliaire <em>être</em>, accord avec <em>Toutes les fenêtres</em> (féminin pluriel).",
                    "<strong>ouvert &rarr; ouvertes :</strong> Adjectif qualificatif accordé au féminin pluriel avec <em>fenêtres</em>."
                ],
                "indice": "Demande : « Qui est resté ouvert ? Les fenêtres. Quel est leur genre et leur nombre ? »"
            }
        ],
        "vigilance": "Après une préposition (à, de, pour, sans, par), le verbe qui suit est TOUJOURS à l'infinitif en <em>-er</em>."
    },
    {
        "num": 5,
        "theme": "Mission Homophones Démonstratifs & Possessifs",
        "sous_titre": "Maîtriser ce/se, ces/ses, c'est/s'est",
        "regle": "Distingue l'action sur soi-même (pronominal) de la désignation (démonstratif) ou de la possession :<br>• <strong>se / s'est :</strong> s'emploie avec un verbe pronominal (action que l'on fait sur soi : <em>il <strong>se</strong> lave, il <strong>s'est</strong> endormi</em>). Test : remplace par <em>je me</em>.<br>• <strong>ce / ces :</strong> montre quelque chose (démonstratif = celui-ci / ceux-là).<br>• <strong>ses :</strong> indique la possession (les siens). Test : remplace par <em>mes</em> ou <em>tes</em>.<br>• <strong>c'est :</strong> équivaut à <em>cela est</em> (remplaçable par <em>c'était</em>).",
        "phrases": [
            {
                "id": 1,
                "nb_err": 2,
                "texte_err": "Le jeune champion ce lève très tôt car s'est le grand jour de la finale.",
                "texte_corr": "Le jeune champion se lève très tôt car c'est le grand jour de la finale.",
                "texte_annote": "Le jeune champion <span class='err'>ce</span> <span class='fix'>se</span> lève très tôt car <span class='err'>s'est</span> <span class='fix'>c'est</span> le grand jour de la finale.",
                "explications": [
                    "<strong>ce lève &rarr; se lève :</strong> Verbe pronominal (se lever). Test : « je <em>me</em> lève », donc s-e.",
                    "<strong>s'est &rarr; c'est :</strong> Présentatif. Test : « car <em>c'était</em> le grand jour », donc c-apostrophe."
                ],
                "indice": "Demande : « Le champion se lève lui-même ? Oui (se). Peut-on dire 'c'était le grand jour' ? Oui (c'est). »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Maxime prend ces affaires de dessin et il ce dépêche d'aller en récréation.",
                "texte_corr": "Maxime prend ses affaires de dessin et il se dépêche d'aller en récréation.",
                "texte_annote": "Maxime prend <span class='err'>ces</span> <span class='fix'>ses</span> affaires de dessin et il <span class='err'>ce</span> <span class='fix'>se</span> dépêche d'aller en récréation.",
                "explications": [
                    "<strong>ces &rarr; ses :</strong> Déterminant possessif. Test : « ses affaires » = « <em>mes</em> affaires » (les siennes).",
                    "<strong>ce dépêche &rarr; se dépêche :</strong> Verbe pronominal (se dépêcher)."
                ],
                "indice": "Demande : « À qui appartiennent les affaires ? À Maxime (ses = les siennes). Et se dépêcher prend un s ! »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Le skieur c'est blessé à la cheville pendant c'est entraînements intensifs.",
                "texte_corr": "Le skieur s'est blessé à la cheville pendant ses entraînements intensifs.",
                "texte_annote": "Le skieur <span class='err'>c'est</span> <span class='fix'>s'est</span> blessé à la cheville pendant <span class='err'>c'est</span> <span class='fix'>ses</span> entraînements intensifs.",
                "explications": [
                    "<strong>c'est blessé &rarr; s'est blessé :</strong> Verbe pronominal au passé composé (se blesser). Test : « je <em>me suis</em> blessé ».",
                    "<strong>c'est entraînements &rarr; ses entraînements :</strong> Déterminant possessif (les siens)."
                ],
                "indice": "Demande : « Peut-on dire 'je me suis blessé' ? Oui, donc s'est. Et ce sont ses entraînements à lui (possessif) ! »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Se matin, le renard ce cache derrière les buissons pour guetter sa proie.",
                "texte_corr": "Ce matin, le renard se cache derrière les buissons pour guetter sa proie.",
                "texte_annote": "<span class='err'>Se</span> <span class='fix'>Ce</span> matin, le renard <span class='err'>ce</span> <span class='fix'>se</span> cache derrière les buissons pour guetter sa proie.",
                "explications": [
                    "<strong>Se matin &rarr; Ce matin :</strong> Déterminant démonstratif (on montre ce matin-là, avec un C).",
                    "<strong>ce cache &rarr; se cache :</strong> Verbe pronominal (se cacher, avec un S)."
                ],
                "indice": "Demande : « 'Ce matin' montre le jour, donc avec un C. 'Se cacher' est une action sur soi, donc avec un S. »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "Lucas c'est réveillé en sursaut et il ce demande quelle heure il est.",
                "texte_corr": "Lucas s'est réveillé en sursaut et il se demande quelle heure il est.",
                "texte_annote": "Lucas <span class='err'>c'est</span> <span class='fix'>s'est</span> réveillé en sursaut et il <span class='err'>ce</span> <span class='fix'>se</span> demande quelle heure il est.",
                "explications": [
                    "<strong>c'est réveillé &rarr; s'est réveillé :</strong> Verbe pronominal (se réveiller). Test : « je <em>me suis</em> réveillé ».",
                    "<strong>ce demande &rarr; se demande :</strong> Verbe pronominal (se demander)."
                ],
                "indice": "Demande : « Dans les deux cas, le sujet fait l'action sur lui-même : réveiller et demander prennent un S ! »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Regarde tout ses oiseaux qui c'envolent au-dessus de notre maison.",
                "texte_corr": "Regarde tous ces oiseaux qui s'envolent au-dessus de notre maison.",
                "texte_annote": "Regarde tous <span class='err'>ses</span> <span class='fix'>ces</span> oiseaux qui <span class='err'>c'envolent</span> <span class='fix'>s'envolent</span> au-dessus de notre maison.",
                "explications": [
                    "<strong>ses &rarr; ces :</strong> Déterminant démonstratif : on montre du doigt les oiseaux dans le ciel (ceux-là).",
                    "<strong>c'envolent &rarr; s'envolent :</strong> Verbe pronominal (s'envoler)."
                ],
                "indice": "Demande : « Montre-t-on les oiseaux du doigt ? Si oui, c'est le démonstratif avec un C ! »"
            }
        ],
        "vigilance": "Pour vérifier <em>ces / ses</em> : remplace par <em>ceux-là</em> (si ça marche &rarr; <strong>ces</strong>) ou par <em>les siens / mes</em> (si ça marche &rarr; <strong>ses</strong>)."
    },
    {
        "num": 6,
        "theme": "Mission Présent et Imparfait",
        "sous_titre": "Les pièges de conjugaison au présent et à l'imparfait",
        "regle": "Rappels clés des terminaisons pièges :<br>• <strong>Au présent :</strong> Avec <em>tu</em>, il y a TOUJOURS un <strong>s</strong> (tu prends, tu franchis). Avec <em>il</em>, les verbes en <em>-dre</em> gardent leur <strong>d</strong> (il prend, il mord) et les verbes en <em>-ndre</em> prennent un <strong>t</strong> (il peint).<br>• <strong>À l'imparfait :</strong> Les terminaisons sont invariables : <strong>-ais, -ais, -ait, -ions, -iez, -aient</strong>. Avec <em>nous</em> et <em>vous</em>, n'oublie jamais le <strong>i</strong> même après un radical en i ou y (nous cri<strong>i</strong>ons, vous balay<strong>i</strong>ez) !",
        "phrases": [
            {
                "id": 1,
                "nb_err": 2,
                "texte_err": "Autrefois, nous copions de longs textes pendant que vous balayez la classe.",
                "texte_corr": "Autrefois, nous copiions de longs textes pendant que vous balayiez la classe.",
                "texte_annote": "Autrefois, nous <span class='err'>copions</span> <span class='fix'>copiions</span> de longs textes pendant que vous <span class='err'>balayez</span> <span class='fix'>balayiez</span> la classe.",
                "explications": [
                    "<strong>copions &rarr; copiions :</strong> À l'imparfait avec <em>nous</em>, les verbes en <em>-ier</em> doublent le « i » (radical copi- + terminaison -ions).",
                    "<strong>balayez &rarr; balayiez :</strong> À l'imparfait avec <em>vous</em>, la terminaison est <em>-iez</em> (ne pas confondre avec le présent en -ez)."
                ],
                "indice": "Demande : « 'Autrefois' indique le passé. Quelle est la terminaison de l'imparfait avec nous (-ions) et vous (-iez) ? »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Le jeune chiot prends son jouet et il mordt dedans avec énergie.",
                "texte_corr": "Le jeune chiot prend son jouet et il mord dedans avec énergie.",
                "texte_annote": "Le jeune chiot <span class='err'>prends</span> <span class='fix'>prend</span> son jouet et il <span class='err'>mordt</span> <span class='fix'>mord</span> dedans avec énergie.",
                "explications": [
                    "<strong>prends &rarr; prend :</strong> Au présent avec <em>il</em> (3e pers. sing.), les verbes en <em>-dre</em> se terminent par un simple <strong>d</strong> (pas de s).",
                    "<strong>mordt &rarr; mord :</strong> Même règle : le d final suffit à la 3e personne du singulier (il mord, pas de t)."
                ],
                "indice": "Demande : « Avec les verbes en -dre au présent, quelle est la lettre finale avec 'il' ? Juste le D ! »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Chaque hiver, vous allumez un grand feu et nous mangons de la soupe bien chaude.",
                "texte_corr": "Chaque hiver, vous allumiez un grand feu et nous mangions de la soupe bien chaude.",
                "texte_annote": "Chaque hiver, vous <span class='err'>allumez</span> <span class='fix'>allumiez</span> un grand feu et nous <span class='err'>mangons</span> <span class='fix'>mangions</span> de la soupe bien chaude.",
                "explications": [
                    "<strong>allumez &rarr; allumiez :</strong> À l'imparfait (action habituelle du passé), terminaison <em>-iez</em> avec <em>vous</em>.",
                    "<strong>mangons &rarr; mangions :</strong> À l'imparfait avec <em>nous</em>, la terminaison est <em>-ions</em> (le « i » adoucit le g sans besoin de 'e')."
                ],
                "indice": "Demande : « C'est une habitude du passé : conjugue ces deux verbes à l'imparfait ! »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Tu franchit la ligne d'arrivée puis tu applaudit tes camarades courageux.",
                "texte_corr": "Tu franchis la ligne d'arrivée puis tu applaudis tes camarades courageux.",
                "texte_annote": "Tu <span class='err'>franchit</span> <span class='fix'>franchis</span> la ligne d'arrivée puis tu <span class='err'>applaudit</span> <span class='fix'>applaudis</span> tes camarades courageux.",
                "explications": [
                    "<strong>franchit &rarr; franchis :</strong> Au présent avec le pronom <em>tu</em>, la terminaison prend TOUJOURS un <strong>s</strong>.",
                    "<strong>applaudit &rarr; applaudis :</strong> Même règle : avec <em>tu</em>, le verbe prend un <strong>s</strong> final (tu applaudis)."
                ],
                "indice": "Demande : « Quelle est la lettre inséparable du pronom 'tu' dans presque toutes les conjugaisons ? Le S ! »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "À cette époque, ils voyageait toujours en calèche et ils dormait dans de vieilles auberges.",
                "texte_corr": "À cette époque, ils voyageaient toujours en calèche et ils dormaient dans de vieilles auberges.",
                "texte_annote": "À cette époque, ils <span class='err'>voyageait</span> <span class='fix'>voyageaient</span> toujours en calèche et ils <span class='err'>dormait</span> <span class='fix'>dormaient</span> dans de vieilles auberges.",
                "explications": [
                    "<strong>voyageait &rarr; voyageaient :</strong> Le sujet est le pronom pluriel <em>ils</em> : terminaison <em>-aient</em> à l'imparfait.",
                    "<strong>dormait &rarr; dormaient :</strong> Même règle avec le sujet <em>ils</em> : terminaison <em>-aient</em>."
                ],
                "indice": "Demande : « Qui voyageait et dormait ? 'Ils' au pluriel ! Quelle est la terminaison plurielle de l'imparfait ? »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "L'artisan peind la clôture du jardin et il nettoit soigneusement son pinceau.",
                "texte_corr": "L'artisan peint la clôture du jardin et il nettoie soigneusement son pinceau.",
                "texte_annote": "L'artisan <span class='err'>peind</span> <span class='fix'>peint</span> la clôture du jardin et il <span class='err'>nettoit</span> <span class='fix'>nettoie</span> soigneusement son pinceau.",
                "explications": [
                    "<strong>peind &rarr; peint :</strong> Les verbes en <em>-ndre</em> (peindre, craindre, joindre) perdent leur d et prennent un <strong>t</strong> avec <em>il</em> au présent.",
                    "<strong>nettoit &rarr; nettoie :</strong> Verbe du 1er groupe en <em>-oyer</em> : terminaison <strong>-e</strong> avec <em>il</em> au présent (il nettoie)."
                ],
                "indice": "Demande : « Le verbe peindre prend un T avec il. Et nettoyer est un verbe du 1er groupe : quelle est sa terminaison avec il ? »"
            }
        ],
        "vigilance": "Attention aux verbes en <em>-ier</em>, <em>-yer</em> et <em>-gner</em> à l'imparfait : ne pas oublier le 'i' de la terminaison (<em>nous dessinions, vous payiez</em>)."
    },
    {
        "num": 7,
        "theme": "Mission Homophones de Nuance",
        "sous_titre": "Maîtriser leur/leurs, ou/où, la/l'a/là",
        "regle": "Règles d'or pour ne plus jamais hésiter :<br>• <strong>leur / leurs :</strong> Placé devant un <strong>verbe</strong>, <em>leur</em> est un pronom personnel : il est <strong>INVARIABLE</strong> (jamais de 's') ! Placé devant un <strong>nom</strong>, il prend un 's' si le nom est au pluriel (<em>leurs cartables</em>).<br>• <strong>ou / où :</strong> <em>ou</em> sans accent exprime un choix (remplaçable par <em>ou bien</em>). <em>où</em> avec accent indique le lieu ou le temps.<br>• <strong>là / la / l'a :</strong> <em>là</em> avec accent indique un endroit (reste là). <em>l'a</em> vient du verbe avoir (remplaçable par <em>l'avait</em>).",
        "phrases": [
            {
                "id": 1,
                "nb_err": 2,
                "texte_err": "Les élèves écoutent leurs professeur puis ils leurs posent de nombreuses questions.",
                "texte_corr": "Les élèves écoutent leur professeur puis ils leur posent de nombreuses questions.",
                "texte_annote": "Les élèves écoutent <span class='err'>leurs</span> <span class='fix'>leur</span> professeur puis ils <span class='err'>leurs</span> <span class='fix'>leur</span> posent de nombreuses questions.",
                "explications": [
                    "<strong>leurs professeur &rarr; leur professeur :</strong> Le nom <em>professeur</em> est au singulier, donc <em>leur</em> reste au singulier.",
                    "<strong>leurs posent &rarr; leur posent :</strong> Placé devant le verbe <em>posent</em>, <em>leur</em> est invariable (jamais de 's')."
                ],
                "indice": "Demande : « Combien ont-ils de professeurs ? Un seul. Et devant un verbe, est-ce que 'leur' prend un s ? Jamais ! »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Choisis rapidement : préfères-tu une glace où une crêpe, la sur la terrasse ?",
                "texte_corr": "Choisis rapidement : préfères-tu une glace ou une crêpe, là sur la terrasse ?",
                "texte_annote": "Choisis rapidement : préfères-tu une glace <span class='err'>où</span> <span class='fix'>ou</span> une crêpe, <span class='err'>la</span> <span class='fix'>là</span> sur la terrasse ?",
                "explications": [
                    "<strong>où &rarr; ou :</strong> Conjonction exprimant un choix. Test : remplace par « ou bien » (donc pas d'accent).",
                    "<strong>la &rarr; là :</strong> Adverbe de lieu désignant l'endroit où s'asseoir (prend un accent grave)."
                ],
                "indice": "Demande : « Peux-tu dire 'une glace ou bien une crêpe' ? Si oui, pas d'accent ! Et 'là' montre le lieu. »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Cette chanson et magnifique : je la connais bien car maman me l'as apprise hier.",
                "texte_corr": "Cette chanson est magnifique : je la connais bien car maman me l'a apprise hier.",
                "texte_annote": "Cette chanson <span class='err'>et</span> <span class='fix'>est</span> magnifique : je la connais bien car maman me <span class='err'>l'as</span> <span class='fix'>l'a</span> apprise hier.",
                "explications": [
                    "<strong>et &rarr; est :</strong> Verbe être. Test : « cette chanson <em>était</em> magnifique ».",
                    "<strong>l'as &rarr; l'a :</strong> Verbe avoir avec le sujet <em>maman</em> (elle). Test : « maman me <em>l'avait</em> apprise » (3e pers., donc sans s)."
                ],
                "indice": "Demande : « Remplace par 'était' au début. Et qui a appris la chanson ? Maman (donc elle l'a, sans s). »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Les randonneurs ont préparé leur sacs et le guide leurs indique le bon sentier.",
                "texte_corr": "Les randonneurs ont préparé leurs sacs et le guide leur indique le bon sentier.",
                "texte_annote": "Les randonneurs ont préparé <span class='err'>leur</span> <span class='fix'>leurs</span> sacs et le guide <span class='err'>leurs</span> <span class='fix'>leur</span> indique le bon sentier.",
                "explications": [
                    "<strong>leur sacs &rarr; leurs sacs :</strong> Le nom <em>sacs</em> est au pluriel, donc le déterminant prend un <strong>s</strong>.",
                    "<strong>leurs indique &rarr; leur indique :</strong> Devant le verbe <em>indique</em>, <em>leur</em> est un pronom invariable."
                ],
                "indice": "Demande : « 'Sacs' est au pluriel. Mais que fait 'leur' devant le verbe 'indique' ? Il ne prend jamais de s ! »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "Regarde la-bas dans le pré : le village ou nous allons se trouve juste derrière.",
                "texte_corr": "Regarde là-bas dans le pré : le village où nous allons se trouve juste derrière.",
                "texte_annote": "Regarde <span class='err'>la-bas</span> <span class='fix'>là-bas</span> dans le pré : le village <span class='err'>ou</span> <span class='fix'>où</span> nous allons se trouve juste derrière.",
                "explications": [
                    "<strong>la-bas &rarr; là-bas :</strong> Expression de lieu, prend un accent grave sur le <em>à</em>.",
                    "<strong>ou &rarr; où :</strong> Pronom relatif de lieu (« le village dans lequel »). Il prend un accent grave."
                ],
                "indice": "Demande : « Ces deux mots parlent-ils d'un endroit ? Oui, donc ils prennent tous les deux un accent grave ! »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Les musiciens accordent leur violons et le chef d'orchestre leurs fait signe de jouer.",
                "texte_corr": "Les musiciens accordent leurs violons et le chef d'orchestre leur fait signe de jouer.",
                "texte_annote": "Les musiciens accordent <span class='err'>leur</span> <span class='fix'>leurs</span> violons et le chef d'orchestre <span class='err'>leurs</span> <span class='fix'>leur</span> fait signe de jouer.",
                "explications": [
                    "<strong>leur violons &rarr; leurs violons :</strong> Nom au pluriel (<em>violons</em>), donc déterminant possessif avec un <strong>s</strong>.",
                    "<strong>leurs fait &rarr; leur fait :</strong> Devant le verbe <em>fait</em>, <em>leur</em> est pronom et reste invariable."
                ],
                "indice": "Demande : « Repère le nom et le verbe : accorde devant le nom au pluriel, n'accorde jamais devant le verbe ! »"
            }
        ],
        "vigilance": "Règle absolue à marteler : devant un VERBE, <em>leur</em> ne prend JAMAIS de « s » (ex: <em>je leur parle, ils leur donnent</em>)."
    },
    {
        "num": 8,
        "theme": "Grand Défi de Synthèse",
        "sous_titre": "La grande finale des maîtres détectives de l'orthographe",
        "regle": "Tu es arrivé au sommet ! Pour cette ultime mission, combine toutes tes compétences de détective :<br>1. <strong>Trouve le sujet</strong> de chaque verbe (qui fait l'action ?).<br>2. <strong>Vérifie la chaîne d'accord</strong> dans chaque groupe nominal.<br>3. <strong>Applique les tests magiques</strong> pour les homophones (avait, était, mon, mordu, mordre).",
        "phrases": [
            {
                "id": 1,
                "nb_err": 2,
                "texte_err": "Dans la clairière enneigé se sont rassembler plusieurs biches craintives.",
                "texte_corr": "Dans la clairière enneigée se sont rassemblées plusieurs biches craintives.",
                "texte_annote": "Dans la clairière <span class='err'>enneigé</span> <span class='fix'>enneigée</span> se sont <span class='err'>rassembler</span> <span class='fix'>rassemblées</span> plusieurs biches craintives.",
                "explications": [
                    "<strong>enneigé &rarr; enneigée :</strong> Accord de l'adjectif avec le nom féminin singulier <em>la clairière</em>.",
                    "<strong>rassembler &rarr; rassemblées :</strong> Participe passé employé avec <em>être</em> (se sont). Le sujet inversé est « plusieurs biches craintives » (féminin pluriel)."
                ],
                "indice": "Demande : « Avec qui s'accorde enneigée ? Et qui s'est rassemblé ? Accord avec l'auxiliaire être ! »"
            },
            {
                "id": 2,
                "nb_err": 2,
                "texte_err": "Ces jeunes explorateurs on découvert une grotte secrète dont l'entrée et masquée par la mousse.",
                "texte_corr": "Ces jeunes explorateurs ont découvert une grotte secrète dont l'entrée est masquée par la mousse.",
                "texte_annote": "Ces jeunes explorateurs <span class='err'>on</span> <span class='fix'>ont</span> découvert une grotte secrète dont l'entrée <span class='err'>et</span> <span class='fix'>est</span> masquée par la mousse.",
                "explications": [
                    "<strong>on &rarr; ont :</strong> Verbe avoir au passé composé. Test : « ils <em>avaient</em> découvert ».",
                    "<strong>et &rarr; est :</strong> Verbe être. Test : « dont l'entrée <em>était</em> masquée »."
                ],
                "indice": "Demande : « Remplace par 'avaient' puis par 'était'. Quels sont les deux verbes ? »"
            },
            {
                "id": 3,
                "nb_err": 2,
                "texte_err": "Les oiseaux migrateurs c'élancent vers le sud et leurs voyage durera plusieurs semaines.",
                "texte_corr": "Les oiseaux migrateurs s'élancent vers le sud et leur voyage durera plusieurs semaines.",
                "texte_annote": "Les oiseaux migrateurs <span class='err'>c'élancent</span> <span class='fix'>s'élancent</span> vers le sud et <span class='err'>leurs</span> <span class='fix'>leur</span> voyage durera plusieurs semaines.",
                "explications": [
                    "<strong>c'élancent &rarr; s'élancent :</strong> Verbe pronominal (s'élancer).",
                    "<strong>leurs voyage &rarr; leur voyage :</strong> Le nom <em>voyage</em> est au singulier, donc <em>leur</em> reste au singulier."
                ],
                "indice": "Demande : « S'élancer est un verbe pronominal avec S. Et regarde le mot voyage : est-il singulier ou pluriel ? »"
            },
            {
                "id": 4,
                "nb_err": 2,
                "texte_err": "Après avoir franchis la ligne d'arrivée, les coureurs épuisé se sont écroulés sur la pelouse.",
                "texte_corr": "Après avoir franchi la ligne d'arrivée, les coureurs épuisés se sont écroulés sur la pelouse.",
                "texte_annote": "Après avoir <span class='err'>franchis</span> <span class='fix'>franchi</span> la ligne d'arrivée, les coureurs <span class='err'>épuisé</span> <span class='fix'>épuisés</span> se sont écroulés sur la pelouse.",
                "explications": [
                    "<strong>franchis &rarr; franchi :</strong> Participe passé employé avec <em>avoir</em> sans COD placé avant (après avoir <em>mordu</em>, pas d'accord).",
                    "<strong>épuisé &rarr; épuisés :</strong> Adjectif qualificatif accordé au masculin pluriel avec <em>les coureurs</em>."
                ],
                "indice": "Demande : « Qui est épuisé ? Les coureurs. Et avec 'avoir franchi', y a-t-il un accord ? Non ! »"
            },
            {
                "id": 5,
                "nb_err": 2,
                "texte_err": "La directrice leurs à remis une belle médaille pour récompenser leurs efforts constants.",
                "texte_corr": "La directrice leur a remis une belle médaille pour récompenser leurs efforts constants.",
                "texte_annote": "La directrice <span class='err'>leurs</span> <span class='fix'>leur</span> <span class='err'>à</span> <span class='fix'>a</span> remis une belle médaille pour récompenser leurs efforts constants.",
                "explications": [
                    "<strong>leurs &rarr; leur :</strong> Placé devant le verbe <em>a remis</em>, <em>leur</em> est invariable (jamais de 's').",
                    "<strong>à &rarr; a :</strong> Verbe avoir au passé composé. Test : « elle <em>avait</em> remis »."
                ],
                "indice": "Demande : « 'Leur' est devant un verbe. Prend-il un s ? Et peut-on dire 'avait remis' ? »"
            },
            {
                "id": 6,
                "nb_err": 2,
                "texte_err": "Pendant que vous chantiez cette douce mélodie, les spectateurs ému vous ont applaudir avec joie.",
                "texte_corr": "Pendant que vous chantiez cette douce mélodie, les spectateurs émus vous ont applaudi avec joie.",
                "texte_annote": "Pendant que vous chantiez cette douce mélodie, les spectateurs <span class='err'>ému</span> <span class='fix'>émus</span> vous ont <span class='err'>applaudir</span> <span class='fix'>applaudi</span> avec joie.",
                "explications": [
                    "<strong>ému &rarr; émus :</strong> Adjectif s'accordant au masculin pluriel avec <em>les spectateurs</em>.",
                    "<strong>applaudir &rarr; applaudi :</strong> Participe passé avec l'auxiliaire avoir (ils ont <em>mordu</em>, pas ils ont mordre)."
                ],
                "indice": "Demande : « Qui est ému ? Les spectateurs. Et dit-on 'ont mordu' ou 'ont mordre' ? »"
            }
        ],
        "vigilance": "Félicitez chaudement l'enfant ! Il a su mobiliser l'ensemble des règles fondamentales du cycle 3."
    }
]

CSS_COMMUN = """
@page {
  size: 210mm 297mm;
  margin: 0;
}
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: #1e293b;
  background: #f8fafc;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.page {
  width: 210mm;
  height: 297mm;
  max-height: 297mm;
  padding: 10mm 13mm;
  background: #ffffff;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  position: relative;
}
"""

def generer_carnet_eleve_html():
    pages_html = []

    # ==================== PAGE 1 : COUVERTURE ÉLÈVE ====================
    page1 = f"""
    <div class="page" style="background: linear-gradient(145deg, #f0f7ff 0%, #ffffff 40%, #fdf8f6 100%);">
      <div style="border: 3px double #2563eb; border-radius: 16px; height: 100%; padding: 12mm 10mm; display: flex; flex-direction: column; justify-content: space-between; text-align: center; background: white; box-shadow: 0 4px 20px rgba(37,99,235,0.06);">
        
        <!-- Header Décoratif -->
        <div>
          <div style="display: inline-flex; align-items: center; gap: 8px; background: #dbeafe; color: #1e40af; padding: 4px 14px; border-radius: 20px; font-size: 10pt; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">
            <span>🔍</span> Cycle 3 • Niveau CM2
          </div>
          <h1 style="font-size: 26pt; color: #0f172a; margin-top: 10px; font-weight: 800; line-height: 1.15; letter-spacing: -0.5px;">
            LE CARNET DU DÉTECTIF<br>
            <span style="color: #2563eb; font-size: 24pt;">DE L'ORTHOGRAPHE</span>
          </h1>
          <p style="font-size: 11pt; color: #64748b; margin-top: 6px; font-weight: 500;">
            8 semaines de défis quotidiens pour débusquer les pièges de la langue française
          </p>
        </div>

        <!-- Illustration Centrale Insigne SVG -->
        <div style="margin: 8px auto;">
          <svg width="90" height="90" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="46" fill="#eff6ff" stroke="#3b82f6" stroke-width="4"/>
            <circle cx="44" cy="44" r="22" stroke="#1d4ed8" stroke-width="5" fill="#ffffff"/>
            <line x1="60" y1="60" x2="80" y2="80" stroke="#1d4ed8" stroke-width="7" stroke-linecap="round"/>
            <path d="M44 32 L44 56 M32 44 L56 44" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
            <circle cx="44" cy="44" r="6" fill="#f59e0b"/>
          </svg>
        </div>

        <!-- Cartouche Élève -->
        <div style="background: #f8fafc; border: 2px dashed #94a3b8; border-radius: 12px; padding: 10px 16px; margin: 0 auto; width: 90%; text-align: left;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 9.5pt;">
            <div><strong>Prénom de l'enquêteur :</strong> <span style="border-bottom: 1.5px dotted #64748b; display: inline-block; width: 55%;">&nbsp;</span></div>
            <div><strong>Nom de famille :</strong> <span style="border-bottom: 1.5px dotted #64748b; display: inline-block; width: 60%;">&nbsp;</span></div>
            <div><strong>Classe :</strong> <span style="color: #2563eb; font-weight: bold;">CM2</span> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>École :</strong> <span style="border-bottom: 1.5px dotted #64748b; display: inline-block; width: 50%;">&nbsp;</span></div>
            <div><strong>Année scolaire :</strong> 2024 - 2025</div>
          </div>
        </div>

        <!-- Le Serment du Détective -->
        <div style="background: #fffbeb; border: 1.5px solid #fde68a; border-radius: 12px; padding: 10px 14px; text-align: left;">
          <h3 style="color: #b45309; font-size: 10pt; font-weight: 700; margin-bottom: 4px; display: flex; align-items: center; gap: 6px;">
            <span>📜</span> Le Serment du Détective Orthographe :
          </h3>
          <p style="font-size: 8.5pt; color: #78350f; line-height: 1.35;">
            1. Je lis chaque phrase lentement en cherchant les mots suspects.<br>
            2. Je trouve le verbe conjugué et je lui demande : <em>« Qui est-ce qui ? »</em> pour repérer son sujet.<br>
            3. Dans chaque groupe de mots, je vérifie l'accord entre le déterminant, le nom et l'adjectif.<br>
            4. J'utilise mes astuces magiques (<em>avait, étaient, mordu, mordre</em>) pour démasquer les pièges !
          </p>
        </div>

        <!-- Tableau de Bord des 8 Missions -->
        <div>
          <h4 style="font-size: 9pt; color: #334155; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px;">
            🗺️ Tableau de bord de tes 8 enquêtes (Coche chaque mission accomplie) :
          </h4>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
            {"".join([f'''
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 6px 4px; font-size: 7.5pt; text-align: center;">
              <div style="font-weight: 700; color: #1e40af;">Semaine {s['num']}</div>
              <div style="color: #64748b; font-size: 6.8pt; margin: 2px 0;">{s['theme'].replace("Mission ", "")}</div>
              <div style="font-size: 9pt; color: #cbd5e1;">⭐ ▢</div>
            </div>''' for s in DATA_SEMAINES])}
          </div>
        </div>

        <div style="font-size: 7.5pt; color: #94a3b8; border-top: 1px solid #f1f5f9; padding-top: 4px;">
          Carnet d'apprentissage CM2 • Réalisé pour un entraînement quotidien de qualité • 48 phrases d'entraînement
        </div>

      </div>
    </div>
    """
    pages_html.append(page1)

    # ==================== PAGES 2 À 9 : LES 8 SEMAINES ÉLÈVE ====================
    for sem in DATA_SEMAINES:
        phrases_html = []
        for p in sem["phrases"]:
            p_html = f"""
            <div class="phrase-card">
              <div class="phrase-head">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span class="phrase-badge">PHRASE {p['id']}</span>
                  <span class="badge-err">🕵️ {p['nb_err']} erreurs à trouver</span>
                </div>
                <div class="stars-eval">
                  <span style="color:#f59e0b;">★ ★ ★</span>
                  <span class="check-box">Vu : ▢</span>
                </div>
              </div>
              <div class="phrase-source">
                « {p['texte_err']} »
              </div>
              <!-- Zone d'écriture avec lignage Seyes 2 lignes -->
              <div class="writing-area">
                <div class="seyes-line"></div>
                <div class="seyes-line"></div>
              </div>
            </div>
            """
            phrases_html.append(p_html)

        total_err = sum(p["nb_err"] for p in sem["phrases"])

        page_sem = f"""
        <div class="page">
          
          <!-- En-tête Semaine -->
          <div class="sem-header">
            <div>
              <div class="mission-tag">SEMAINE {sem['num']} • {sem['theme'].upper()}</div>
              <h2 class="mission-title">{sem['sous_titre']}</h2>
            </div>
            <div class="student-meta">
              <div><strong>Détective :</strong> _________________</div>
              <div style="margin-top: 3px;"><strong>Semaine du :</strong> _____________</div>
            </div>
          </div>

          <!-- Règle de la Loupe -->
          <div class="loupe-box">
            <span class="loupe-icon">🔍</span>
            <div style="font-size: 8.2pt; line-height: 1.35; color: #1e3a8a;">
              <strong>La loupe du détective :</strong> {sem['regle']}
            </div>
          </div>

          <!-- 6 Phrases -->
          <div class="phrases-container">
            {"".join(phrases_html)}
          </div>

          <!-- Bilan Hebdomadaire -->
          <div class="bilan-box">
            <div style="font-size: 8.5pt;">
              <strong>🎯 Bilan mission {sem['num']} :</strong>
              <span style="margin-left: 8px;">Erreurs démasquées : <strong>___ / {total_err}</strong></span>
            </div>
            <div style="font-size: 8pt; display: flex; gap: 8px; color: #475569;">
              <span>▢ Apprenti 🔎</span>
              <span>▢ Confirmé 🎖️</span>
              <span>▢ Maître Détective 🏆</span>
            </div>
            <div style="font-size: 8pt;">
              <strong>Visa adulte :</strong> _________________
            </div>
          </div>

        </div>
        """
        pages_html.append(page_sem)

    # ==================== PAGE 10 : DIPLÔME ET MÉMO FINAL ====================
    page10 = f"""
    <div class="page" style="background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);">
      
      <!-- Diplôme Officiel -->
      <div style="border: 4px double #d97706; border-radius: 16px; padding: 10mm 10mm; background: #ffffff; box-shadow: 0 4px 20px rgba(180,83,9,0.08); text-align: center; position: relative;">
        <div style="font-size: 9pt; font-weight: 800; color: #d97706; text-transform: uppercase; letter-spacing: 2px;">RÉPUBLIQUE DE L'ORTHOGRAPHE ET DU FRANÇAIS</div>
        <h2 style="font-size: 22pt; color: #78350f; font-weight: 800; margin: 4px 0 2px 0;">DIPLÔME OFFICIEL</h2>
        <div style="font-size: 11.5pt; color: #b45309; font-weight: 700;">de Grand Maître Détective de la Langue Française</div>
        
        <p style="font-size: 9.5pt; color: #475569; margin: 8px auto 6px auto; max-width: 90%; line-height: 1.35;">
          Décerné solennellement et avec les félicitations du jury à l'élève :
        </p>
        <div style="font-size: 16pt; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #3b82f6; width: 65%; margin: 0 auto 6px auto; padding-bottom: 2px;">
          &nbsp;
        </div>
        <p style="font-size: 9pt; color: #475569; line-height: 1.35; margin-bottom: 8px;">
          pour avoir traqué avec perspicacité, rigueur et persévérance les pièges des <strong>48 phrases d'entraînement</strong> du CM2 au cours des 8 semaines de défis !
        </p>

        <div style="display: flex; justify-content: space-around; align-items: flex-end; margin-top: 12px; font-size: 8.5pt; color: #334155;">
          <div>
            <div>Date d'obtention :</div>
            <div style="border-bottom: 1.5px dotted #94a3b8; width: 110px; margin: 4px auto 0 auto;">&nbsp;</div>
          </div>
          <div>
            <div style="display: inline-block; width: 48px; height: 48px; border-radius: 50%; border: 2.5px solid #f59e0b; background: #fffbeb; color: #d97706; font-size: 22pt; line-height: 44px; box-shadow: 0 2px 8px rgba(245,158,11,0.25);">🏆</div>
            <div style="font-size: 7.5pt; font-weight: 800; color: #b45309; margin-top: 3px; letter-spacing: 0.5px;">SCEAU OFFICIEL</div>
          </div>
          <div>
            <div>Signature des parents / maître :</div>
            <div style="border-bottom: 1.5px dotted #94a3b8; width: 140px; margin: 4px auto 0 auto;">&nbsp;</div>
          </div>
        </div>
      </div>

      <!-- Le Mémo des 8 Astuces Magiques -->
      <div style="margin-top: 8px; background: white; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 10px 14px;">
        <h3 style="font-size: 10.5pt; color: #1e40af; font-weight: 800; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
          <span>🧠</span> Le Carnet Secret des 8 Astuces d'Or (À conserver précieusement pour la 6ème !) :
        </h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 7.8pt; color: #334155; line-height: 1.35;">
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>1. Groupe Nominal :</strong> L'adjectif s'accorde TOUJOURS avec le nom chef (genre + nombre). Pense aux pluriels en <em>-aux</em> et <em>-x</em>.
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>2. a / à, on / ont :</strong> Remplace par le passé : <em>avait</em> (donc <strong>a</strong> sans accent) et <em>avaient</em> (donc <strong>ont</strong> avec un t).
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>3. Accord Sujet-Verbe :</strong> Pose la question : <em>« Qui est-ce qui ? »</em>. Attention au pronom placé devant le verbe (<em>il les mange</em>) !
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>4. -é ou -er :</strong> Remplace par <em>mordu</em> (participe en <strong>-é</strong>) ou par <em>mordre</em> (infinitif en <strong>-er</strong>).
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>5. ce / se &amp; ces / ses :</strong> <strong>se</strong> pour une action sur soi (<em>se laver</em>). <strong>ces</strong> pour montrer, <strong>ses</strong> pour ce qui lui appartient.
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>6. Présent &amp; Imparfait :</strong> Au présent, <em>tu</em> prend toujours un <strong>s</strong>. À l'imparfait, les terminaisons sont <em>-ais, -ais, -ait, -ions, -iez, -aient</em>.
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>7. leur / leurs :</strong> Devant un <strong>verbe</strong>, <em>leur</em> est invariable (JAMAIS de s). Devant un nom au pluriel, il prend un <strong>s</strong>.
          </div>
          <div style="background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid #3b82f6;">
            <strong>8. ou / où :</strong> <strong>ou</strong> = <em>ou bien</em> (choix). <strong>où</strong> avec accent = l'endroit (lieu).
          </div>
        </div>
      </div>

      <div style="text-align: center; font-size: 8pt; color: #94a3b8;">
        Bravo pour ton investissement ! L'orthographe est un super-pouvoir qui t'accompagnera toute ta vie.
      </div>

    </div>
    """
    pages_html.append(page10)

    css_eleve = CSS_COMMUN + """
    .sem-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #2563eb;
      padding-bottom: 4px;
    }
    .mission-tag {
      font-size: 8.2pt;
      font-weight: 800;
      color: #2563eb;
      letter-spacing: 0.5px;
    }
    .mission-title {
      font-size: 13.5pt;
      color: #0f172a;
      font-weight: 700;
      margin-top: 1px;
    }
    .student-meta {
      font-size: 8.2pt;
      color: #475569;
      text-align: right;
    }
    .loupe-box {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-left: 4px solid #2563eb;
      border-radius: 6px;
      padding: 5px 10px;
      margin: 5px 0 6px 0;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .loupe-icon {
      font-size: 15pt;
    }
    .phrases-container {
      display: flex;
      flex-direction: column;
      gap: 7px;
    }
    .phrase-card {
      border: 1px solid #e2e8f0;
      border-radius: 7px;
      padding: 5px 10px 4px 10px;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 3px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .phrase-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 8pt;
    }
    .phrase-badge {
      background: #1e40af;
      color: white;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 7.2pt;
      letter-spacing: 0.5px;
    }
    .badge-err {
      background: #fef2f2;
      color: #b91c1c;
      border: 1px solid #fecaca;
      border-radius: 12px;
      padding: 2px 8px;
      font-size: 7.2pt;
      font-weight: 700;
    }
    .stars-eval {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 9pt;
    }
    .check-box {
      font-size: 7.5pt;
      color: #64748b;
    }
    .phrase-source {
      font-size: 9.6pt;
      color: #1e293b;
      background: #f8fafc;
      padding: 4px 8px;
      border-radius: 4px;
      font-family: Georgia, serif;
      font-style: italic;
      border-left: 3px solid #94a3b8;
      line-height: 1.35;
    }
    .writing-area {
      margin-top: 2px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    /* Lignage Seyes écolier 2 lignes par phrase avec hauteur 22px */
    .seyes-line {
      height: 22px;
      border-left: 2px solid #f87171;
      margin-left: 2px;
      background-image: 
        linear-gradient(to bottom, transparent 20px, #6366f1 21px),
        linear-gradient(to bottom, #f8fafc 0px, transparent 1px, transparent 4px, #c7d2fe 5px, transparent 6px, transparent 9px, #c7d2fe 10px, transparent 11px, transparent 14px, #c7d2fe 15px);
      background-size: 100% 22px;
      background-repeat: no-repeat;
    }
    .bilan-box {
      border-top: 1.5px dashed #94a3b8;
      padding-top: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 8.2pt;
      background: #f8fafc;
      padding: 5px 10px;
      border-radius: 5px;
      border: 1px dashed #cbd5e1;
      margin-top: 3px;
    }
    """

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Carnet du Détective de l'Orthographe - CM2</title>
<style>
{css_eleve}
</style>
</head>
<body>
{"".join(pages_html)}
</body>
</html>
"""

def generer_correctif_parents_html():
    pages_html = []

    # ==================== PAGE 1 : GUIDE DES PARENTS ====================
    page1 = f"""
    <div class="page" style="background: linear-gradient(145deg, #f0fdf4 0%, #ffffff 50%, #eff6ff 100%);">
      <div style="border: 3px double #16a34a; border-radius: 16px; height: 100%; padding: 10mm 10mm; display: flex; flex-direction: column; justify-content: space-between; background: white; box-shadow: 0 4px 20px rgba(22,163,74,0.06);">
        
        <!-- Header Parents -->
        <div style="text-align: center;">
          <div style="display: inline-flex; align-items: center; gap: 8px; background: #dcfce7; color: #15803d; padding: 4px 14px; border-radius: 20px; font-size: 10pt; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">
            <span>👨‍👩‍👧‍👦</span> Espace Parents &amp; Enseignants • CM2
          </div>
          <h1 style="font-size: 24pt; color: #0f172a; margin-top: 10px; font-weight: 800; line-height: 1.15;">
            LE GUIDE DU PARENT ENQUÊTEUR<br>
            <span style="color: #16a34a; font-size: 22pt;">CORRECTIF COMPLET &amp; MÉTHODE</span>
          </h1>
          <p style="font-size: 10.5pt; color: #64748b; margin-top: 4px;">
            Les 48 phrases corrigées pas à pas, les règles expliquées simplement et les indices à souffler
          </p>
        </div>

        <!-- Les 4 Piliers de l'Accompagnement Bienveillant -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 4px 0;">
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #16a34a; border-radius: 8px; padding: 8px 10px;">
            <div style="font-weight: 700; color: #166534; font-size: 9pt; margin-bottom: 2px;">1. Laisser chercher en autonomie</div>
            <p style="font-size: 8pt; color: #475569; line-height: 1.3;">
              Laissez votre enfant lire la phrase et chercher seul les erreurs. Le badge lui indique combien d'erreurs sont dissimulées pour le guider sans le bloquer.
            </p>
          </div>
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #2563eb; border-radius: 8px; padding: 8px 10px;">
            <div style="font-weight: 700; color: #1e40af; font-size: 9pt; margin-bottom: 2px;">2. Poser la bonne question</div>
            <p style="font-size: 8pt; color: #475569; line-height: 1.3;">
              S'il hésite, ne donnez pas la réponse : utilisez <em>« L'indice à lui souffler »</em> mentionné sous chaque phrase du guide pour qu'il trouve par lui-même.
            </p>
          </div>
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #f59e0b; border-radius: 8px; padding: 8px 10px;">
            <div style="font-weight: 700; color: #b45309; font-size: 9pt; margin-bottom: 2px;">3. Utiliser les astuces orales</div>
            <p style="font-size: 8pt; color: #475569; line-height: 1.3;">
              Faites-lui tester à voix haute les substitutions : « Est-ce qu'on peut dire <em>avait</em> ? », « Est-ce qu'on dit <em>mordu</em> ou <em>mordre</em> ? ».
            </p>
          </div>
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #8b5cf6; border-radius: 8px; padding: 8px 10px;">
            <div style="font-weight: 700; color: #6d28d9; font-size: 9pt; margin-bottom: 2px;">4. Valoriser la justification</div>
            <p style="font-size: 8pt; color: #475569; line-height: 1.3;">
              Demandez-lui : <em>« Pourquoi as-tu mis un -s ici ? »</em>. Formuler la règle à l'oral est le meilleur moyen d'ancrer durablement la compétence.
            </p>
          </div>
        </div>

        <!-- Sommaire du Programme des 8 Semaines -->
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 8px 12px;">
          <h3 style="font-size: 9.5pt; color: #1e293b; font-weight: 700; margin-bottom: 6px;">
            📋 Programme synthétique des 8 semaines d'enquêtes :
          </h3>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 14px; font-size: 7.8pt;">
            {"".join([f'''
            <div style="display: flex; gap: 6px; align-items: baseline;">
              <span style="font-weight: bold; color: #16a34a;">Semaine {s['num']} :</span>
              <span style="color: #334155;">{s['sous_titre']}</span>
            </div>''' for s in DATA_SEMAINES])}
          </div>
        </div>

        <div style="font-size: 8pt; color: #64748b; text-align: center; border-top: 1px solid #f1f5f9; padding-top: 4px;">
          Une pratique de 5 à 10 minutes par jour (1 phrase quotidienne) suffit pour transformer la rigueur orthographique de votre enfant !
        </div>

      </div>
    </div>
    """
    pages_html.append(page1)

    # ==================== PAGES 2 À 9 : LES 8 SEMAINES PARENTS ====================
    for sem in DATA_SEMAINES:
        phrases_html = []
        for p in sem["phrases"]:
            explications_html = "".join([f"<li>{exp}</li>" for exp in p["explications"]])
            p_html = f"""
            <div class="corr-card">
              <div class="corr-head">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span class="badge-num">PHRASE {p['id']}</span>
                  <span style="font-size: 7.2pt; color: #64748b;">({p['nb_err']} pièges ciblés)</span>
                </div>
                <div style="font-size: 7.2pt; color: #15803d; font-weight: 600;">
                  ✔ Correction complète
                </div>
              </div>

              <!-- Ligne Erreurs barrées -->
              <div class="line-annotated">
                <strong>Texte repéré :</strong> {p['texte_annote']}
              </div>

              <!-- Ligne Corrigée Propre -->
              <div class="line-clean">
                <strong>Phrase juste :</strong> « {p['texte_corr']} »
              </div>

              <!-- Explications Pédagogiques -->
              <div class="exp-block">
                <ul class="exp-list">
                  {explications_html}
                </ul>
                <div class="indice-box">
                  <strong>💡 L'indice à lui souffler s'il hésite :</strong> {p['indice']}
                </div>
              </div>
            </div>
            """
            phrases_html.append(p_html)

        page_sem = f"""
        <div class="page">
          
          <!-- En-tête Semaine Correctif -->
          <div class="corr-header">
            <div>
              <div style="font-size: 7.8pt; font-weight: 800; color: #16a34a; letter-spacing: 0.5px;">CORRECTIF OFFICIEL • SEMAINE {sem['num']}</div>
              <h2 style="font-size: 13pt; color: #0f172a; font-weight: 700; margin-top: 1px;">{sem['theme']} : {sem['sous_titre']}</h2>
            </div>
            <div style="background: #dcfce7; color: #166534; font-size: 7.5pt; font-weight: 700; padding: 3px 8px; border-radius: 12px;">
              6 PHRASES DÉCORTIQUÉES
            </div>
          </div>

          <!-- 6 Fiches Correctives -->
          <div class="corr-phrases-container">
            {"".join(phrases_html)}
          </div>

          <!-- Encadré Vigilance Parentale -->
          <div class="vigilance-box">
            <span style="font-size: 11pt;">⚠️</span>
            <div style="font-size: 7.6pt; color: #854d0e; line-height: 1.3;">
              <strong>Point vigilance pour le parent :</strong> {sem['vigilance']}
            </div>
          </div>

        </div>
        """
        pages_html.append(page_sem)

    # ==================== PAGE 10 : SUIVI ET LEXIQUE PARENTS ====================
    page10_parents = f"""
    <div class="page" style="background: #ffffff;">
      
      <div style="border-bottom: 2px solid #16a34a; padding-bottom: 4px; margin-bottom: 8px;">
        <h2 style="font-size: 15pt; color: #0f172a; font-weight: 800;">TABLEAU DE BORD DU SUIVI &amp; LEXIQUE CM2</h2>
        <p style="font-size: 8.8pt; color: #64748b;">Outil de suivi sur les 8 semaines, barème d'encouragement et rappel des notions clés</p>
      </div>

      <!-- Grille d'encouragement -->
      <div style="background: #ecfdf5; border: 1.5px solid #a7f3d0; border-radius: 8px; padding: 6px 12px; margin-bottom: 8px; display: flex; justify-content: space-around; align-items: center; font-size: 8pt; color: #065f46;">
        <div><strong>⭐ 1 étoile :</strong> 1 erreur débusquée (bon début d'observation)</div>
        <div><strong>⭐⭐ 2 étoiles :</strong> 2 erreurs débusquées (enquêteur appliqué)</div>
        <div><strong>⭐⭐⭐ 3 étoiles :</strong> Phrase entièrement corrigée avec justification !</div>
      </div>

      <!-- Grille de Suivi Hebdomadaire -->
      <table style="width: 100%; border-collapse: collapse; font-size: 8pt; margin-bottom: 8px;">
        <thead>
          <tr style="background: #f1f5f9; color: #1e293b; text-align: left;">
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 14%;">Semaine</th>
            <th style="padding: 6px; border: 1px solid #cbd5e1;">Thématique travaillée</th>
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 15%;">Score fautes</th>
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 18%;">Autonomie</th>
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 22%;">Commentaire parent</th>
          </tr>
        </thead>
        <tbody>
          {"".join([f'''
          <tr style="background: {"#ffffff" if s["num"] % 2 == 1 else "#f8fafc"};">
            <td style="padding: 5px 6px; border: 1px solid #cbd5e1; font-weight: bold; color: #1e40af;">Semaine {s['num']}</td>
            <td style="padding: 5px 6px; border: 1px solid #cbd5e1;">{s['theme'].replace("Mission ", "")}</td>
            <td style="padding: 5px 6px; border: 1px solid #cbd5e1;">___ / {sum(p["nb_err"] for p in s["phrases"])}</td>
            <td style="padding: 5px 6px; border: 1px solid #cbd5e1;">▢ Seul &nbsp; ▢ Guidé</td>
            <td style="padding: 5px 6px; border: 1px solid #cbd5e1;">&nbsp;</td>
          </tr>''' for s in DATA_SEMAINES])}
        </tbody>
      </table>

      <!-- Lexique Express pour les Parents -->
      <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 8px 12px; flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
        <h3 style="font-size: 9.8pt; color: #15803d; font-weight: 700; margin-bottom: 4px;">
          📚 Petit lexique grammatical pour parents (Sans jargon) :
        </h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 7.7pt; color: #334155; line-height: 1.35;">
          <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #1e40af;">Groupe Nominal (GN) :</strong> Ensemble de mots constitué d'un nom principal (le chef), d'un déterminant et souvent d'adjectifs. Tous s'accordent en bloc !
          </div>
          <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #1e40af;">Homophone grammatical :</strong> Mots qui se prononcent de la même façon mais s'écrivent différemment (a/à, son/sont, et/est). La substitution permet de trancher.
          </div>
          <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #1e40af;">Pronom écran / complément :</strong> Petit mot (<em>les, la, lui, leur</em>) placé devant le verbe. Piège fréquent : les enfants accordent avec ce mot alors qu'il n'est pas le sujet !
          </div>
          <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #1e40af;">Participe passé vs Infinitif :</strong> <em>-é</em> (passé) ou <em>-er</em> (infinitif). L'astuce consiste à remplacer par un verbe du 3e groupe comme <em>mordre / mordu</em> ou <em>vendre / vendu</em>.
          </div>
          <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #1e40af;">Sujet inversé :</strong> Le sujet est placé après le verbe (très fréquent après un complément de lieu : <em>« Dans le ciel brillent les étoiles »</em>).
          </div>
          <div style="background: white; padding: 6px 10px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong style="color: #1e40af;">Leur invariable vs Leurs :</strong> Devant un <strong>verbe</strong>, <em>leur</em> est toujours invariable (<em>« je leur dis »</em>). Devant un nom, il prend un 's' si le nom est pluriel.
          </div>
        </div>
        <div style="font-size: 7.5pt; color: #94a3b8; text-align: center; margin-top: 4px;">
          En félicitant chaque démarche de réflexion, vous développez l'assurance et le plaisir d'écrire chez votre enfant.
        </div>
      </div>

    </div>
    """

    pages_html.append(page10_parents)

    css_parents = CSS_COMMUN + """
    .corr-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #16a34a;
      padding-bottom: 4px;
    }
    .corr-phrases-container {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 5px;
    }
    .corr-card {
      border: 1px solid #e2e8f0;
      border-radius: 7px;
      padding: 5px 10px;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      gap: 3px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .corr-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 7.8pt;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 2px;
    }
    .badge-num {
      background: #166534;
      color: white;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 7.2pt;
      letter-spacing: 0.5px;
    }
    .line-annotated {
      font-size: 8.2pt;
      color: #334155;
      background: #fff1f2;
      border-left: 3px solid #e11d48;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .line-annotated .err {
      text-decoration: line-through;
      color: #be123c;
      font-weight: bold;
    }
    .line-annotated .fix {
      color: #15803d;
      font-weight: bold;
      background: #dcfce7;
      padding: 0 4px;
      border-radius: 3px;
      margin-left: 2px;
    }
    .line-clean {
      font-size: 8.4pt;
      color: #166534;
      background: #f0fdf4;
      border-left: 3px solid #16a34a;
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 600;
    }
    .exp-block {
      background: #f8fafc;
      border-radius: 5px;
      padding: 3px 8px;
    }
    .exp-list {
      margin-left: 16px;
      font-size: 7.6pt;
      color: #334155;
      line-height: 1.32;
    }
    .indice-box {
      font-size: 7.5pt;
      color: #b45309;
      margin-top: 3px;
      background: #fffbeb;
      padding: 3px 8px;
      border-radius: 4px;
      border-left: 3px solid #f59e0b;
    }
    .vigilance-box {
      background: #fefce8;
      border: 1px solid #fef08a;
      border-left: 4px solid #eab308;
      border-radius: 6px;
      padding: 5px 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 3px;
    }
    """

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Correctif Parents - Chasse aux fautes CM2</title>
<style>
{css_parents}
</style>
</head>
<body>
{"".join(pages_html)}
</body>
</html>
"""

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_eleve_path = os.path.join(base_dir, "carnet_eleve.html")
    html_parents_path = os.path.join(base_dir, "correctif_parents.html")
    pdf_eleve_path = os.path.join(base_dir, "Carnet_Eleve_Chasse_aux_fautes_CM2.pdf")
    pdf_parents_path = os.path.join(base_dir, "Correctif_Parents_Chasse_aux_fautes_CM2.pdf")

    print("1. Génération de carnet_eleve.html...")
    with open(html_eleve_path, "w", encoding="utf-8") as f:
        f.write(generer_carnet_eleve_html())

    print("2. Génération de correctif_parents.html...")
    with open(html_parents_path, "w", encoding="utf-8") as f:
        f.write(generer_correctif_parents_html())

    chrome_cmd = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    print("3. Compilation du PDF élève...")
    subprocess.run([
        chrome_cmd,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_eleve_path}",
        "--no-pdf-header-footer",
        html_eleve_path
    ], check=True)

    print("4. Compilation du PDF parents...")
    subprocess.run([
        chrome_cmd,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_parents_path}",
        "--no-pdf-header-footer",
        html_parents_path
    ], check=True)

    def verifier_pdf(path):
        with open(path, "rb") as f:
            c = f.read()
            pages = c.count(b"/Type /Page") - c.count(b"/Type /Pages")
            taille_ko = len(c) // 1024
            return pages, taille_ko

    p_eleve, s_eleve = verifier_pdf(pdf_eleve_path)
    p_parents, s_parents = verifier_pdf(pdf_parents_path)

    print(f"\n[OK] Carnet Élève : {pdf_eleve_path} ({p_eleve} pages, {s_eleve} Ko)")
    print(f"[OK] Correctif Parents : {pdf_parents_path} ({p_parents} pages, {s_parents} Ko)")

if __name__ == "__main__":
    main()
