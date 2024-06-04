"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterChantier(FlaskForm):
    chantier_ajouter_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    rue = StringField("Rue", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                         Regexp( chantier_ajouter_regexp,
                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    cp = StringField("Cp", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                         Regexp( chantier_ajouter_regexp,
                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    ville = StringField("Ville", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                             Regexp( chantier_ajouter_regexp,
                                                    message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    etage = StringField("Etage", validators=[Length(min=1, max=50, message="min 2 max 50"),
                                             Regexp( chantier_ajouter_regexp,
                                                    message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    pays = StringField("Pays", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                             Regexp( chantier_ajouter_regexp,
                                                    message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    date_debut = DateField("Date de début", format='%Y-%m-%d', validators=[DataRequired(message="Date requise")])

    date_fin = DateField("Date de fin", format='%Y-%m-%d', validators=[DataRequired(message="Date requise")])

    statut = StringField("Statut", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                           Regexp( chantier_ajouter_regexp,
                                                  message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])
    submit = SubmitField("Enregistrer le Chantier")


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, InputRequired

class FormWTFUpdateChantier(FlaskForm):
    chantier_update_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    nom_rue_update_wtf = StringField("Rue", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(chantier_update_regexp,
                                                               message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    cp_update_wtf = StringField("Cp", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                  Regexp(chantier_update_regexp,
                                                         message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    ville_update_wtf = StringField("Ville", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(chantier_update_regexp,
                                                               message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    etage_update_wtf = IntegerField("Etage", validators=[DataRequired()])

    pays_update_wtf = StringField("Pays", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                      Regexp(chantier_update_regexp,
                                                             message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    date_debut_update_wtf = DateField("Date de début", validators=[InputRequired("Date obligatoire"),
                                                                   DataRequired("Date non valide")])

    date_fin_update_wtf = DateField("Date de fin", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])

    statut_update_wtf = StringField("Statut", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                          Regexp(chantier_update_regexp,
                                                                 message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    submit = SubmitField("Update chantier")


class FormWTFDeleteChantier(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
