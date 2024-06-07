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


class FormWTFAjouteremploye(FlaskForm):

    employe_ajouter_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    nom = StringField("Nom", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                         Regexp( employe_ajouter_regexp,
                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    prenom = StringField("Prenom", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                         Regexp( employe_ajouter_regexp,
                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    date_de_naissance = StringField("Date de naissance", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                               Regexp(employe_ajouter_regexp,
                                                      message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    numero_avs = StringField("Numero AVS", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                               Regexp(employe_ajouter_regexp,
                                                      message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    notoriete = StringField("Notoriété", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                             Regexp( employe_ajouter_regexp,
                                                    message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    submit = SubmitField("Enregistrer le employe")


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, InputRequired

class FormWTFUpdateemploye(FlaskForm):

    employe_update_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    nom_update_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(employe_update_regexp,
                                                               message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    prenom_update_wtf = StringField("Prenom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                  Regexp(employe_update_regexp,
                                                         message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    notoriete_update_wtf = StringField("Notoriete", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(employe_update_regexp,
                                                               message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    submit = SubmitField("Update employe")


class FormWTFDeleteemploye(FlaskForm):
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

class FormWTFAjouterLiaisonEmployeChantier(FlaskForm):
    id_employe_wtf = SelectField('Employé', validators=[DataRequired()], coerce=int)
    id_chantier_wtf = SelectField('Chantier', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Ajouter Liaison')

class FormWTFUpdateLiaisonEmployeChantier(FlaskForm):
    id_employe_wtf = SelectField('Employé', validators=[DataRequired()], coerce=int)
    id_chantier_wtf = SelectField('Chantier', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Mettre à jour Liaison')







