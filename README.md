# DSA-SleepHealthData

## 1. Beschreibung der Problematik
## a. Hintergrund
Schlafapnoe ist eine weit verbreitete, aber oft unbemerkte schlafbezogene Atemstörung, die durch wiederholte Atemaussetzer während des Schlafs gekennzeichnet ist.
Diese Unterbrechungen führen zu einer verminderten Sauerstoffversorgung des Körpers und stören das natürliche Schlafmuster.
Unbehandelt kann Schlafapnoe zu ernsthaften gesundheitlichen Problemen wie Herz-Kreislauf-Erkrankungen, Diabetis und Schlaganfall führen.
Aktuell erfolgt die Diagnose hauptsächlich durch aufwändige Polysomnographie-Tests in spezialisierten Schlaflaboren. Diese Tests erfordern, dass Patienten über Nacht in der Klink bleiben und an verschiedenen Sensoren angeschlossen werden, was logistisch als auch finanziell belastend ist und sich nicht für eine langfristige Überwachung eignet. Zudem können die Ergebnisse durch die ungewohnte, klinische Umgebung verzerrt sein.

## b. Mögliche Lösungen durch das Projekt
Dieses Projekt zielt darauf ab, Schlafapnoe mithilfe von Wearable-Daten zu erkennen und die Nutzer über das mögliche Bestehen einer Schlafapnoe zu informieren. Dafür soll ein Modell mithilfe von klinischen Daten entwickelt werden. Durch die frühzeitige Erkennung von Schlafapnoe können Betroffenen eine ärztliche Behandlung aufsuchen und dadurch das Risiko für die oben genannten Erkrankungen reduzieren. Wearables können im Alltag, beim Sport und in Ruhephasen getragen werden. Dadurch entfällt die Notwendigkeit einer Übernachtung in einem Schlaflabor, und die Nutzer können sich in ihrer gewohnten Umgebung befinden, was die Daten nicht verfälscht. Zudem ermöglicht die nächtliche und regelmäßige Überwachung des Schalfs durch Wearables eine genauere Beurteilung der Schlafqualität.

## 2. Projektziele
### a. Projektziel
Entwicklung eines Modells zur Erkennung von Schlafapnoe-Phasen durch die Nutzung von klinischen Messdaten (siehe Kapitel 3a)
### b. Projektziel
Gewinnung und Konvertierung von Wearable-Daten in für das Modell nutzbare Daten
### c. Projektziel
Klassifizierung der Schlafapnoe nach dem Apnoe-Hypopnoe-Index (AHI)

## Erste technische Dokumentation

## Projektskizze
Nach der ersten Analyse sind folgende Werte für die Indentifizierung des Schalfaphnoes wichtig:
- Puls
- Atemfrequenz
- Sauerstoffsättigung
- Schlafphase
- Bewegungsdaten (Augen, Arme, Beine)
- Generelle Daten (Alter, Geschlecht, Gewicht, Lebensstil usw.)
- Pulsvariabilität
- Hirnaktivität (Schlaflabor)
- Elektrokardiogramm (EKG)
- Körpertemperatur



## Technische Dokumentation
### Architektur
### Mögliche Datenquellen
