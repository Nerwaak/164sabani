SELECT * FROM t_chantier WHERE Statut = 'En cours';

SELECT t_chantier.Ville, SUM(t_budget.Depense) as Total_Depense
FROM t_budget
JOIN t_chantier ON t_budget.FK_chantier = t_chantier.ID_Chantier
GROUP BY t_chantier.Ville;

SELECT t_chantier.Ville, t_employe.Nom, t_employe.Prenom
FROM t_employe
JOIN t_employe_chantier ON t_employe.ID_Employe = t_employe_chantier.FK_employe_chantier
JOIN t_chantier ON t_chantier.ID_Chantier = t_employe_chantier.FK_chantier_employe;

SELECT t_chantier.Ville, t_materiel.Nom
FROM t_chantier
JOIN t_chantier_materiel ON t_chantier.ID_Chantier = t_chantier_materiel.FK_chantier_materiel
JOIN t_materiel ON t_materiel.ID_Materiel = t_chantier_materiel.FK_materiel_chantier;

SELECT t_chantier.Ville, t_tache.Description, t_tache.Date_debut, t_tache.Date_fin
FROM t_chantier
JOIN t_chantier_tache ON t_chantier.ID_Chantier = t_chantier_tache.FK_chantier_tache
JOIN t_tache ON t_tache.ID_Tache = t_chantier_tache.FK_tache_chantier;

SELECT * FROM t_chantier WHERE Statut = 'Termine';

SELECT t_employe.Nom, t_employe.Prenom, t_mail.Mail
FROM t_employe
JOIN t_employe_mail ON t_employe.ID_Employe = t_employe_mail.FK_employe_mail
JOIN t_mail ON t_mail.ID_Mail = t_employe_mail.FK_mail_employe;

SELECT t_fournisseur.Nom, t_materiel.Nom
FROM t_fournisseur
JOIN t_materiel_fournisseur ON t_fournisseur.ID_Fournisseur = t_materiel_fournisseur.FK_fournisseur_materiel
JOIN t_materiel ON t_materiel.ID_Materiel = t_materiel_fournisseur.FK_materiel_fournisseur;

SELECT t_chantier.Ville, SUM(t_budget.Montant_total) as Total_Budget
FROM t_budget
JOIN t_chantier ON t_budget.FK_chantier = t_chantier.ID_Chantier
GROUP BY t_chantier.Ville;

SELECT t_chantier.Ville, COUNT(t_employe_chantier.FK_employe_chantier) as Nombre_Employes
FROM t_chantier
JOIN t_employe_chantier ON t_chantier.ID_Chantier = t_employe_chantier.FK_chantier_employe
GROUP BY t_chantier.Ville;

SELECT t_chantier.Ville, t_budget.Montant_restant
FROM t_chantier
JOIN t_budget ON t_chantier.ID_Chantier = t_budget.FK_chantier;

SELECT t_chantier.Ville, AVG(t_budget.Depense) as Moyenne_Depense
FROM t_chantier
JOIN t_budget ON t_chantier.ID_Chantier = t_budget.FK_chantier
GROUP BY t_chantier.Ville;

SELECT t_chantier.Ville, COUNT(t_chantier_tache.FK_tache_chantier) as Nombre_Taches
FROM t_chantier
JOIN t_chantier_tache ON t_chantier.ID_Chantier = t_chantier_tache.FK_chantier_tache
GROUP BY t_chantier.Ville;

SELECT t_fournisseur.Nom, t_fournisseur.Prenom, t_materiel.Nom as Materiel
FROM t_fournisseur
JOIN t_materiel_fournisseur ON t_fournisseur.ID_Fournisseur = t_materiel_fournisseur.FK_fournisseur_materiel
JOIN t_materiel ON t_materiel.ID_Materiel = t_materiel_fournisseur.FK_materiel_fournisseur;

SELECT t_employe.Nom, t_employe.Prenom, t_employe.Date_de_naissance, t_numero_telephone.Numero_telephone
FROM t_employe
JOIN t_employe_numero ON t_employe.ID_Employe = t_employe_numero.FK_employe_numero
JOIN t_numero_telephone ON t_numero_telephone.ID_Numero_telephone = t_employe_numero.FK_numero_employe
WHERE t_employe_numero.FK_type_numero = 1;  -- 1 is for 'Professionel'

SELECT SUM(Quantite_disponible) as Total_Materiel
FROM t_materiel;

SELECT t_employe.Nom, t_employe.Prenom, t_tache.Description
FROM t_employe
JOIN t_employe_tache ON t_employe.ID_Employe = t_employe_tache.FK_employe_tache
JOIN t_tache ON t_tache.ID_Tache = t_employe_tache.FK_tache_employe;

SELECT Nom, Prenom, Notoriete
FROM t_employe;

SELECT Ville, Rue, Date_debut, Date_fin
FROM t_chantier;

SELECT t_employe.Nom, t_employe.Prenom, t_mail.Mail
FROM t_employe
JOIN t_employe_mail ON t_employe.ID_Employe = t_employe_mail.FK_employe_mail
JOIN t_mail ON t_mail.ID_Mail = t_employe_mail.FK_mail_employe
WHERE t_employe_mail.FK_type_mail = 1;  -- 1 is for 'Professionnel'









































