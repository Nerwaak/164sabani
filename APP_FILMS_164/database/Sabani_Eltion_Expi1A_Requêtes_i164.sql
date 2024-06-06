-- Sélectionne tous les chantiers dont le statut est 'En cours'
SELECT * FROM t_chantier WHERE Statut = 'En cours';

-- Sélectionne la ville et la dépense totale de chaque chantier
SELECT t_chantier.Ville, SUM(t_budget.Depense) as Total_Depense
FROM t_budget
JOIN t_chantier ON t_budget.FK_chantier = t_chantier.ID_Chantier
GROUP BY t_chantier.Ville;

-- Sélectionne la ville du chantier et le nom et prénom des employés
SELECT t_chantier.Ville, t_employe.Nom, t_employe.Prenom
FROM t_employe
JOIN t_employe_chantier ON t_employe.ID_Employe = t_employe_chantier.FK_employe_chantier
JOIN t_chantier ON t_chantier.ID_Chantier = t_employe_chantier.FK_chantier_employe;

-- Sélectionne la ville du chantier et le nom du matériel utilisé
SELECT t_chantier.Ville, t_materiel.Nom
FROM t_chantier
JOIN t_chantier_materiel ON t_chantier.ID_Chantier = t_chantier_materiel.FK_chantier_materiel
JOIN t_materiel ON t_materiel.ID_Materiel = t_chantier_materiel.FK_materiel_chantier;

-- Sélectionne la ville du chantier, la description de la tâche, la date de début et la date de fin
SELECT t_chantier.Ville, t_tache.Description, t_tache.Date_debut, t_tache.Date_fin
FROM t_chantier
JOIN t_chantier_tache ON t_chantier.ID_Chantier = t_chantier_tache.FK_chantier_tache
JOIN t_tache ON t_tache.ID_Tache = t_chantier_tache.FK_tache_chantier;

-- Sélectionne tous les chantiers dont le statut est 'Terminé'
SELECT * FROM t_chantier WHERE Statut = 'Termine';

-- Sélectionne le nom et prénom des employés ainsi que leur email
SELECT t_employe.Nom, t_employe.Prenom, t_mail.Mail
FROM t_employe
JOIN t_employe_mail ON t_employe.ID_Employe = t_employe_mail.FK_employe_mail
JOIN t_mail ON t_mail.ID_Mail = t_employe_mail.FK_mail_employe;

-- Sélectionne le nom du fournisseur et le nom du matériel fourni
SELECT t_fournisseur.Nom, t_materiel.Nom
FROM t_fournisseur
JOIN t_materiel_fournisseur ON t_fournisseur.ID_Fournisseur = t_materiel_fournisseur.FK_fournisseur_materiel
JOIN t_materiel ON t_materiel.ID_Materiel = t_materiel_fournisseur.FK_materiel_fournisseur;

-- Sélectionne la ville du chantier et le budget total de chaque chantier
SELECT t_chantier.Ville, SUM(t_budget.Montant_total) as Total_Budget
FROM t_budget
JOIN t_chantier ON t_budget.FK_chantier = t_chantier.ID_Chantier
GROUP BY t_chantier.Ville;

-- Sélectionne la ville du chantier et le nombre d'employés affectés à chaque chantier
SELECT t_chantier.Ville, COUNT(t_employe_chantier.FK_employe_chantier) as Nombre_Employes
FROM t_chantier
JOIN t_employe_chantier ON t_chantier.ID_Chantier = t_employe_chantier.FK_chantier_employe
GROUP BY t_chantier.Ville;

-- Sélectionne la ville du chantier et le montant restant du budget de chaque chantier
SELECT t_chantier.Ville, t_budget.Montant_restant
FROM t_chantier
JOIN t_budget ON t_chantier.ID_Chantier = t_budget.FK_chantier;

-- Sélectionne la ville du chantier et la dépense moyenne de chaque chantier
SELECT t_chantier.Ville, AVG(t_budget.Depense) as Moyenne_Depense
FROM t_chantier
JOIN t_budget ON t_chantier.ID_Chantier = t_budget.FK_chantier
GROUP BY t_chantier.Ville;

-- Sélectionne la ville du chantier et le nombre de tâches associées à chaque chantier
SELECT t_chantier.Ville, COUNT(t_chantier_tache.FK_tache_chantier) as Nombre_Taches
FROM t_chantier
JOIN t_chantier_tache ON t_chantier.ID_Chantier = t_chantier_tache.FK_chantier_tache
GROUP BY t_chantier.Ville;

-- Sélectionne le nom et prénom du fournisseur ainsi que le nom du matériel fourni
SELECT t_fournisseur.Nom, t_fournisseur.Prenom, t_materiel.Nom as Materiel
FROM t_fournisseur
JOIN t_materiel_fournisseur ON t_fournisseur.ID_Fournisseur = t_materiel_fournisseur.FK_fournisseur_materiel
JOIN t_materiel ON t_materiel.ID_Materiel = t_materiel_fournisseur.FK_materiel_fournisseur;

-- Sélectionne le nom, prénom, date de naissance des employés ainsi que leur numéro de téléphone professionnel
SELECT t_employe.Nom, t_employe.Prenom, t_employe.Date_de_naissance, t_numero_telephone.Numero_telephone
FROM t_employe
JOIN t_employe_numero ON t_employe.ID_Employe = t_employe_numero.FK_employe_numero
JOIN t_numero_telephone ON t_numero_telephone.ID_Numero_telephone = t_employe_numero.FK_numero_employe
WHERE t_employe_numero.FK_type_numero = 1;  -- 1 pour 'Professionel'

-- Sélectionne la quantité totale de matériel disponible
SELECT SUM(Quantite_disponible) as Total_Materiel
FROM t_materiel;

-- Sélectionne le nom et prénom des employés ainsi que la description des tâches qu'ils effectuent
SELECT t_employe.Nom, t_employe.Prenom, t_tache.Description
FROM t_employe
JOIN t_employe_tache ON t_employe.ID_Employe = t_employe_tache.FK_employe_tache
JOIN t_tache ON t_tache.ID_Tache = t_employe_tache.FK_tache_employe;

-- Sélectionne le nom, prénom et la notoriété des employés
SELECT Nom, Prenom, Notoriete
FROM t_employe;

-- Sélectionne la ville, la rue, la date de début et la date de fin des chantiers
SELECT Ville, Rue, Date_debut, Date_fin
FROM t_chantier;

-- Sélectionne le nom, prénom des employés et leur email professionnel
SELECT t_employe.Nom, t_employe.Prenom, t_mail.Mail
FROM t_employe
JOIN t_employe_mail ON t_employe.ID_Employe = t_employe_mail.FK_employe_mail
JOIN t_mail ON t_mail.ID_Mail = t_employe_mail.FK_mail_employe
WHERE t_employe_mail.FK_type_mail = 1;  -- 1 pour 'Professionnel'
