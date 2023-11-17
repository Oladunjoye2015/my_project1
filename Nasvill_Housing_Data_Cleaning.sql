/*
Cleaning Data in SQL Queries

*/


SELECT *

FROM NashVille_Housing

-- Standardize Date Format

ALTER TABLE Nashville_Housing
ADD SalesDateConverted Date;


UPDATE NashVille_Housing
SET SalesDateConverted=CONVERT(Date, SaleDate)

SELECT SalesDateConverted

FROM NashVille_Housing

--Populate Property Address

SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM NashVille_Housing a
JOIN NashVille_Housing b
ON a.ParcelID=b.ParcelID
AND a.[UniqueID ]<>b.[UniqueID ]
WHERE a.PropertyAddress is NULL


UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM NashVille_Housing a
JOIN NashVille_Housing b
ON a.ParcelID=b.ParcelID
AND a.[UniqueID ]<>b.[UniqueID ]
WHERE a.PropertyAddress is NULL


-- Breaking out Address into Individual Collumns (Address, City, State)


SELECT PropertyAddress
FROM NashVille_Housing

SELECT 
		SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1) AS Street,
		SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+ 1,  LEN(PropertyAddress)) AS City
FROM NashVille_Housing


ALTER TABLE Nashville_Housing
ADD PropertyStreet NVARCHAR(255);


UPDATE NashVille_Housing
SET  PropertyStreet=SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1)


ALTER TABLE Nashville_Housing
ADD PropertyCity NVARCHAR(255);


UPDATE NashVille_Housing
SET PropertyCity=SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+ 1,  LEN(PropertyAddress))


SELECT PropertyStreet, PropertyCity
FROM NashVille_Housing

-- Owner Address
SELECT
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
FROM NashVille_Housing



ALTER TABLE Nashville_Housing
ADD OwnerStreet NVARCHAR(255);


UPDATE NashVille_Housing
SET OwnerStreet=PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)



ALTER TABLE Nashville_Housing
ADD OwnerCity NVARCHAR(255);


UPDATE NashVille_Housing
SET OwnerCity=PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)


ALTER TABLE Nashville_Housing
ADD OwnerState NVARCHAR(255);


UPDATE NashVille_Housing
SET OwnerState=PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)



SELECT *
FROM NashVille_Housing

-- Change Y and N to Yes and No in "SolAsVacant" field
SELECT SoldASVacant,
	CASE WHEN SoldASVacant='Y' THEN 'Yes'
		 WHEN SoldAsVacant='N' THEN 'No'
		 ELSE SoldAsVacant 
		 END 
FROM NashVille_Housing

UPDATE NashVille_Housing
SET SoldAsVacant = CASE WHEN SoldASVacant='Y' THEN 'Yes'
		 WHEN SoldAsVacant='N' THEN 'No'
		 ELSE SoldAsVacant 
		 END 
FROM NashVille_Housing

SELECT SoldAsVacant
FROM NashVille_Housing


-- Remove Duplicates
WITH RowNumCTE AS(
SELECT *,
	ROW_NUMBER() OVER (PARTITION BY ParcelID, PropertyAddress, SalePrice, SaleDate, LegalReference ORDER BY UniqueID) row_num


FROM NashVille_Housing

)
DELETE
FROM RowNumCTE
WHERE row_num >1

--unused fields

ALTER TABLE NashVille_Housing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate


SELECT *
FROM NashVille_Housing