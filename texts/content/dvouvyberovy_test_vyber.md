Často je třeba porovnat několik statistických souborů vůči sobě. To znamená, že například u dvou souborů zjišťujeme, jestli některý z nich nemá větší střední hodnotu nebo rozptyl než ten druhý. Pro takový typ úloh budeme používat testy, které jsou navržené na práci s více soubory.

Začneme s dvouvýběrovými testy, tj. testy, které porovnávají právě dva soubory. Na porovnání dvou souborů s normálním rozdělením máme k dispozici hned tři testy: [párový t-test](t_test_parovy.md), [dvouvýběrový (Studentův) t-test](t_test_dvouvyberovy.md) a Welschův t-test. Nyní uvedu tři jednoduché otázky, pomocí kterých dokážeme vybrat správný test:

- Jsou pozorování spárovaná, tj. dokážu jednomu konkrétnímu pozorování z prvního souboru přiřadit právě jedno konkrétní pozorování z druhého souboru? Pokud ano, volíme párový t-test.
- Mají oba soubory shodný rozptyl? Pokud ano, použijeme Dvouvýběrový t-test.
- Máme-li v souborech nespárovaná pozorování a mají-li oba soubory různý rozptyl, volíme Welschův t-test.
