Microsoft Excel obsahuje funkci Z.TEST pro provedení z-testu, která vrací p-hodnotu testované hypotézy. Bohužel je standardně tato funkce napsána pro provedení jednostranného testu pro nulovou hypotézu, že střední hodnota souboru větší než zadaná střední hodnota.

Pokud provádíme oboustranný test, který je popsaný v článku o [z-testu](z_test_excel.md), musíme výstup funkce mírně upravit. Proveďme následující úvahu.

* Pokud je průměr náhodného výběru větší než teoretická střední hodnota, vrací nám funkce Z.TEST p-hodnotu menší než 0,5. Takovou p-hodnotu můžeme použít. Protože však provádíme oboustranný test, pro náš výsledek násobíme ještě tuto hodnotu dvěma.
* Pokud je průměr náhodného výběr menší než teoretická střední hodnota, vrací nám funkce Z.TEST p-hodnotu větší než 0,5. V takovém případě odečteme tuto p-hodnotu od jedničky a výsledek násobíme dvěma.

Pro výpočet můžeme použít funkci MIN, která nám vrátí menší hodnotu z obou variant. Výsledek násobíme dvěma. Výsledný vzorec vypadá takto:

<pre>=2*MIN(Z.TEST(A1:A20;D5;D4);1-Z.TEST(A1:A20;D5;D4))</pre>

Pro snazší pochopení se podívejte na obrázky níže. Na prvním jsou zeleně a modře obě varianty výsledků získaných z funkce Z.TEST. Z nich vybíráme tu menší, tj. modrou plochu. To provádí funkce MIN. Modrou plochu pak násobíme dvěma a získáme výslednou p-hodnotu.
