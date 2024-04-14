{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# DWV primer pipeline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## benodigdheden:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conda:\n",
    "\n",
    "Voor het runnen van deze pipeline hebben wij een conda environment gemaakt die alle benodigde packages bevat. Om deze environment te gebruiken moet je eerst conda geinstalleerd hebben.\n",
    "\n",
    "installeer conda hier:\n",
    "https://conda.io/projects/conda/en/latest/user-guide/install/index.html\n",
    "\n",
    "Wanneer conda correct is geinstalleerd kan je de correcte environment instellen door de .yaml in de environment map in te laden.\n",
    "\n",
    "Laad de envoirenment door naar de DWV map te navigeren en dan dit command te runnen:\n",
    "\n",
    "#### conda env create -f environments/DWV_primer_pipeline.yaml"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### tools\n",
    "\n",
    "Naast de packages in de conda environment hebben wij ook een aantal apparte tools gebruikt. Deze moeten ook op het systeem geinstalleerd zijn om de pipeline correct te runnen.\n",
    "\n",
    "de volgende tools kunnen geinstalleerd worden door de links te volgen(zorg dat je goed de correcte versies van de tools installeert om zeker te weten dat de pipeline correct werkt)\n",
    "\n",
    "guppy 5.0.11:\n",
    "https://help.nanoporetech.com/en/articles/6628042-how-do-i-install-stand-alone-guppy\n",
    "\n",
    "clustalo 1.2.4:\n",
    "http://www.clustal.org/omega/\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Het runnen van de pipeline met snakemake\n",
    "\n",
    "Als de envoironment en de tools correct zijn geinstalleerd kan de snakemake pipeline voorbereid worden.\n",
    "\n",
    "### voorbereiden snakemake file\n",
    "\n",
    "De snakemake file die in de map pipeline staat kan niet direct gerunned worden. Eerst moeten de bestands locaties en namen verandert worden. \n",
    "\n",
    "Begin boven aan de snakemake file en vervang stapsgewijs de input en output regel zodat deze overeenkomt met de gewenste input en output.\n",
    "\n",
    "### snakemake runnen\n",
    "\n",
    "Je kan de pipeline runnen door naar de DWV map te navigeren en dan de correcte conda environment te activeren door het volgende command te runnen:\n",
    "\n",
    "#### conda activate DWV_primer_pipeline\n",
    "\n",
    "Als de conda environment correct geactiveerd is kan de pipeline gerunned worden met het volgende command:\n",
    "\n",
    "#### snakemake -s pipeline/DWV_snakefile -c 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## het runnen van de pipeline als snakemake niet werkt\n",
    "\n",
    "De snakemake file is vooral gemaakt om het runnen van de pipeline door nieuwe mensen makkelijker te maken. Maar als dit om welke reden dan ook niet lukt is het altijd mogelijk om ons logboek te gebruiken die in de map logboek staat. Om stap voor stap de pipeline zelf te runnen. In het logboek staan de directe commands beschreven die gerunned zijn om tot ons resultaat te komen. Het is wel belangrijk om te onthouden dat het logboek alle genomen stappen beschrijft, dus er staan ook tools en stappen in die later uit de pipeline gehaald zijn. Dus als je de pipeline runned door het logboek te volgen. Let goed op welke stappen echt in de pipeline gebruikt worden.\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
