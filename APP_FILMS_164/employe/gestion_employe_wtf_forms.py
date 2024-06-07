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


from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, InputRequired

class FormWTFAjouteremploye(FlaskForm):
    employe_ajouter_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    avs_regexp = "^[0-9.]+$"  # New regular expression to allow numbers and periods

    nom = StringField("Nom", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                         Regexp(employe_ajouter_regexp,
                                                message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    prenom = StringField("Prenom", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                               Regexp(employe_ajouter_regexp,
                                                      message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    date_de_naissance = DateField("Date de naissance", format='%Y-%m-%d', validators=[DataRequired(message="Date requise")])

    numero_avs = StringField("Numero AVS", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                       Regexp(avs_regexp,
                                                              message="Uniquement des chiffres et des points")])

    notoriete = StringField("Notoriété", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                     Regexp(employe_ajouter_regexp,
                                                            message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    submit = SubmitField("Enregistrer le employe")

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, InputRequired

class FormWTFUpdateemploye(FlaskForm):
    employe_update_regexp = "^(?!.*['\-\s]{2,})([A-Za-zÀ-ÖØ-öø-ÿ0-9]+['\- ]?)*[A-Za-zÀ-ÖØ-öø-ÿ0-9]+$"
    avs_regexp = "^[0-9.]+$"

    nom_update_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                    Regexp(employe_update_regexp,
                                                           message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    prenom_update_wtf = StringField("Prenom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                          Regexp(employe_update_regexp,
                                                                 message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    numero_avs_update_wtf = StringField("Numero_AVS", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                  Regexp(avs_regexp,
                                                                         message="Uniquement des chiffres et des points")])

    date_de_naissance_update_wtf = DateField("Date de naissance", validators=[InputRequired("Date obligatoire"),
                                                                              DataRequired("Date non valide")])

    notoriete_update_wtf = StringField("Notoriété", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                Regexp(employe_update_regexp,
                                                                       message="Pas de caractères spéciaux, d'espace à double, de double apostrophe, de double trait union")])

    submit = SubmitField("Update employe")



class FormWTFDeleteEmploye(FlaskForm):
    """
        Dans le formulaire "employe_delete_wtf.html"

        nom_employe_delete_wtf : Champ qui reçoit la valeur de l'employé, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "employé".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_employe".
    """
    nom_employe_delete_wtf = StringField("Effacer cet Employé")
    submit_btn_del = SubmitField("Effacer Employé")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")

#Employe/chantier

class FormWTFAjouterLiaisonEmployeChantier(FlaskForm):
    id_employe_wtf = SelectField('Employé', validators=[DataRequired()], coerce=int)
    id_chantier_wtf = SelectField('Chantier', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Ajouter Liaison')

class FormWTFUpdateLiaisonEmployeChantier(FlaskForm):
        id_employe_wtf = SelectField('Employé', validators=[DataRequired()], coerce=int)
        id_chantier_wtf = SelectField('Chantier', validators=[DataRequired()], coerce=int)
        submit = SubmitField('Mettre à jour Liaison')

class FormWTFDeleteLiaisonEmployeChantier(FlaskForm):
    id_liaison_wtf = StringField("Effacer cette liaison", validators=[DataRequired()])
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_del = SubmitField("Effacer Liaison")
    submit_btn_annuler = SubmitField("Annuler")







