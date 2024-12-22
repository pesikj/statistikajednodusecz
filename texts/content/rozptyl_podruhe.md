V popisu [výběrového rozptylu](rozptyl.md) chybí důkaz nebo jakékoli vysvětlení, proč je zavedení výběrového rozptylu vlastně potřeba a proč vzorec na rozptyl nelze použít pro nestranný odhad. Tomu se budeme věnovat nyní. 

Nejprve si odvodíme takzvaný **výpočetní tvar pro rozptyl**. Víme, že populační rozptyl se spočte pomocí vztahu

$ \sigma^2_X = \mathrm{E} \left[ X - \mathrm{E} \left(X \right) \right]^2 \, .$

Pro výpočet hodnoty rozptylu pomocí kalkulačky je tento vzorec poměrně nepraktický, protože pro každou hodnotu souboru je potřeba zadat rozdíl mezi danou hodnotou a střední hodnotou. Můžeme ale provést následující úpravy:

$ \begin{aligned}  
 \sigma^2_X &= \mathrm{E} \left[ X - \mathrm{E} \left(X \right) \right]^2 \\  
 &= \mathrm{E} \left[ X^2 - 2 X \cdot \mathrm{E} \left(X \right) + \mathrm{E} \left(X \right) \right] \\  
 &= \mathrm{E} \left( X^2 \right) - \mathrm{E} \left[ 2 X \cdot \mathrm{E} \left(X \right) \right] + \left[ \mathrm{E} \left(X \right) \right]^2 \\  
 &= \mathrm{E} \left( X^2 \right) - 2 \left[ \mathrm{E} \left(X \right) \right]^2 + \left[ \mathrm{E} \left(X \right) \right]^2 \\  
 &= \mathrm{E} \left( X^2 \right) - \left[ \mathrm{E} \left(X \right) \right]^2  
 \end{aligned}\, . $

Výsledný výpočetní tvar pro rozptyl má tvar

$ \sigma^2_X = \mathrm{E} \left( X^2 \right) - \left[ \mathrm{E} \left(X \right) \right]^2 = \mathrm{E} \left( X^2 \right) - \mu_X^2  \, . $

Stačí tedy vypočítat součet druhých mocnin hodnot souboru a odečíst od něj druhou mocninu součtu hodnot, což rychlost výpočtu podstatně sníží. Tento vztah ještě využijeme níže.

Nyní se ale vraťme k výběrovému rozptylu. Jestliže máme k dispozici pouze náhodný výběr z nějakého souboru (a nikoli všechny hodnoty souboru), zpravidla **nebudeme znát střední hodnotu** základního souboru. Tuto střední hodnotu musíme **odhadnout pomocí aritmetického průměru**. Dokažme si nejprve, že aritmetický průměr je **nezkresleným odhadem** střední hodnoty, tj. určíme si střední hodnotu aritmetického průměru:

$ \mathrm{E} \left( \bar{X} \right) = \mathrm{E} \left( \frac{1}{n} \sum\limits_{i=1}^n x_i \right) = \frac{1}{n} \sum\limits_{i=1}^n \mathrm{E} \left( x_i \right) = \frac{1}{n} \cdot n \cdot \mu = \mu \, .$

Využíváme dvou známých vlastností střední hodnoty. Při násobení náhodné veličiny konstantou $ c \in \mathbb{R} $ platí, že

$ \mathrm{E} \left( c \cdot X \right) = c \cdot \mathrm{E} \left( X \right) \, . $

A dále střední hodnota součtu náhodných veličin se rovná součtu středních hodnot náhodných veličin:

$ \mathrm{E} \left( X + Y \right) = \mathrm{E} \left( X \right) + \mathrm{E} \left( Y \right) \, . $

Střední hodnota aritmetického průměru je tedy skutečně střední hodnotou náhodného výběru, tím pádem je dokázáno, že takový odhad je **nezkreslený**. Vraťme se nyní ke vzorci pro populační rozptyl:

$ \sigma^2_X = \frac{1}{n} \sum\limits_{i=1}^{n} \left[ x_i - \mathrm{E} \left(X \right) \right]^2 \, .$

Namísto střední hodnoty nyní do vzorce dosadíme aritmetický průměr. Takto upravenou statistiku si označíme jako $ \left(s^{'} \right)^2_X $:

$ \left(s^{'} \right)^2_X = \frac{1}{n} \sum\limits_{i=1}^{n} \left( x_i - \bar{X} \right)^2 \, . $

Nyní použijeme známý vzorec $ (a + b)^2 = a^2 + 2ab + b^2 $ a provedeme několik jednoduchých úprav.

$ \begin{aligned}  

\left(s^{'} \right)^2_X &= \frac{1}{n} \sum\limits_{i=1}^{n} \left( x_i^2 - 2 x_i \bar{X}  + \bar{X}^2 \right) \\  

&= \frac{1}{n} \sum\limits_{i=1}^{n} x_i^2 - 2 \bar{X} \frac{\sum\limits_{i=1}^{n}x_i}{n}  + \frac{n \cdot \bar{X}^2}{n} \\  

&= \frac{1}{n} \sum\limits_{i=1}^{n} x_i^2 - 2 \bar{X} \cdot \bar{X} + \bar{X}^2 \\  

&= \frac{1}{n} \sum\limits_{i=1}^{n} x_i^2 - \bar{X}^2 \\  

&= \frac{1}{n} \sum\limits_{i=1}^{n} x_i^2 - \left( \frac{1}{n} \sum\limits_{i=1}^{n} x_i \right)^2  

\end{aligned}\, . $

V případě druhého sčítance na posledním řádku provádíme součet vzájemných násobků hodnot v náhodném výběru. Výraz lze zapsat též jako

$ \frac{1}{n^2} \left( \sum\limits_{i=1}^{n} x_i \right) \left( \sum\limits_{i=1}^{n} x_i \right) = \frac{1}{n^2} \left( \sum\limits_{i=1}^{n} x_i^2 +  \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} x_i x_j \right) \, ,$

protože rozlišujeme mezi případy, kdy jsou mezi sebou násobeny dva různé náhodné výběry, a kdy je násobena tatáž realizace náhodného výběru. Tím jsme získali upravený vzorec pro statistiku $ \left(s^{'} \right)^2_X $:

$ \left(s^{'} \right)^2_X = \frac{1}{n} \sum\limits_{i=1}^{n} x_i^2 - \frac{1}{n^2} \left( \sum\limits_{i=1}^{n} x_i^2 +  \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} x_i x_j \right) \, .$

Abychom si ukázali, jak je statistika $ \left(s^{'} \right)^2_X $ zkresleným odhadem rozptylu, určíme si její střední hodnotu:

$ \begin{aligned}  

\mathrm{E} \left[ \left( s^{'} \right)^2_X \right] &= \mathrm{E} \left[ \frac{1}{n} \sum\limits_{i=1}^{n} x_i^2 - \frac{1}{n^2} \left( \sum\limits_{i=1}^{n} x_i^2 +  \sum\limits_{i=1}^{n} \sum\limits_{j=1}^{n} x_i x_j \right) \right] \\  

&= \frac{1}{n} \sum\limits_{i=1}^{n} \mathrm{E} \left( x_i^2 \right) - \frac{1}{n^2} \left[ \sum\limits_{i=1}^{n} \mathrm{E} \left( x_i^2 \right) + \sum\limits_{\substack{ i=1 \\ i \neq j}}^{n} \sum\limits_{j=1}^{n} \mathrm{E} \left( x_i x_j \right) \right]  

\end{aligned}$

Uvažujeme, že jednotlivé realizace náhodného výběru jsou vzájemně nezávislé, tj. hodnoty $ x_i $ a $ x_j$ jsou pro $ i \neq j $ nezávislé. V tom případě pak platí vztah

$ \mathrm{E} \left( x_i x_j \right) = \mathrm{E} \left( x_i \right) \mathrm{E} \left( x_j \right) \, .$

Protože se ale v obou případech jedná o náhodný výběr ze stejného souboru se střední hodnotou $ \mu$, platí dokonce

$ \mathrm{E} \left( x_i x_j \right) = \mathrm{E} \left( x_i \right) \mathrm{E} \left( x_j \right) =  \mu \cdot \mu = \mu^2 \, .$

Dále máme v rovnici výraz $ \mathrm{E} \left( x_i^2 \right) $. Upravíme-li si rovnici pro výpočetní tvar rozptylu, kterou jsme odvodili výše, zjistíme, že

$ \mathrm{E} \left( X^2 \right) = \sigma^2_X + \mu_X^2 \, . $

Dosaďme tedy za oba výrazy a pokračuje v odvození

$ \begin{aligned}  

\mathrm{E} \left[ \left( s^{'} \right)^2_X \right] &=  

\frac{1}{n} \sum\limits_{i=1}^{n} \mathrm{E} \left( x_i^2 \right) - \frac{1}{n^2} \left[ \sum\limits_{i=1}^{n} \mathrm{E} \left( x_i^2 \right) + \sum\limits_{\substack{ i=1 \\ i \neq j}}^{n} \sum\limits_{j=1}^{n} \mathrm{E} \left( x_i x_j \right) \right] \\  

&=  

\frac{1}{n} \sum\limits_{i=1}^{n} \left( \sigma^2_X + \mu_X^2 \right) - \frac{1}{n^2}  \sum\limits_{i=1}^{n} \left( \sigma^2_X + \mu_X^2 \right) + \sum\limits_{\substack{ i=1 \\ i \neq j}}^{n} \sum\limits_{j=1}^{n} \mu^2 \\  

&= \left( \sigma^2_X + \mu_X^2 \right) - \frac{n}{n^2} \left( \sigma^2_X + \mu_X^2 \right) -\frac{(n^2 - n)}{n^2}  \mu^2 \\  

&= \sigma^2_X \left( 1 - \frac{n}{n^2} \right) + \mu_X^2 \left[ 1 - \frac{n}{n^2} + \frac{(n^2 - n)}{n^2} \right] \\  

&= \sigma^2_X \frac{n \left( n - 1 \right) }{n^2} + \mu_X^2 \frac{n^2 - n - n^2 + n}{n^2}\\  

&= \sigma^2_X \frac{ n - 1}{n}  

\end{aligned}$

Vidíme tedy, že střední hodnota statistiky $ \left(s^{'} \right)^2_X $ je

$ \left[ \left( s^{'} \right)^2_X \right] = \sigma^2_X \frac{ n - 1}{n} \, . $

Abychom tedy získali nezkreslený odhad rozptylu, museli bychom statistiku $ \left(s^{'} \right)^2_X $ násobit výrazem $ \frac{n}{n -1} $. Na základě této myšlenky je pak odvozen vzorec pro výběrový rozptyl. Výraz $ \frac{n}{n -1}$ je někdy nazýván jako [Besselova korekce](https://en.wikipedia.org/wiki/Bessel%27s_correction). Výraz $ \frac{n}{n -1}$ konverguje k 1, pro velmi velké náhodné výběry je rozdíl mezi statistikami zanedbatelný. Protože střední hodnota statistiky $ \left(s^{'} \right)^2_X $ konverguje k hodnotě rozptylu, je **asymptoticky nestranným odhadem rozptylu**.
