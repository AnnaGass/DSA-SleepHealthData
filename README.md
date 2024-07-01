# DSA-SleepHealthData

**Thema**: Schlafapnoe-Erkennung mittels Wearable-Daten: Ein Modell basierend auf klinischen Daten

**Team**: HeartDataSquad

**Team-Mitglieder**: Alejandro Restrepo Klinge,
Anna Gaßmann,
Yusuf Özdemirkan,
Sofie Haas,
Tristan Gräble,
David Silva Goncalves

**Versionierung**

| Version | Datum | Details | 
|--------|--------|--------|
|V1.0|15.05.2024|Projektskizze + Datenaufbereitung|
|V2.0|12.06.2024|Dokumentation + Modellerstellung|
|V3.0|03.07.2024|Dokumentation + Modellerstellung|

**Zeitraum des Semesterprojekts**: 03.04.2024 - 03.07.2024 

## 1. Beschreibung der Problematik
## 1.1. Hintergrund
Schlafapnoe ist eine weit verbreitete, aber oft unbemerkte schlafbezogene Atemstörung, die durch wiederholte Atemaussetzer während des Schlafs gekennzeichnet ist.
Diese Unterbrechungen führen zu einer verminderten Sauerstoffversorgung des Körpers und stören das natürliche Schlafmuster.
Der Schweregrad der nächtlichen Atemaussetzer (≥ 10 Sekunden) wird anhand des AHI (Apnoe-Hypopnoe-Index) klasifiziert: 
* Leicht 5–15 Atemaussetzer/Minute
* Mittel 15–30 Atemaussetzer/Minute
* Schwer > 30 Atemaussetzer/Minute

Unbehandelt kann Schlafapnoe zu ernsthaften gesundheitlichen Problemen wie Herz-Kreislauf-Erkrankungen, Diabetis und Schlaganfall führen.
Aktuell erfolgt die Diagnose hauptsächlich durch aufwändige Polysomnographie-Tests in spezialisierten Schlaflaboren. Diese Tests erfordern, dass Patienten über Nacht in der Klink bleiben und an verschiedenen Sensoren angeschlossen werden, was logistisch als auch finanziell belastend ist und sich nicht für eine langfristige Überwachung eignet. Zudem können die Ergebnisse durch die ungewohnte, klinische Umgebung verzerrt sein.

## 1.2. Mögliche Lösungen durch das Projekt
Dieses Projekt zielt darauf ab, Schlafapnoe mithilfe von Wearable-Daten zu erkennen und die Nutzer über das mögliche Bestehen einer Schlafapnoe zu informieren. Dafür soll ein Modell mithilfe von klinischen Daten (siehe Kapitel 4.2 Mögliche Datenquellen) entwickelt werden. Durch die frühzeitige Erkennung von Schlafapnoe können Betroffenen eine ärztliche Behandlung aufsuchen und dadurch das Risiko für die oben genannten Erkrankungen reduzieren. Wearables können im Alltag, beim Sport und in Ruhephasen getragen werden. Dadurch entfällt die Notwendigkeit einer Übernachtung in einem Schlaflabor, und die Nutzer können sich in ihrer gewohnten Umgebung befinden. Dadurch können Daten aus realistischen und alltäglichen Situationen erfasst werden. Zudem ermöglicht die nächtliche und regelmäßige Überwachung des Schalfs durch Wearables eine genauere Beurteilung der Schlafqualität.

## 2. Projektziele

Um die Ziele in messbare, zeitgebundene und klare Vorgaben zu definieren werden sie mithilfe der SMART-Zielformulierung formuliert. Damit kann zudem der Forschritt und der Erfolg des Projekts überwacht werden.

### 2.1. Projektziel - Preparation of Data
Gewinnung und Konvertierung von klinischen Daten in für das Modell nutzbare Daten.

**SMART-Zielformulierung:**
Die Datenaufbereitung ist abgeschlossen, wenn innerhalb von einem Monat 100% der klinischen Daten bereinigt, normalisiert und konvertiert wurden und in einem für das Modell verwendbaren Format vorliegen.

**Specific:** Die klinischen Daten müssen so vor- und aufbereitet werden, dass sie mit dem Machine-Learning-Modell genutzt werden können. Das beinhaltet das Bereinigen, Normalisieren und Konvertieren der Daten.

**Mesurable:** Die Datenvorbereitung ist abgeschlossen, wenn 100% der benötigten Daten in einem für das Modell verwendbaren Format vorliegen und die Datensätze bereinigt wurden.

**Achievable:** Mit den vorhandenen Ressourcen und dem Zugang zu den erforderlichen klinischen Daten sollte die Datenaufbereitung innerhalb des festgelegten Projekt-Zeitrahmens durchgeführt werden.

**Relevant:** Eine präzise und vollständige Datenaufbereitung ist entscheidend für die Genauigkeit des Modells und damit den Erfolg des gesamten Projekts.

**Time-bounded:** Die Datenaufbereitung muss innerhalb von 4 Wochen abgeschlossen werden.

![Preparation of Data](https://raw.githubusercontent.com/AnnaGass/DSA-SleepHealthData/c90d1071f9640b0ab6695decd131f6dafb6a4f42/Flow1.drawio.png)

### 2.2. Projektziel - Data Analysis + Model Creation
Analyse der Daten und Entwicklung eines Modells zur Erkennung von Schlafapnoe-Phasen durch die Nutzung von klinischen Messdaten (siehe Kapitel 3a)
Klassifizierung der Schlafapnoe nach dem Apnoe-Hypopnoe-Index (AHI)

**SMART-Zielformulierung:**
Ein Machine-Learning-Modell zur Erkennung von Schlafapnoe-Phasen wird innerhalb von ccc Monaten nach Abschluss der Datenaufbereitung entwickelt und getestet, mit einer Genauigkeit von mindestens 85%, einer Sensitivität von mindestens 80% und eine Spezifität von mindestens 80%.

**Specific:** Es soll ein Modell entwickelt werden, das Schlafapnoe-Pahasen anhand von klinischen Messdaten erkennt und die Schlafapnoe nach dem Apnoe-Hypopnoe-Index (AHI) klassifiziert.

**Mesurable:** Das Modell gilt als präzise genug, wenn es eine Genauigkeit von mindestens 85%, eine Sensitivität von mindestens 80% und eine Spezifität von mindestens 80% aufweist.

**Achievable:** Mit den vorhandenen Daten und den zur Verfügung stehenden Modellierungswerkzeugen ist das Ziel erreichbar. 

**Relevant:** Die Modellgenauigkeit ist entscheidend für die zuverlässige Erkennung von Schlafapnoe und damit die Akzeptanz und den Erfolg des Projekts. 

**Time-bounded:** Das Modell muss innerhalb von 3 Wochen nach Abschluss der Datenaufbereitung entwickelt und getestet werden. 

![Data Analysis + Model Creation](https://github.com/AnnaGass/DSA-SleepHealthData/blob/34ccfd4f38311f0dfc050df18122f38fbaeb79b6/flows/Flow2.drawio.png)


### 2.3. Projektziel - Hypothesis Validation
Validierung der Hypothese und Testen des Modells

**SMART-Zielformulierung:**
Die Hypothese, dass Schlafapnoe mithilfe von Wearable-Daten erkannt werden kann, wird innerhalb von 2 Monaten nach der Modellentwicklung validiert, indem das Modell an einem unabhängigen Datensatz getestet und die festgelegten Genauigkeitskriterien erfüllt werden.

**Specific:** Die Hypothese, dass Schlafapnoe mithilfe von Wearable-Daten erkannt werden kann, soll validiert werden.

**Mesurable:** Die Validierung ist abgeschlossen, wenn das Modell an einem unabhängigen Datensatz getestet und die festgelegten Genauigkeitskriterien erfüllt hat.

**Achievable:** Durch den Einsatz der entwickelten Modelle und der verfügbaren klinischen Daten sollte die Hypothesenvalidierung machbar sein. 

**Relevant:** Die Validierung der Hypothese ist entscheidend, um die klinische Nützlichkeit und den praktischen Einsatz des Modells zu bestätigen.

**Time-bounded:** Die Hypothesenvalidierung muss innerhalb von 3 Wochen nach der Modellentwicklung abgeschlossen sein. 

![Hypothesis Validation](https://github.com/AnnaGass/DSA-SleepHealthData/blob/354c2d079c5b08daed40b96d017ccceba6922886/Flow3.drawio.png)


Aus den einzelnen Flows ergibt sich dieser Gesamtflow, entsprechend der Architektur des Projektes (siehe Kapitel 3.3): 

![Complete Flow](https://github.com/AnnaGass/DSA-SleepHealthData/blob/354c2d079c5b08daed40b96d017ccceba6922886/CompleteFlow.drawio.png)

## 3. Erste technische Dokumentation

### 3.1 Datenquellen
Die zur Modellerstellung verwendeten Forschungsdaten stammen aus der St. Vincent´s University Hospital / University College Dublin Schlafapnoe-Datenbank. Diese Datenbank enthält 25 vollständige Übernacht-Polysomnogramme von erwachsenen Personen mit Verdacht auf obstruktive Schlafapnoe, zentrale Schlafapnoe oder primärem Schnarchen. Die überarbeitete Version dieser Datenbank wurde am 01.09.2011 veröffentlicht. Allgemeine Informationen zu den Patienten (BMI, Alter, AHI-Index, Körpergröße,...) sind in der Datei SubjectDetails.xls dargestellt.

Die gesamten Daten sind unter der folgenden Quelle zu finden: https://physionet.org/content/ucddb/1.0.0/ (Stand 08.05.2024)

Folgende Abbildung fasst die wichtigsten Daten der Datenbank zusammen:

![Database](https://github.com/AnnaGass/DSA-SleepHealthData/blob/79dcf71dce61faea7d92affa54ff811221a08e3b/Database.drawio.png)

Zu Erstellung des klinischen Modells werden drei Patienten der genannten Forschung ausgewählt. Die Patienten werden anhand des AHI-Index aus der Datei SubjectDetails.xls gewählt.
Dabei werden der Patient mit dem höchsten AHI-Index, der Patient mit dem niedrigsten AHI-Index und ein Patient mit einem dazwischenliegenden Wert gewählt, um eine möglichst große Verteilung des AHI-Index zu haben.

Die Entscheidung für diese Daten fiel anhand der folgenden Kriterien (sortiert nach Wichtigkeit): 
1. Die Daten sind repräsentativ und gültig, da keine leeren Werte vorhanden sind, ebenso treten keine zeitlichen Lücken auf.
2. Die Quelldaten sind weder komprimiert, noch gekürzt.
3. Es ist eine Vielzahl an Patientendaten verfügbar.
4. Es sind zusätzliche Annotationen vorhanden, sodass das Gesamtbild nachvollzogen werden kann.
5. Die Quelle ist eine Kooperation der St. Vincent´s University Hospital / University College Dublin. Dies macht die Daten zu glaubwürdigen Daten.
6. Es gibt eine "Open Data Commons Attribution License V1.0".
7. Es gibt zitierfähige Publikationen (z.B. https://ieeexplore.ieee.org/document/9864566).

**Datenschutz**

Die verwendeten Daten stammen aus einer öffentlich zugänglichen Forschungsdatenbank und wurden in Übereinstimmung mit den Datenschutzrichtlinien erhoben und veröffentlicht.

Bei der Verarbeitung werden die folgenden Grundsätze der Datenschutz-Grundverordnung (DSGVO) beachtet: 
* Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz: Die Daten werden rechtmäßig, fair und transparent verarbeitet
* Zweckbindung: Die Daten werden nur für die Erstellung des klinischen Modells verwendet
* Datenminimierung: Es werden nur die für das Modell notwendigen Daten verwendet
* Speicherbegrenzung: Die Daten werden nur so lange gespeichert, wie es für die Erreichung der Projektziele notwenig ist

### 3.2 Installationsanleitung

1. **Notebook auswählen**  

   Die gewünschte Notebook-Datei (.ipynb) aus dem Repository auswählen.

2. **Den Code in Google Colab öffnen**

   Den Button "Open in Colab" betätigen.

3. **Subjekt (Patienten-ID) auswählen**  

   Das Subjekt (entspricht der Patienten-ID) im Notebook auswählen. Möglich ist hierbei eine ID zwischen 002-028.
   Zur Erstellung des Modells wurden die folgenden drei IDs verwendet:
   * 018 (niedrigster AHI-Index)
   * 027 (höchster AHI-Index)
   * 006 (mittlerer AHI-Index)

4. **Notebook ausführen**  

   Das Notebook starten und laufen lassen. **Die Installtion aller benötigten Libraries ist bereits im Quellcode definiert. Diese werden automatisch beim Starten des Programms bei Bedarf installiert.**

5. **Ergebnisse überprüfen**  

   Die Ausgabe des Notebooks auf etwaige Fehler oder Warnungen überprüfen. Sicherstellen, dass das Modell ordnungsgemäß erstellt und validiert wurde.   

### 3.3 Architektur
Die Architektur besteht aus mehreren Hauptkomponenten: Datenakquise, Datenverarbeitung, Datenanalyse und Visualisierung.

#### Datenakquise
Die Daten werden von der PhysioNet-Plattform bezogen, wo sie als .rec und .txt Dateien für verschiedene Patienten zur Verfügung stehen. Die Dateien enthalten klinische Messdaten und Annotationen zur Schlafphase und zu Atmungsereignissen. Diese Daten werden mittels Skriptbefehlen heruntergeladen und lokal gespeichert, um eine schnelle und wiederholbare Verarbeitung zu ermöglichen.

#### Datapreparation
Nach dem Herunterladen der Daten folgt die Verarbeitung:

* **Signalverarbeitung**: Die Rohsignale (z.B. SpO2, Puls) werden aus den .rec Dateien extrahiert und in CSV-Dateien formatiert.
* **Annotationsextraktion**: Schlafstadien und Atmungsereignisse werden aus den entsprechenden .txt Dateien gelesen und ebenfalls in CSV-Dateien umgewandelt.

Diese Prozesse nutzen Python-Bibliotheken wie pyedflib für das Lesen von EDF-Dateien und pandas für die Datenmanipulation.

#### Modellentwicklung und Datenanalyse
Die verarbeiteten Daten werden anschließend analysiert, um Muster zu erkennen und Vorhersagemodelle zu erstellen. Dabei kann auch auf maschinelles Lernen zurückgegriffen werden.

Beispiele dazu wären:
* **Feature Engineering**: Es werden relevante Merkmale aus den Signalen abgeleitet, die für die Vorhersage von Schlafapnoe nützlich sind.
* **Modelltraining**: Verschiedene Modelle werden trainiert und evaluiert, um das effektivste zu identifizieren.

#### Visualisierung
Zur Überprüfung der Datenqualität und zur Darstellung der Analyseergebnisse werden Visualisierungen verwendet. 'matplotlib' und 'plotly' bieten Funktionen, um die Zeitreihen der biologischen Signale sowie die Ergebnisse der Modellvorhersagen graphisch darzustellen.

#### Technologien
* **Python**: Als Hauptprogrammiersprache für das Projekt
* **Jupyter Notebook**: Um die Übersicht des Projekts zu erleichtern

Der entsprechende Code ist im Notebook _01_DataPreparation.ipynb_ zu finden.

## 4. Datavisualization
Die vorbereiteten Daten werden im Notebook _02_DataVisualizations.ipynb_ visualisiert. 
Hierzu wurden zur Darstellung der Daten Histogramme und Boxplots unter Verwendung der Python-Bibliotheken matplotlib und seaborn erstellt.
Die Visualisierungen bieten einen umfassenden Überblick über wichitge Metirken im Datensatz und zeigen die Verteilung sowie die zusammenhänge zwischen Puls, SpO2, Schlafstadien und Apnoe-Ereignisse.

Ergebnisse: 
|  | Subject 020 | Subject 024 | Subject 027 |
|--------|--------|--------|--------|
| Verteilung der Herzfrequenz (Puls)| ![Verteilung der Herzfrequenz (Puls) sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/histograms/Pulse.png) | ![Verteilung der Herzfrequenz (Puls) sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/histograms/Pulse.png) | ![Verteilung der Herzfrequenz (Puls) sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/histograms/Pulse.png) |
| Verteilung der Sauerstoffsättigung (SpO2)| ![Verteilung der Sauerstoffsättigung (SpO2) sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/histograms/Sp02.png) | ![Verteilung der Sauerstoffsättigung (SpO2) sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/histograms/Sp02.png) | ![Verteilung der Sauerstoffsättigung (SpO2) sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/histograms/Sp02.png) |
| Verteilung der Schlafstadien| ![Verteilung der Schlafstadien sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/histograms/SleepStage.png)| ![Verteilung der Schlafstadien sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/histograms/SleepStage.png) | ![Verteilung der Schlafstadien sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/histograms/SleepStage.png) |
| Verteilung der Apnoe-Ereignisse| ![Verteilung der Apnoe-Ereignisse sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/histograms/Apnea.png) | ![Verteilung der Apnoe-Ereignisse sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/histograms/Apnea.png) | ![Verteilung der Apnoe-Ereignisse sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/histograms/Apnea.png) |
| Puls in verschiedenen SpO2-Kategorien| ![Puls in verschiedenen SpO2-Kategorien sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/boxplots/Sp02Cat-Pulse.png) | ![Puls in verschiedenen SpO2-Kategorien sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/boxplots/Sp02Cat-Pulse.png)| ![Puls in verschiedenen SpO2-Kategorien sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/boxplots/Sp02Cat-Pulse.png) |
| Puls in verschiedenen Schlafstadien| ![Puls in verschiedenen Schlafstadien sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/boxplots/Pulse-SleepPhase.png) | ![Puls in verschiedenen Schlafstadien sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/boxplots/Pulse-SleepPhase.png)| ![Puls in verschiedenen Schlafstadien sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/boxplots/Pulse-SleepPhase.png) |
| SpO2 in verschiedenen Schlafstadien| ![SpO2 in verschiedenen Schlafstadien sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/boxplots/SpO2-SleepPhase.png) | ![SpO2 in verschiedenen Schlafstadien sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/boxplots/SpO2-SleepPhase.png)| ![SpO2 in verschiedenen Schlafstadien sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/boxplots/SpO2-SleepPhase.png) |
| SpO2 in verschiedenen Apnoe-Phasen| ![SpO2 in verschiedenen Apnoe-Phasen sub20](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject020/boxplots/Apnea-Sp02.png) | ![SpO2 in verschiedenen Apnoe-Phasen sub24](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject024/boxplots/Apnea-Sp02.png)| ![SpO2 in verschiedenen Apnoe-Phasen sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/boxplots/Apnea-Sp02.png) |

## 5. Methoden

In diesem Kapitel werden die Methoden beschrieben, die zur Untersuchung der Fragestellung verwendet werden: 
Inwieweit beeinflusst der Sauerstoffgehalt (SpO2) und der Puls das Auftreten von Apnoe? 
Die hierfür verwendeten Methoden sind ein Entscheidungsbaum, eine multivariate Regression und eine Korrelationsmatrix.

### 5.1 Methode 1: Entscheidungsbaum 

Als erste Methode wurde ein Entscheidungsbaum verwendet, um die Beziehung zwischen dem Sauerstoffgehalt (SpO2), dem Puls und dem Auftreten von Apnoe zu modellieren.

In diesem Modell werden die Daten in Trainings- und Testsets aufgeteilt und ein Entscheidungsbaum trainiert. Die Leistung wird anhand von Metriken wie Genauigkeit und Klassifikationsbericht evaluiert. 

Nachdem der Datensatz aus einer CSV-Dateie geladen wurde, wurden die Variablen _SpO2_ und _Pulse Range_ in numerische Werte konvertiert.
Danach wurden die Merkmale _SpO2_Category_Transformed, Pulse_Range_Transformed, Sleep Stage_ sowie die Zielvariable _Apnea_ aufgeteilt.
Die Daten wurden in Trainings- (80%) und Testdaten (20%) aufgeteilt, um das Modell zu trainieren und zu evaluieren. 
Das Modell wurde mit der Methode _DecisionTreeClassifier_ initialisiert und auf die Trainingsdaten angepasst.
Das Modell wurde mithilfe der Testdaten evaluiert. Die Genauigkeit (Accuracy) und der Klassifikationsbereich (Precision, Recall, F1-Score) wurden berechnet und gespeichert. 
Schlussendlich wurde der Entscheidungsbaum visualisiert, um die Entscheidungsregeln und die Struktur des Baumes zu verstehen.

Nachdem die Größe des Testdatensatzes auf 40% erhöht wurde, zeigt das Modell ähnliche Muster wie zuvor, jedoch mit einem größeren Testdatensatz. Die Herausforderung besteht nun darin, mit dem Klassenungleichgewicht umzugehen.

Accuracy: 0.5180722891566265
**Classification Report:**

|  | precision | recall | f1-score  | support |
|--------|--------|--------|--------|--------|
|Apnea|0.56|0.42|0.48|320|
|Hypoapnea|0.45|0.60|0.51|478|
|Nothing|0.58|0.54|0.56|496|
||||||
|accuracy|||0.52|1494|
|macro avg|0.53|0.52|0.52|1494|
|weighted avg|0.53|0.52|0.52|1494|

![decisionTree sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/decision_tree/decision_tree.png)

**Interpretation der Ergebnisse**
* Hohe Genauigkeit für "Nothing": Das Modell zeigt eine gute Leistung bei der Erkennung von Instanzen, in denen "Noting" vorkommt, was sich in einer höhen _prcision_, einem hohen _recall_ und einem hohen _f1-score_ ezgit. Die Klasse weit auch die höchste Anzahl von Instanzen auf, was die Gesamtgenauigkeit erheblich beeinflusst
* Geringe Leistung bei Apnoe und Hypoapnoe: Das Modell hat Schwierigkeiten Apnoe- und Hypoapnoe-Ereignisse korrekt zu identifizieren, da die _precision_, _recall_ und _f1-score_ fpr beide Klassen niedrig sind. Dies deutet darauf hin, dass das MOdell diese Ereignises weniger gut voneinander und von "Nothing"-Ereignissen unterscheiden kann
* Unausgewogene Klassen: Die UNterstützungswerte zeigen ein erhobeliches Klassenungleichgewicht, mit viel mehr Instanzen kann zu der schlechten Leistung des Modells bei den weniger vertretenen Klassen (Apnoe und Hypoapnoe) beitragen.

Dieses Modell verwendet eine Technik der Random Under Sampling um das Ungleichgewicht zwischen den Klassen zu adressieren. Durch diese Vorverarbeitung werden weniger Instanden der dominanten Klasse ("Nothing") verwendet, um ein ausgewogeneres Trainingsset zu erstellen. Die Leistung des Modells verbessert sich in Bezug auf die Erkennung von Apnoe- Und Hypoapnoe-Ereignissen, obwohl die Gesamtgenauigkeit etwas sinken kann. 

Accuracy: 0.7924211312301661
**Classification Report:**

|  | precision | recall | f1-score  | support |
|--------|--------|--------|--------|--------|
|Apnea|0.42|0.16|0.23|496|
|Hypoapnea|0.46|0.10|0.17|4201|
|Nothing|0.82|0.98|0.89|4201|
||||||
|accuracy|||0.79|5357|
|macro avg|0.57|0.41|0.43|5357|
|weighted avg|0.74|0.79|0.74|5357|

![decisionTree sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/decision_tree/decision_tree.png)
         
**Interpretation der Ergebnisse**

* Verbesserte Balance: Die metriken für Apnoe- und Hypoapnoe-Ereignisse haben sich im verlgiech zu den initalien Ergebnissen verbessert, was darauf hinweist, dass das Modell jetzt besser in der Lage ist, die Klassen zu identifizieren.
* Ausgeglichene Leistung: Die _pecision_, _recall_ und _f1-score_ sin dnun ausgewogener über alle drei Klassen verteilt.
* Recall für Hypoapnoe: Das Modell zeigt einen relativ guten Rückrüf für Hypoapnoe (0.60), was bedeutet, dass es 60% der Hypoapnoe-Instanzen identifiziert. 

Der entsprechende Code ist im folgenden Notebook zu finden: https://github.com/AnnaGass/DSA-SleepHealthData/blob/0ba7a382aff9470d099e13d851e01b85045741f4/DecisionTree.ipynb

### 5.2 Methode 2: multivariante Regression

Als zweite Methode wurde ein multivariantes Regressionsmodell entwickelt, um Apnoe-Ereignisse basierend auf physiologischen Parametern vorherzusagen. Das Modell verwendet die Variablen SpO2, Puls und Schlafstadium als Prädiktoren für das Auftreten von Apnoe. 

Mean Squared Error: 0.4519180140685941R-squared: 0.03946184531819075

|Dep. Variable|Apnea||R-squared|0.036|
|--------|--------|--------|--------|--------|
|Model|OLS||Adj. R-squared|0.035|
|Method|Least Squares||F-statistic|263.0|
|Date|Tue, 25 Jun 2024||Prob (F-statistic)|1.21e-167|
|Time|08:19:46||Log-Likelihood|-21368.|
|No. Observations|21426||AIC|4.274e+04|
|Df Residuals|21426||BIC|4.274e+04|
|Df Model|3||||
|Covariance Type|nonrobust||||

||coef|std err|t|P > t |[0.025|0.975]|
|--------|--------|--------|--------|--------|--------|--------|
|const|5.8791|0.236|24.885|0.000|5.416|6.342|
|SpO2|-0.0525|0.002|-22.001|0.000|-0.057|-0.048|
|Pulse|-0.0094|0.001|-10.582|0.000|-0.011|-0.008|
|Sleep Stage|0.004|0.236|7.019|0.000|0.020|0.036|

|Omnibus|6429.107||Durbin-Watson|1.989|
|--------|--------|--------|--------|--------|
|Prob(Omnibus)|0.000||Jarque-Bera (JB)|14313.476|
|Skew|1.789||Prob(JB)|0.00|
|Kurtosis|4.797||Cond. No.|6.51e+03|

Anmerkung: 
* Die Standardfehler setzen voraus, dass die Kovarianzmatrix der Fehler korrekt angegeben ist
* Die Bedingungszahl ist groß, 6.51e+03. Das könnte darauf hindeuten, dass es starte Multikollinearität oder andere numerische Probleme gibt.


![ResidualPlot sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/regression/Regression_Residual_Plot.png)

![Regression actual vs prdicted sub27](https://github.com/AnnaGass/DSA-SleepHealthData/blob/80036e0f824574d7a01b7340497dc257d724ebe7/results/subject027/regression/Regression_Actual_vs_Predicted_Plot.png)

Das Modell zeigt, dass sowohl die SpO2 als auch der Puls signifikante Prädiktoren für Apnoe sind, obwohl das Modell nur einen kleinen Teil der Varianz (3.3%) in Apnoe erklärt. Weitere Untersuchungen oder zusätzliche Prädiktoren könnten notwendig sein, um ein besser erklärendes Modell zu entwickeln.


Der entsprechende Code ist im folgenden Notebook zu finden: https://github.com/AnnaGass/DSA-SleepHealthData/blob/c499f0f1159e13fe0c054e3f0cc27bda6a2deef9/multivariante_Regression_und_Korrelationsmatrix.ipynb

## 6. Ausblick

Die folgenden Schritte müssen als nächstes durchgeführt werden, um das Projekt weiterzuführen: 

* Wearables-Daten Beschaffen
* Aufbereitung der Wearables-Daten  
* Verbesserung unser Modell mit Wearbelldaten

* Modellanpassung
   * Modelle mehr Trainingsdaten bereitstellen
   * Erweiterung der Analysierten Objekte
   * Fokussierung auf den Wearable Kontext
   * Validierung der Endlösung



 









