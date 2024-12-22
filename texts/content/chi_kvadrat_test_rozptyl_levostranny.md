V článku si vysvětlíme, jak bychom provedli levostranný test, tentokrát již bez slovního zadání. Důvodem je, abychom si ukázali chování funkcí pro $ \chi^2$ při levostranném testu. 

V případě levostranného testu budeme mít následující hypotézy:

* Nulová hypotéza: Rozptyl je 0,64. ($ H_0: \sigma^2 = 0{,}64 $)
* Alternativní hypotéza: Rozptyl je menší než 0,64. ($ H_1: \sigma^2 < 0{,}64 $)

Soubor s daty a výpočty naleznete [zde](media/chi-kvadrat-test-rozptyl-levostranny/test-rozptyl.xlsx)

## Výpočet v Excelu

Pro určení hranice kritického oboru u levostranného testu je výhodnější standardní kvantilová funkce CHISQ.INV:

```
=CHISQ.INV(D5;D2-1)
```

Protože rozdělení $ \chi^2$ nabývá pouze kladných hodnot, kritický obor zapsaný intervalem je:

$ W = \langle 0, 10{,}1170 \rangle \, .$

Hodnota statistiky $ T = 9{,}0587$ leží v kritickém oboru, proto na dané hladině významnosti zamítáme nulovou hypotézu.

Vzorec pro výpočet p-hodnoty testu je u standardní distribuční funkce opět jednoduchý:

```
=CHISQ.DIST(D8;D2-1;TRUE)
```

U pravostranné distribuční funkce je opět třeba odečíst výslednou hodnotu od jedničky.

```
=1-CHISQ.DIST.RT(D8;D2-1)
```

Správně vidíme, že p-hodnota $ 0{,}0275$ je nižší než hladina významnosti, což potvrzuje náš předchozí závěr o zamítnutí nulové hypotézy.
