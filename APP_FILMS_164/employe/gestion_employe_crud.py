"""Gestion des "routes" FLASK et des données pour les employe.
Fichier : gestion_employe_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.employe.gestion_employe_wtf_forms import FormWTFAjouteremploye
from APP_FILMS_164.employe.gestion_employe_wtf_forms import FormWTFDeleteemploye
from APP_FILMS_164.employe.gestion_employe_wtf_forms import FormWTFUpdateemploye

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /employe_afficher
    
    Test : ex : http://127.0.0.1:5575/employe_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_employe_sel = 0 >> tous les employe.
                id_employe_sel = "n" affiche le employe dont l'id est "n"
"""


@app.route("/employe_afficher/<string:order_by>/<int:id_employe_sel>", methods=['GET', 'POST'])
def employe_afficher(order_by, id_employe_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_employe_sel == 0:
                    strsql_employe_afficher = """SELECT * FROM t_employe ORDER BY ID_employe ASC"""
                    mc_afficher.execute(strsql_employe_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_employe"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du employe sélectionné avec un nom de variable
                    valeur_id_employe_selected_dictionnaire = {"value_id_employe_selected": id_employe_sel}
                    strsql_employe_afficher = """SELECT * FROM t_employe WHERE ID_employe = %(value_id_employe_selected)s"""

                    mc_afficher.execute(strsql_employe_afficher, valeur_id_employe_selected_dictionnaire)
                else:
                    strsql_employe_afficher = """SELECT * FROM t_employe ORDER BY ID_employe DESC"""

                    mc_afficher.execute(strsql_employe_afficher)

                data_employe = mc_afficher.fetchall()

                print("data_employe ", data_employe, " Type : ", type(data_employe))

                # Différencier les messages si la table est vide.
                if not data_employe and id_employe_sel == 0:
                    flash("""La table "t_employe" est vide. !!""", "warning")
                elif not data_employe and id_employe_sel > 0:
                    # Si l'utilisateur change l'id_employe dans l'URL et que le employe n'existe pas,
                    flash(f"Le employe demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_employe" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données employe affichés !!", "success")

        except Exception as Exception_employe_afficher:
            raise ExceptionEmployeAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{employe_afficher.__name__} ; "
                                          f"{Exception_employe_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("employe/employe_afficher.html", data=data_employe)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /employe_ajouter
    
    Test : ex : http://127.0.0.1:5575/employe_ajouter
    
    Paramètres : sans
    
    But : Ajouter un employe pour un film
    
    Remarque :  Dans le champ "name_employe_html" du formulaire "employe/employe_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/employe_ajouter", methods=['GET', 'POST'])
def employe_ajouter_wtf():
    form = FormWTFAjouteremploye()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                rue = form.rue.data
                cp = form.cp.data
                ville = form.ville.data
                etage = form.etage.data
                pays = form.etage.data
                date_debut = form.date_debut.data
                date_fin = form.date_fin.data
                statut = form.statut.data


                valeurs_insertion_dictionnaire = {
                    "value_rue": rue,
                    "value_cp": cp,
                    "value_ville": ville,
                    "value_etage": etage,
                    "value_pays": pays,
                    "value_date_debut": date_debut,
                    "value_date_fin": date_fin,
                    "value_statut": statut,
                }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_employe = """INSERT INTO t_employe (id_employe, Rue, Cp, Ville, Etage, Pays, Date_debut, 
                Date_fin, statut) 
                                         VALUES (NULL, %(value_rue)s, %(value_cp)s, %(value_ville)s, %(value_etage)s, %(value_pays)s, %(value_date_debut)s, %(value_date_fin)s, %(value_statut)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_employe, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('employe_afficher', order_by='DESC', id_employe_sel=0))

        except Exception as Exception_employe_ajouter_wtf:
            raise ExceptionEmployeAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{employe_ajouter_wtf.__name__} ; "
                                            f"{Exception_employe_ajouter_wtf}")

    return render_template("employe/employe_ajouter_wtf.html", form=form)



"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /employe_update
    
    Test : ex cliquer sur le menu "employe" puis cliquer sur le bouton "EDIT" d'un "employe"
    
    Paramètres : sans
    
    But : Editer(update) un employe qui a été sélectionné dans le formulaire "employe_afficher.html"
    
    Remarque :  Dans le champ "nom_employe_update_wtf" du formulaire "employe/employe_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/employe_update", methods=['GET', 'POST'])
def employe_update_wtf():
    id_employe_update = request.values['id_employe_btn_edit_html']

    form_update = FormWTFUpdateemploye()
    try:
        if request.method == "POST" and form_update.submit.data:
            rue = form_update.nom_rue_update_wtf.data
            cp = form_update.cp_update_wtf.data
            ville = form_update.ville_update_wtf.data
            etage = form_update.etage_update_wtf.data
            pays = form_update.pays_update_wtf.data
            date_debut = form_update.date_debut_update_wtf.data
            date_fin = form_update.date_fin_update_wtf.data
            statut = form_update.statut_update_wtf.data

            valeur_update_dictionnaire = {
                "value_rue": rue,
                "value_cp": cp,
                "value_ville": ville,
                "value_etage": etage,
                "value_pays": pays,
                "value_date_debut": date_debut,
                "value_date_fin": date_fin,
                "value_statut": statut,
                "value_id_employe": id_employe_update
            }

            str_sql_update_employe = """UPDATE t_employe SET Rue = %(value_rue)s, 
                                        Cp = %(value_cp)s, Ville = %(value_ville)s, 
                                        Etage = %(value_etage)s, Pays = %(value_pays)s, 
                                        Date_debut = %(value_date_debut)s, 
                                        Date_fin = %(value_date_fin)s, 
                                        statut = %(value_statut)s 
                                        WHERE ID_employe = %(value_id_employe)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_employe, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            return redirect(url_for('employe_afficher', order_by="ASC", id_employe_sel=id_employe_update))
        elif request.method == "GET":
            str_sql_id_employe = "SELECT * FROM t_employe WHERE ID_employe = %(value_id_employe)s"
            valeur_select_dictionnaire = {"value_id_employe": id_employe_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_employe, valeur_select_dictionnaire)
            data_employe = mybd_conn.fetchone()

            form_update.nom_rue_update_wtf.data = data_employe["Rue"]
            form_update.cp_update_wtf.data = data_employe["Cp"]
            form_update.ville_update_wtf.data = data_employe["Ville"]
            form_update.etage_update_wtf.data = data_employe["Etage"]
            form_update.pays_update_wtf.data = data_employe["Pays"]
            form_update.date_debut_update_wtf.data = data_employe["Date_debut"]
            form_update.date_fin_update_wtf.data = data_employe["Date_fin"]
            form_update.statut_update_wtf.data = data_employe["Statut"]

    except Exception as Exception_employe_update_wtf:
        raise ExceptionEmployeUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{employe_update_wtf.__name__} ; "
                                      f"{Exception_employe_update_wtf}")

    return render_template("employe/employe_update_wtf.html", form_update=form_update)

"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /employe_delete
    
    Test : ex. cliquer sur le menu "employe" puis cliquer sur le bouton "DELETE" d'un "employe"
    
    Paramètres : sans
    
    But : Effacer(delete) un employe qui a été sélectionné dans le formulaire "employe_afficher.html"
    
    Remarque :  Dans le champ "nom_employe_delete_wtf" du formulaire "employe/employe_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/employe_delete", methods=['GET', 'POST'])
def employe_delete_wtf():
    data_films_attribue_employe_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_employe"
    id_employe_delete = request.values['id_employe_btn_delete_html']

    # Objet formulaire pour effacer le employe sélectionné.
    form_delete = FormWTFDeleteemploye()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("employe_afficher", order_by="ASC", id_employe_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "employe/employe_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_employe_delete = session['data_films_attribue_employe_delete']
                print("data_films_attribue_employe_delete ", data_films_attribue_employe_delete)

                flash(f"Effacer le employe de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer employe" qui va irrémédiablement EFFACER le employe
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_employe": id_employe_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_employe = """DELETE FROM t_employe_film WHERE fk_employe = %(value_id_employe)s"""
                str_sql_delete_idemploye = """DELETE FROM t_employe WHERE id_employe = %(value_id_employe)s"""
                # Manière brutale d'effacer d'abord la "fk_employe", même si elle n'existe pas dans la "t_employe_film"
                # Ensuite on peut effacer le employe vu qu'il n'est plus "lié" (INNODB) dans la "t_employe_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_employe, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idemploye, valeur_delete_dictionnaire)

                flash(f"employe définitivement effacé !!", "success")
                print(f"employe définitivement effacé !!")

                # afficher les données
                return redirect(url_for('employe_afficher', order_by="ASC", id_employe_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_employe": id_employe_delete}
            print(id_employe_delete, type(id_employe_delete))

            # Requête qui affiche tous les films_employe qui ont le employe que l'utilisateur veut effacer
            str_sql_employe_films_delete = """SELECT * FROM t_employe_materiel 
                                            INNER JOIN t_film ON t_employe_film.fk_film = t_film.id_film
                                            INNER JOIN t_employe ON t_employe_film.fk_employe = t_employe.id_employe
                                            WHERE fk_employe = %(value_id_employe)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_employe_films_delete, valeur_select_dictionnaire)
                data_films_attribue_employe_delete = mydb_conn.fetchall()
                print("data_films_attribue_employe_delete...", data_films_attribue_employe_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "employe/employe_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_employe_delete'] = data_films_attribue_employe_delete

                # Opération sur la BD pour récupérer "id_employe" et "intitule_employe" de la "t_employe"
                str_sql_id_employe = "SELECT * FROM t_employe WHERE ID_employe = %(value_id_employe)s"

                mydb_conn.execute(str_sql_id_employe, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom employe" pour l'action DELETE
                data_nom_employe = mydb_conn.fetchone()
                print("data_nom_employe ", data_nom_employe, " type ", type(data_nom_employe), " employe ",
                      data_nom_employe["intitule_employe"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "employe_delete_wtf.html"
            form_delete.nom_employe_delete_wtf.data = data_nom_employe["intitule_employe"]

            # Le bouton pour l'action "DELETE" dans le form. "employe_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_employe_delete_wtf:
        raise ExceptionEmployeDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{employe_delete_wtf.__name__} ; "
                                      f"{Exception_employe_delete_wtf}")

    return render_template("employe/employe_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_employe_delete)
