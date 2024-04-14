# DWV Primer Pipeline

## Benodigdheden:

### Conda:

Voor het runnen van deze pipeline hebben wij een conda environment gemaakt die alle benodigde packages bevat. Om deze environment te gebruiken moet eerst conda geinstalleerd zijn.

Installeer conda hier:
https://conda.io/projects/conda/en/latest/user-guide/install/index.html

Wanneer conda correct is geinstalleerd kan je de correcte environment instellen door de .yaml in de environment map in te laden.

Laad de envoirenment door naar de DWV map te navigeren en dan dit command te runnen:

#### Conda env create -f environments/DWV_primer_pipeline.yaml

### Tools

Naast de packages in de conda environment hebben wij ook een aantal apparte tools gebruikt. Deze moeten ook op het systeem geinstalleerd zijn om de pipeline correct te runnen.

de volgende tools kunnen geinstalleerd worden door de links te volgen(zorg dat je goed de correcte versies van de tools installeert om zeker te weten dat de pipeline correct werkt)

guppy 5.0.11:
https://help.nanoporetech.com/en/articles/6628042-how-do-i-install-stand-alone-guppy

clustalo 1.2.4:
http://www.clustal.org/omega/

## Het runnen van de pipeline met snakemake

Als de envoironment en de tools correct zijn geinstalleerd kan de snakemake pipeline voorbereid worden.

### Voorbereiden snakemake file

De snakemake file die in de map pipeline staat kan niet direct gerunned worden. Eerst moeten de bestands locaties en namen verandert worden. 

Begin boven aan de snakemake file en vervang stapsgewijs de input en output regel zodat deze overeenkomt met de gewenste input en output.

### Snakemake runnen

Je kan de pipeline runnen door naar de DWV map te navigeren en dan de correcte conda environment te activeren door het volgende command te runnen:

#### Conda activate DWV_primer_pipeline

Als de conda environment correct geactiveerd is kan de pipeline gerunned worden met het volgende command:

#### Snakemake -s pipeline/DWV_snakefile -c 1

## het runnen van de pipeline als snakemake niet werkt

De snakemake file is vooral gemaakt om het runnen van de pipeline door nieuwe mensen makkelijker te maken. Maar als dit om welke reden dan ook niet lukt is het altijd mogelijk om ons logboek te gebruiken die in de map logboek staat. Om stap voor stap de pipeline zelf te runnen. In het logboek staan de directe commands beschreven die gerunned zijn om tot ons resultaat te komen. Het is wel belangrijk om te onthouden dat het logboek alle genomen stappen beschrijft, dus er staan ook tools en stappen in die later uit de pipeline gehaald zijn. Dus als je de pipeline runned door het logboek te volgen. Let goed op welke stappen echt in de pipeline gebruikt worden.

## systeem

deze pipeline is gerunned op linux. Wij kunnen niet garanderen dat het werkt op een andere OS.

## Bowtie2

Wij hebben zelf na onze pipeline om de primers te vinden zelf ook nog bowtie2 gerunned op de data om naar bepaalde sequenties in onze data te zoeken. (meer informatie in het logboek)
Dit staat helaas niet in onze pipeline omdat het ons niet gelukt was dit in snakemake te verwerken. Dit komt omdat de output die je mee geeft aan bowtie in de command line anders is
dan de output files die hij geeft. Hierdoor herkent snakemake de output niet en geeft hij error messages waardoor de hele pipeline stopt. Als je deze stap toch wil repliceren kan je 
onze stappen die in het logboek staan volgen.
