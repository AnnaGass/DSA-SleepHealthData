# DSA-SleepHealthData

**Thema**: Schlafapnoe-Erkennung mittels Wearable-Daten: Ein Modell basierend auf klinischen Daten

**Team**: HeartDataSquad

**Team-Mitglieder**: Alejandro Restrepo Klinge,
Anna Gaßmann,
Yusuf Özdemirkan,
Sofie Haas,
Tristan Gräble,
David Silva Goncalves

**Zeitraum des Semesterprojekts**: 03.04.2024 - 03.07.2024 

## 1. Beschreibung der Problematik
## 1.1. Hintergrund
Schlafapnoe ist eine weit verbreitete, aber oft unbemerkte schlafbezogene Atemstörung, die durch wiederholte Atemaussetzer während des Schlafs gekennzeichnet ist.
Diese Unterbrechungen führen zu einer verminderten Sauerstoffversorgung des Körpers und stören das natürliche Schlafmuster.
Der Schweregrad der nächtlichen Atemaussetzer wird anhand des AHI (Apnoe-Hypopnoe-Index) klasifiziert: 
* Leicht 5–15 Atemaussetzer/Minute
* Mittel 15–30 Atemaussetzer/Minute
* Schwer > 30 Atemaussetzer/Minute

Unbehandelt kann Schlafapnoe zu ernsthaften gesundheitlichen Problemen wie Herz-Kreislauf-Erkrankungen, Diabetis und Schlaganfall führen.
Aktuell erfolgt die Diagnose hauptsächlich durch aufwändige Polysomnographie-Tests in spezialisierten Schlaflaboren. Diese Tests erfordern, dass Patienten über Nacht in der Klink bleiben und an verschiedenen Sensoren angeschlossen werden, was logistisch als auch finanziell belastend ist und sich nicht für eine langfristige Überwachung eignet. Zudem können die Ergebnisse durch die ungewohnte, klinische Umgebung verzerrt sein.

## 1.2. Mögliche Lösungen durch das Projekt
Dieses Projekt zielt darauf ab, Schlafapnoe mithilfe von Wearable-Daten zu erkennen und die Nutzer über das mögliche Bestehen einer Schlafapnoe zu informieren. Dafür soll ein Modell mithilfe von klinischen Daten (siehe Kapitel 4.2 Mögliche Datenquellen) entwickelt werden. Durch die frühzeitige Erkennung von Schlafapnoe können Betroffenen eine ärztliche Behandlung aufsuchen und dadurch das Risiko für die oben genannten Erkrankungen reduzieren. Wearables können im Alltag, beim Sport und in Ruhephasen getragen werden. Dadurch entfällt die Notwendigkeit einer Übernachtung in einem Schlaflabor, und die Nutzer können sich in ihrer gewohnten Umgebung befinden, was die Daten nicht verfälscht. Zudem ermöglicht die nächtliche und regelmäßige Überwachung des Schalfs durch Wearables eine genauere Beurteilung der Schlafqualität.

## 2. Projektziele

### 2.1. Projektziel - Preparation of Data
Gewinnung und Konvertierung von klinischen Daten in für das Modell nutzbare Daten.

![Preparation of Data](https://raw.githubusercontent.com/AnnaGass/DSA-SleepHealthData/c90d1071f9640b0ab6695decd131f6dafb6a4f42/Flow1.drawio.png)

### 2.2. Projektziel - Data Analysis + Model Creation
Analyse der Daten und Entwicklung eines Modells zur Erkennung von Schlafapnoe-Phasen durch die Nutzung von klinischen Messdaten (siehe Kapitel 3a)
Klassifizierung der Schlafapnoe nach dem Apnoe-Hypopnoe-Index (AHI)

![Data Analysis + Model Creation](https://github.com/AnnaGass/DSA-SleepHealthData/blob/34ccfd4f38311f0dfc050df18122f38fbaeb79b6/flows/Flow2.drawio.png)


### 2.3. Projektziel - Hypothesis Validation
Validierung der Hypothese und Testen des Modells

![Hypothesis Validation](https://github.com/AnnaGass/DSA-SleepHealthData/blob/354c2d079c5b08daed40b96d017ccceba6922886/Flow3.drawio.png)


Aus den einzelnen Flows ergibt sich dieser Gesamtflow, entsprechend der Architektur des Projektes (s. Kapitel 3.3): 

![Complete Flow](https://github.com/AnnaGass/DSA-SleepHealthData/blob/354c2d079c5b08daed40b96d017ccceba6922886/CompleteFlow.drawio.png)

## 3. Erste technische Dokumentation

### 3.1 Datenquellen
Die zur Modellerstellung verwendeten Forschungsdaten stammen aus dem St. Vincent´s University Hospital / University College Dublin Schlafapnoe-Datenbank. Diese Datenbank enthält 25 vollständige Übernacht-Polysomnogramme von erwachsenen Personen mit Verdacht auf obstruktive Schlafapnoe, zentrale Schlafapnoe oder primärem Schnarchen. Die überarbeitete Version dieser Datenbank wurde am 01.09.2011 veröffentlicht. Allgemeine Informationen zu den Patienten (BMI, Alter, AHI-Index, Körpergröße,...) sind in der Datei SubjectDetails.xls dargestellt.

Die gesamten Daten sind unter der folgenden Quelle zu finden: https://physionet.org/content/ucddb/1.0.0/ (Stand 08.05.2024)

Folgende Abbildung fasst die wichtigsten Daten der Datenbank zusammen:

![Database](https://github.com/AnnaGass/DSA-SleepHealthData/blob/79dcf71dce61faea7d92affa54ff811221a08e3b/Database.drawio.png)

Zu Erstellung des klinischen Modells werden drei Patienten der genannten Forschung ausgewählt. Die Patienten werden anhand des AHI-Index aus der Datei SubjectDetails.xls gewählt.
Dabei werden der Patient mit dem höchsten AHI-Index, der Patient mit dem niedrigsten AHI-Index und ein Patient mit einem dazwischenliegenden Wert gewählt, um eine möglichst große Verteilung des AHI-Index zu haben.

Die Entscheidung für diese Daten fiel anhand der folgenden Kriterien (sortiert nach Wichtigkeit): 
1. Die Daten sind repräsentativ und gültig, da keine leeren Werte vorhanden sind, ebenso treten keine zeitlichen Lücken auf
2. Die Quelldaten sind weder komprimiert, noch gekürzt
3. Vielzahl an Patientendaten verfügbar
4. Zusätzliche Annotationen vorhanden, sodass das Gesamtbild nachvollzogen werden kann
5. Quelle ist eine Kooperation der St. Vincent´s University Hospital / University College Dublin. Dies macht die Daten zu glaubwürdigen Daten
6. Es gibt eine "Open Data Commons Attribution License V1.0"
7. Es gibt zitierfähige Publikationen (z.B. https://ieeexplore.ieee.org/document/9864566)

### 3.2 Installationsanleitung

1. **Öffnen Sie Google Colab**  
   Besuchen Sie Google Colab in Ihrem Webbrowser.

2. **Fügen Sie Ihr Repository hinzu**  
   Klicken Sie auf "Datei" > "Github" in Google Colab und fügen Sie dieses Repository hinzu. 
   https://github.com/AnnaGass/DSA-SleepHealthData.git

1. **Notebook auswählen**  
   Die Datei "Notebook.ipynb" aus diesem Repository auswählen.

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

#### Datenverarbeitung
Nach dem Herunterladen der Daten folgt die Verarbeitung:

* Signalverarbeitung: Die Rohsignale (z.B. SpO2, Puls) werden aus den .rec Dateien extrahiert und in CSV-Dateien formatiert.
* Annotationsextraktion: Schlafstadien und Atmungsereignisse werden aus den entsprechenden .txt Dateien gelesen und ebenfalls in CSV umgewandelt.

Diese Prozesse nutzen Python-Bibliotheken wie pyedflib für das Lesen von EDF-Dateien und pandas für die Datenmanipulation.

#### Modellentwicklung und Datenanalyse
Die verarbeiteten Daten werden anschließend analysiert, um Muster zu erkennen und Vorhersagemodelle zu erstellen. Dabei kann auch auf maschinelles Lernen zurückgegriffen werden.

Beispiele dazu wären:
* Feature Engineering: Es werden relevante Merkmale aus den Signalen abgeleitet, die für die Vorhersage von Schlafapnoe nützlich sind.
* Modelltraining: Verschiedene Modelle werden trainiert und evaluiert, um das effektivste zu identifizieren.

#### Visualisierung
Zur Überprüfung der Datenqualität und zur Darstellung der Analyseergebnisse werden Visualisierungen verwendet. 'matplotlib' und 'plotly' bieten Funktionen, um die Zeitreihen der biologischen Signale sowie die Ergebnisse der Modellvorhersagen graphisch darzustellen.

#### Technologien
* Python: Als Hauptprogrammiersprache für das Projekt
* Jupyter Notebook: Um die Übersicht des Projekts zu erleichtern
