# DWV Primer Pipeline

## Wat doet de pipeline?
Deze pipeline is gemaakt om uit (minion) sequencing data primers te maken. Wij hebben de pipeline gebruikt om primers te maken voor DWV. De meest belangrijke stappen van de pipeline zijn de volgende stappen. sequencing data wordt gebasecalled, data wordt getrimmed zodat er alleen DWV reads overblijven, een multiple sequence allignment wordt gemaakt, een fylogenetische boom wordt een gemaakt, een mutation plot wordt gemaakt, een consensus sequentie wordt gemaakt en als laatste worden de primers gegenereerd.

## De stappen in de pipeline

### Basecalling

In onze pipeline wordt Guppy gebruikt om de basecalling te doen. Hierbij wordt het model rna_r9.4.1_70bps_hac gebruikt. Om voor onze specifieke data zo goed mogelijk te basecallen. Bij de basecalling worden ook alle reads die een Qscore lager dan 7.5 hebben uit de data verwijderd. Als deze pipeline gerunned wordt met andere data moet er waarscijnlijk een ander model gebruikt worden dat voor die specifieke data bedoeld is. Guppy wordt in gpu mode gerunned zodat het veel sneller gaat.

### Fastq combineren

Hier worden alle fastq bestanden die door guppy gemaakt worden samengevoegd. Deze stap is nodig als de input voor guppy een map was met fast5 files inplaats van één fast5 file.

### Nanoplot

Hier wordt een naoplot report gemaakt voor de gecombineerde fastq files zodat de data van de reads bekeken kan worden.

### Trimmen

Hier worden alle reads die minder dan 10kb lang zijn uit de data gehaald. Zodat er alleen DWV reads over blijven.

### Nanoplot

Hier wordt een nanoplot report gemaakt van de DWV reads zodat er specifiek naar deze reads gekeken kan worden.

### Fastq to fasta

Hier wordt de fastq file omgezet naar fasta zodat hij door clustalo gebruikt kan worden.

### Multiple sequence allignment

Er is een Multiple sequence allignment gemaakt van de data door clustalo. Er zijn 80 threads gebruikt om clustalo te runnen. Het duurde alsnog meer dan 2 uur dus als je geen toegang hebt tot veel cores zal deze stap lang duren als je veel data hebt.

### Guide tree

Clustalo heeft ook een newick guide tree gemaakt. Deze wordt later omgezet naar een fylogenetische boom.

### Fylogenetische boom

Met de python module ete3 wordt van de guide tree een fylogenetische boom gemaakt.

### Mutation plot

Met de python module biopython wordt een mutation plot gemaakt. In deze plot wordt afgebeeld hoeveel matches en mismatches er zijn voor iedere locatie in het genoom.

### Consensus sequentie

Met een zelf geschreven python script wordt er een consensus sequentie gemaakt. De consensus sequentie wordt gemaakt door bij iedere positie in de multiple sequence allignment te kijken welke base het vaakst voor komt. Als er één base meer dan 50% van de keren voorkomt wordt deze in de consensus sequentie geplaatst. Als er meer dan 50% van de keren een gap is wordt deze positie uit de consensus sequentie gehaald. Als er niks meer dan 50% van de keren voorkomt wordt er een gap in de consensus sequentie geplaatst

### Primers

Met de python module primer3 worden primers gegenereerd vanuit de consensus sequentie. De standaard settings worden gebruikt en er worden 5 primers gegenereerd.

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

## Het runnen van de pipeline als snakemake niet werkt

De snakemake file is vooral gemaakt om het runnen van de pipeline door nieuwe mensen makkelijker te maken. Maar als dit om welke reden dan ook niet lukt is het altijd mogelijk om ons logboek te gebruiken die in de map logboek staat. Om stap voor stap de pipeline zelf te runnen. In het logboek staan de directe commands beschreven die gerunned zijn om tot ons resultaat te komen. Het is wel belangrijk om te onthouden dat het logboek alle genomen stappen beschrijft, dus er staan ook tools en stappen in die later uit de pipeline gehaald zijn. Dus als je de pipeline runned door het logboek te volgen. Let goed op welke stappen echt in de pipeline gebruikt worden.

## Systeem

deze pipeline is gerunned op linux. Wij kunnen niet garanderen dat het werkt op een andere OS.

## Bowtie2

Wij hebben zelf na onze pipeline om de primers te vinden zelf ook nog bowtie2 gerunned op de data om naar bepaalde sequenties in onze data te zoeken. (meer informatie in het logboek)
Dit staat helaas niet in onze pipeline omdat het ons niet gelukt was dit in snakemake te verwerken. Dit komt omdat de output die je mee geeft aan bowtie in de command line anders is
dan de output files die hij geeft. Hierdoor herkent snakemake de output niet en geeft hij error messages waardoor de hele pipeline stopt. Als je deze stap toch wil repliceren kan je 
onze stappen die in het logboek staan volgen.
