
Select location, date, total_cases, new_cases, total_deaths, population
FROM Covid_Deaths$
Order by 1,2

-- Looking at Total Cases Vs Total Deaths
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS DeathRate
FROM Covid_Deaths$
--WHERE location='United States'
Order by 1,2

-- percentage of population that got covid
SELECT location, date, total_cases, population, (total_deaths/population)*100 AS CovidRate
FROM Covid_Deaths$
WHERE location='United States'
Order by 1,2

-- Looking at country with highest infection rate

SELECT location, MAX(total_cases) AS highestinfectioncount, population, MAX((total_cases/population)*100) AS percentPopulationinfected
FROM Covid_Deaths$
GROUP BY location, population
Order by percentPopulationinfected DESC


SELECT location, date, MAX(total_cases) AS highestinfectioncount, population, MAX((total_cases/population)*100) AS percentPopulationinfected
FROM Covid_Deaths$
GROUP BY location, population, date
Order by percentPopulationinfected DESC


-- highest death rate by country 
SELECT location, MAX(Total_deaths) as TotalDeathCount
FROM Covid_Deaths$
WHERE continent is NULL
and location not in ('World', 'European Union', 'Lower middle income', 'Low income', 'High income','Upper middle income')
GROUP BY location 
ORDER BY TotalDeathCount DESC

-- highest death count by continent 
SELECT continent, MAX(Total_deaths) as TotalDeathCount
FROM Covid_Deaths$
WHERE continent is not NULL
GROUP BY continent
ORDER BY TotalDeathCount DESC

-- Gobal Numbers
SELECT SUM(new_cases)  AS New_Total_Cases,  SUM(new_deaths) AS New_Total_deaths,(SUM(new_deaths)/SUM(new_cases))* 100 AS New_DeathRate
FROM Covid_Deaths$
WHERE continent is not null
--GROUP BY date
Order by 1,2


-- Total population vs Vaccination use CTE
With  popVSVac (continent, location, Date, population, New_vaccinations, rolligpeopleVaccinated)
AS
(
SELECT Dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(numeric,vac.new_vaccinations)) OVER (partition by dea.location ORDER BY dea.location , dea.date) AS rollingpeopleVaccinated
--,(rollingpeopleVaccinated/dea.population)
FROM Covid_Deaths$ AS Dea
JOIN Covid_Vaccination$ AS Vac
ON dea.location=vac.location
and dea.date=Vac.date
WHERE dea.continent is not Null
--ORDER BY 2, 3
)
SELECT *,  (rolligpeopleVaccinated/population)*100 AS rollingPercentage_Vaccinated
FROM popVSVac


--TEMP TABLE
DROP TABLE if exists #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(continent nvarchar(255), location nvarchar(255), Date datetime,
population numeric, new_vaccinations numeric, rollingpeopleVaccinated numeric)

INSERT INTO #PercentPopulationVaccinated

SELECT Dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(numeric,vac.new_vaccinations)) OVER (partition by dea.location ORDER BY dea.location , dea.date) AS rollingpeopleVaccinated
--,(rollingpeopleVaccinated/dea.population)
FROM Covid_Deaths$ AS Dea
JOIN Covid_Vaccination$ AS Vac
ON dea.location=vac.location
and dea.date=Vac.date
WHERE dea.continent is not Null
--ORDER BY 2, 3

SELECT *,  (rollingpeopleVaccinated/population)*100 AS rollingPercentage_Vaccinated
FROM #PercentPopulationVaccinated

--creating view to store data for later
CREATE VIEW Num_CovidRate AS
-- percentage of population that got covid
SELECT location, date, total_cases, population, (total_deaths/population)*100 AS CovidRate
FROM Covid_Deaths$
--WHERE location='United States'
--Order by 1,2
CREATE view Covid_Rate_By_Location AS
SELECT location, MAX(total_cases) AS highest_CovidInfection, population, MAX((total_cases/population)*100) AS CovidRate
FROM Covid_Deaths$
WHERE continent is not NULL
GROUP BY location, population
--Order by CovidRate DESC

CREATE VIEW Highest_Death_by_location AS
SELECT location, MAX(Total_deaths) as TotalDeathCount
FROM Covid_Deaths$
WHERE continent is not NULL
GROUP BY location 
--ORDER BY TotalDeathCount DESC

CREATE VIEW Highest_Death_by_continent AS
SELECT continent, MAX(Total_deaths) as TotalDeathCount
FROM Covid_Deaths$
WHERE continent is not NULL
GROUP BY continent
--ORDER BY TotalDeathCount DESC

-- Gobal 
CREATE VIEW  overall_DeathRate AS

SELECT SUM(new_cases)  AS New_Total_Cases,  SUM(new_deaths) AS New_Total_deaths,(SUM(new_deaths)/SUM(new_cases))* 100 AS New_DeathRate
FROM Covid_Deaths$
WHERE continent is not null
--GROUP BY date
--Order by 1,2

-- Total population vs Vaccination use CTE

CREATE VIEW populationVSVaccination_CTE AS
With  popVSVac (continent, location, Date, population, New_vaccinations, rolligpeopleVaccinated)
AS
(
SELECT Dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(numeric,vac.new_vaccinations)) OVER (partition by dea.location ORDER BY dea.location , dea.date) AS rollingpeopleVaccinated
--,(rollingpeopleVaccinated/dea.population)
FROM Covid_Deaths$ AS Dea
JOIN Covid_Vaccination$ AS Vac
ON dea.location=vac.location
and dea.date=Vac.date
WHERE dea.continent is not Null
--ORDER BY 2, 3
)
SELECT *,  (rolligpeopleVaccinated/population)*100 AS rollingPercentage_Vaccinated
FROM popVSVac


--TEMP TABLE
CREATE VIEW Temporary_Table AS
--DROP TABLE if exists #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(continent nvarchar(255), location nvarchar(255), Date datetime,
population numeric, new_vaccinations numeric, rollingpeopleVaccinated numeric)

INSERT INTO #PercentPopulationVaccinated

SELECT Dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(numeric,vac.new_vaccinations)) OVER (partition by dea.location ORDER BY dea.location , dea.date) AS rollingpeopleVaccinated
--,(rollingpeopleVaccinated/dea.population)
FROM Covid_Deaths$ AS Dea
JOIN Covid_Vaccination$ AS Vac
ON dea.location=vac.location
and dea.date=Vac.date
WHERE dea.continent is not Null
--ORDER BY 2, 3

SELECT *,  (rollingpeopleVaccinated/population)*100 AS rollingPercentage_Vaccinated
FROM #PercentPopulationVaccinated