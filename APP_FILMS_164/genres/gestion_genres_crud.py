"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
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
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterChantier
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteChantier
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateChantier

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT * FROM t_chantier ORDER BY ID_Chantier ASC"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT * FROM t_chantier WHERE ID_Chantier = %(value_id_genre_selected)s"""

                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT * FROM t_chantier ORDER BY ID_Chantier DESC"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_chantier" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le chantier demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données chantier affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionChantierAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterChantier()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                rue = form.rue.data
                cp = form.cp.data
                ville = form.ville.data
                etage = form.etage.data
                pays = form.pays.data
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

                strsql_insert_genre = """INSERT INTO t_Chantier (id_Chantier, Rue, Cp, Ville, Etage, Pays, Date_debut, 
                Date_fin, statut) 
                                         VALUES (NULL, %(value_rue)s, %(value_cp)s, %(value_ville)s, %(value_etage)s, %(value_pays)s, %(value_date_debut)s, %(value_date_fin)s, %(value_statut)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionChantierAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)



"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    id_genre_update = request.values['id_genre_btn_edit_html']

    form_update = FormWTFUpdateChantier()
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
                "value_id_genre": id_genre_update
            }

            str_sql_update_chantier = """UPDATE t_Chantier SET Rue = %(value_rue)s, 
                                        Cp = %(value_cp)s, Ville = %(value_ville)s, 
                                        Etage = %(value_etage)s,
                                        Pays = %(value_pays)s,
                                        Date_debut = %(value_date_debut)s, 
                                        Date_fin = %(value_date_fin)s, 
                                        statut = %(value_statut)s 
                                        WHERE ID_Chantier = %(value_id_genre)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_chantier, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_genre_update))
        elif request.method == "GET":
            str_sql_id_genre = "SELECT * FROM t_Chantier WHERE ID_Chantier = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_genre_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
            data_chantier = mybd_conn.fetchone()

            form_update.nom_rue_update_wtf.data = data_chantier["Rue"]
            form_update.cp_update_wtf.data = data_chantier["Cp"]
            form_update.ville_update_wtf.data = data_chantier["Ville"]
            form_update.etage_update_wtf.data = data_chantier["Etage"]
            form_update.pays_update_wtf.data = data_chantier["Pays"]
            form_update.date_debut_update_wtf.data = data_chantier["Date_debut"]
            form_update.date_fin_update_wtf.data = data_chantier["Date_fin"]
            form_update.statut_update_wtf.data = data_chantier["Statut"]

    except Exception as Exception_genre_update_wtf:
        raise ExceptionChantierUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)

"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_employes_associes = None
    btn_submit_del = None
    id_genre_delete = request.args.get('id_genre_btn_delete_html')

    form_delete = FormWTFDeleteChantier()
    try:
        print("On submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            if form_delete.submit_btn_conf_del.data:
                flash(f"Effacer le Chantier de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                if not id_genre_delete:
                    raise ValueError("id_genre_delete is None")

                valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                # Suppression des relations employé-chantier
                str_sql_delete_chantier_employe = """DELETE FROM t_employe_chantier WHERE FK_chantier_employe = %(value_id_genre)s"""
                # Suppression du chantier lui-même
                str_sql_delete_chantier = """DELETE FROM t_chantier WHERE ID_Chantier = %(value_id_genre)s"""

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_chantier_employe, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_chantier, valeur_delete_dictionnaire)

                flash(f"Chantier définitivement effacé !!", "success")
                print(f"Chantier définitivement effacé !!")

                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        if request.method == "GET":
            if not id_genre_delete:
                raise ValueError("id_genre_delete is None")

            valeur_select_dictionnaire = {"value_id_genre": id_genre_delete}
            print(id_genre_delete, type(id_genre_delete))

            # Récupérer les détails du chantier
            str_sql_id_genre = "SELECT ID_Chantier, Rue FROM t_chantier WHERE ID_Chantier = %(value_id_genre)s"
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                data_nom_genre = mybd_conn.fetchone()
                if data_nom_genre is None:
                    raise ValueError(f"No data found for ID_Chantier = {id_genre_delete}")

                print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                      data_nom_genre["Rue"])

            form_delete.nom_genre_delete_wtf.data = data_nom_genre["Rue"]

            # Récupérer les employés associés au chantier
            str_sql_employes_associes = """
                SELECT Nom FROM t_employe
                INNER JOIN t_employe_chantier ON t_employe.ID_employe = t_employe_chantier.FK_employe_chantier
                WHERE FK_chantier_employe = %(value_id_genre)s
            """
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_employes_associes, valeur_select_dictionnaire)
                data_employes_associes = mybd_conn.fetchall()
                print("data_employes_associes ", data_employes_associes)

            btn_submit_del = False

    except KeyError as e:
        print(f"KeyError: {str(e)}")
        flash(f"Erreur interne: Clé manquante {str(e)}", "danger")
        return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))
    except Exception as Exception_genre_delete_wtf:
        print(f"Exception: {str(Exception_genre_delete_wtf)}")
        raise ExceptionChantierDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                         f"{genre_delete_wtf.__name__} ; "
                                         f"{Exception_genre_delete_wtf}")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_employes_associes=data_employes_associes)


