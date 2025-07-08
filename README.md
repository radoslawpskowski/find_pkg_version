🔍 Wyszukiwanie pakietu na agentach Wazuh (find_pkg.py)
Ten skrypt umożliwia szybkie sprawdzenie, na których agentach Wazuh zainstalowany jest dany pakiet systemowy (np. perl-Git) oraz wyświetla jego wersję.

⚙️ Jak to działa:
Autoryzacja do API Wazuh:
Skrypt loguje się do Wazuh REST API (lokalnie, po HTTPS) i pobiera token autoryzacyjny.

Pobieranie listy agentów:
Pobierana jest pełna lista agentów (ID i nazwa hosta), które później są mapowane do wyników.

Wprowadzenie nazwy pakietu:
Użytkownik podaje nazwę pakietu do wyszukania.

Przeszukiwanie pakietów zainstalowanych na agentach:
Dla agentów o ID od 000 do 020 (czyli do 21 agentów), wysyłane jest zapytanie o zainstalowane pakiety.
Jeśli pakiet o podanej nazwie zostanie znaleziony, wypisywana jest:

nazwa hosta agenta,

nazwa pakietu,

wersja pakietu.

🛡️ Uwaga:
Połączenia są realizowane bez weryfikacji certyfikatu SSL (verify=False) – może być to ryzykowne w środowisku produkcyjnym.

Dane logowania do API są zapisane w kodzie – zalecane jest ich przeniesienie do zmiennych środowiskowych lub pliku .env.

✅ Przykładowe użycie:
ruby
Kopiuj
Edytuj
$ python3 find_pkg.py
wprowadz nazwe poszukiwanego pakietu: perl-Git
host01
nazwa pakietu perl-Git wersja 2.43.0-150600.3.6.1
host02
nazwa pakietu perl-Git wersja 2.43.0-150600.3.6.1
host03
nazwa pakietu perl-Git wersja 2.43.5-3.el8_10
📦 Wymagania:
Python 3

Pakiety: requests, urllib3

