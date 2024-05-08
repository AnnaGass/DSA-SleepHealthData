# DSA-SleepHealthData

Thema: Prävention von Herz-Kreislauferkrankungen mittels Wearables (Fokus
auf Schlafapnoe)

Team: HeartDataSquad

Team-Mitglieder: Alejandro Restrepo Klinge,
Anna Gaßmann,
Yusuf Özdemirkan,
Sofie Haas,
Tristan Gräble,
David Silva Goncalves

Zeitraum von dem Semesterprojekt: 03.04.2024 - 03.07.2024 

## 1. Beschreibung der Problematik
## a. Hintergrund
Schlafapnoe ist eine weit verbreitete, aber oft unbemerkte schlafbezogene Atemstörung, die durch wiederholte Atemaussetzer während des Schlafs gekennzeichnet ist.
Diese Unterbrechungen führen zu einer verminderten Sauerstoffversorgung des Körpers und stören das natürliche Schlafmuster.
Unbehandelt kann Schlafapnoe zu ernsthaften gesundheitlichen Problemen wie Herz-Kreislauf-Erkrankungen, Diabetis und Schlaganfall führen.
Aktuell erfolgt die Diagnose hauptsächlich durch aufwändige Polysomnographie-Tests in spezialisierten Schlaflaboren. Diese Tests erfordern, dass Patienten über Nacht in der Klink bleiben und an verschiedenen Sensoren angeschlossen werden, was logistisch als auch finanziell belastend ist und sich nicht für eine langfristige Überwachung eignet. Zudem können die Ergebnisse durch die ungewohnte, klinische Umgebung verzerrt sein.

## b. Mögliche Lösungen durch das Projekt
Dieses Projekt zielt darauf ab, Schlafapnoe mithilfe von Wearable-Daten zu erkennen und die Nutzer über das mögliche Bestehen einer Schlafapnoe zu informieren. Dafür soll ein Modell mithilfe von klinischen Daten entwickelt werden. Durch die frühzeitige Erkennung von Schlafapnoe können Betroffenen eine ärztliche Behandlung aufsuchen und dadurch das Risiko für die oben genannten Erkrankungen reduzieren. Wearables können im Alltag, beim Sport und in Ruhephasen getragen werden. Dadurch entfällt die Notwendigkeit einer Übernachtung in einem Schlaflabor, und die Nutzer können sich in ihrer gewohnten Umgebung befinden, was die Daten nicht verfälscht. Zudem ermöglicht die nächtliche und regelmäßige Überwachung des Schalfs durch Wearables eine genauere Beurteilung der Schlafqualität.

## 2. Projektziele

### a. Projektziel - Preparation of Data
Gewinnung und Konvertierung von klinische Daten in für das Modell nutzbare Daten

![Preparation of Data](https://raw.githubusercontent.com/AnnaGass/DSA-SleepHealthData/c90d1071f9640b0ab6695decd131f6dafb6a4f42/Flow1.drawio.png)

### b. Projektziel - Data Analysis + Model Creation
Analyse der Daten und Entwicklung eines Modells zur Erkennung von Schlafapnoe-Phasen durch die Nutzung von klinischen Messdaten (siehe Kapitel 3a)
Klassifizierung der Schlafapnoe nach dem Apnoe-Hypopnoe-Index (AHI)

![Data Analysis + Model Creation](https://github.com/AnnaGass/DSA-SleepHealthData/blob/34ccfd4f38311f0dfc050df18122f38fbaeb79b6/flows/Flow2.drawio.png)


### c. Projektziel - Hypothesis Validation
Validierung der Hypothese und Testen des Modells

![Hypothesis Validation](https://github.com/AnnaGass/DSA-SleepHealthData/blob/354c2d079c5b08daed40b96d017ccceba6922886/Flow3.drawio.png)


Aus den einzelnen Flows ergibt sich dieser Gesamtflow: 

![Complete Flow](https://github.com/AnnaGass/DSA-SleepHealthData/blob/354c2d079c5b08daed40b96d017ccceba6922886/CompleteFlow.drawio.png)

## Erste technische Dokumentation


## Technische Dokumentation
### Architektur
### Mögliche Datenquellen
Die Daten für unsere Forschung stammen aus dem St. Vincent´s University Hospital / University College Dublin Schlafapnoe-Datenbank. Diese Datenbank enthält 25 vollständige Übernacht-Polysomnogramme von erwachsenen Personen mit Verdacht auf schlafbezogene Atmungsstörungen. Die überarbeitete Version dieser Datenbank wurde am 01.09.2011 veröffentlicht. 

Die Daten sind unter dieser Quelle zu finden: https://physionet.org/content/ucddb/1.0.0/

Zusammenfassend könnten potenzielle Datenquellen für unsere Forschung die St. Vincent´s University Hospital / University College Dublin Schlafapnoe-Datenbank selbst, begleitende Dokumentationen und Protokolle, wissenschaftliche Publikationen und Forschungsstudien sein, die auf dieser Datenbank basieren.

## Installationsanleitung

1. **Öffnen Sie Google Colab**  
   Besuchen Sie Google Colab in Ihrem Webbrowser.

2. **Fügen Sie Ihr Repository hinzu**  
   Klicken Sie auf "Datei" > "Github" in Google Colab und fügen Sie dieses Repository hinzu.

3. **Wählen Sie Ihr Notebook aus**  
   Suchen Sie das "Notebook.ipynb" im hinzugefügten Repository und wählen Sie es aus.

4. **Wählen Sie das Subjekt aus**  
   Hierzu muss im Notebook im ersten Schritt das Subjekt ausgewählt werden. Hierbei muss es eine Zahl zwischen 001-028 sein.

6. **Führen Sie das Notebook aus**  
   Starten Sie das Notebook und lassen Sie es laufen. **Alle benötigten Installationen sind bereits im Notebook enthalten. Bei der Ausführung der Schritte werden automatisch alle Schritte gemacht.**

7. **Überprüfen Sie die Ergebnisse**  
   Überprüfen Sie die Ausgabe des Notebooks auf etwaige Fehler oder Warnungen. Stellen Sie sicher, dass das Modell ordnungsgemäß erstellt und validiert wurde.

