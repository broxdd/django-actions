Tak, bardzo dobrze. Na screenie widać 6 zielonych workflowów dla commita „Optymalizacja GitHub Actions”: Celery, Security, Lint, PostgreSQL, Django CI i Deploy. Zachowaj ten screenshot do zadania 7.

Jedna rzecz: kryterium „pipeline krótszy minimum o 30%” wymagałoby pomiaru przed/po. Sam screen potwierdza poprawne i równoległe działanie, ale nie dowodzi 30%. Nie będziemy tego sztucznie deklarować.

Teraz ostatnie zadanie 8: dokumentacja.

W głównym folderze projektu, tam gdzie `manage.py` i `requirements.txt`, utwórz plik:

```text
README.md
```

Wklej do niego:

```md
# Django GitHub Actions

Projekt demonstracyjny Django wykorzystujący GitHub Actions do CI/CD.

## CI/CD

Projekt posiada automatyczne workflowy GitHub Actions uruchamiane na `ubuntu-latest`.

### Workflowy

#### Django CI - ci.yml

Podstawowy workflow CI.

Wykonuje:
- instalację Python 3.12,
- instalację zależności z requirements.txt,
- migracje Django,
- testy Django.

Pipeline kończy się błędem, jeśli testy nie przejdą.

#### Lint - lint.yml

Kontroluje jakość i formatowanie kodu.

Wykorzystuje:
- flake8,
- black --check,
- isort --check-only.

Błędy formatowania powodują niepowodzenie workflow.

#### PostgreSQL Tests - tests.yml

Uruchamia PostgreSQL jako usługę GitHub Actions.

Wykonuje:
- uruchomienie PostgreSQL,
- konfigurację bazy testowej,
- migracje Django,
- testy integracyjne.

#### Security - security.yml

Automatyczne skanowanie bezpieczeństwa.

Wykorzystuje:
- Bandit,
- Safety,
- pip-audit.

pip-audit sprawdza zależności Python pod kątem znanych podatności.
Wykrycie podatności powoduje niepowodzenie pipeline.

Skan bezpieczeństwa może być również wykonywany cyklicznie.

#### Deploy - deploy.yml

Workflow uruchamiany dla brancha main.

Wykonuje:
- budowę obrazu Docker,
- logowanie do GitHub Container Registry,
- publikowanie obrazu w registry.

Obrazy posiadają tag `latest` oraz tag odpowiadający SHA commita.
Tag SHA umożliwia wykorzystanie konkretnej wcześniejszej wersji obrazu podczas rollbacku.

Uwaga: publikacja obrazu w registry jest przygotowaniem do wdrożenia. Pełne wdrożenie aplikacji na serwer wymaga skonfigurowanego serwera docelowego.

#### Celery Redis Tests - celery.yml

Uruchamia środowisko do testowania zadań asynchronicznych.

Wykorzystuje:
- Redis,
- Celery worker,
- testy tasków Django/Celery.

## GitHub Secrets

Projekt wykorzystuje następujący sekret:

- `SECRET_KEY` - klucz Django.

Sekrety konfiguruje się w:

Settings -> Secrets and variables -> Actions

Wartości sekretów nie powinny być umieszczane bezpośrednio w kodzie ani repozytorium.

## Uruchamianie pipeline

Workflowy uruchamiają się automatycznie po wykonaniu `push` do brancha `main` oraz dla Pull Requestów do `main`.

Kod można wysłać za pomocą:

git add .
git commit -m "Opis zmian"
git push

Status wykonania znajduje się w zakładce `Actions` repozytorium GitHub.

## Optymalizacja

Workflowy wykorzystują:
- cache zależności pip,
- równoległe wykonywanie niezależnych workflowów,
- ograniczone triggery,
- concurrency z `cancel-in-progress`.

Opcja `cancel-in-progress` pozwala anulować starszy workflow po wysłaniu nowszego commita.

## Debugowanie

Jeśli workflow zakończy się błędem:

1. Otwórz zakładkę Actions.
2. Wybierz czerwony workflow.
3. Otwórz nieudany job.
4. Rozwiń krok oznaczony na czerwono.
5. Sprawdź komunikat błędu.
6. Popraw problem lokalnie.
7. Wykonaj ponownie commit i push.

## Rollback

Obrazy Docker są oznaczane SHA commita.

Dzięki temu można wskazać wcześniejszą wersję obrazu zamiast `latest` i ponownie uruchomić aplikację z poprzedniej wersji.

## Technologie

- Django
- Python 3.12
- GitHub Actions
- PostgreSQL
- Redis
- Celery
- Docker
- Flake8
- Black
- isort
- Bandit
- Safety
- pip-audit
```

Teraz zapisz `README.md`.

Potem:

```powershell
git add README.md
git commit -m "Dodanie dokumentacji CI CD"
git push
```

Po pushu przejdź na główną stronę repozytorium:

```text
GitHub → Code
```

Przewiń w dół. GitHub automatycznie wyświetli zawartość `README.md`.

Zrób screenshot sekcji `CI/CD` oraz listy workflowów. To będzie główny dowód do zadania 8.

Po wykonaniu tego będziemy mieli zrobione zadania 1–4 oraz 6–8, a w zadaniu 5 działające budowanie i publikację obrazu Docker. Do pełnego zadania 5 pozostaje faktyczny deploy na serwer i działający rollback, bo do tego potrzebujemy określić, gdzie aplikacja ma zostać wdrożona.