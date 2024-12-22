<!-- wp:advanced-gutenberg-blocks/intro -->
<div class="wp-block-advanced-gutenberg-blocks-intro"><p class="wp-block-advanced-gutenberg-blocks-intro__content">Welchův test používáme pro soubory, jejichž pozorování <strong>nejsou spárována a nemůžeme u nich předpokládat shodný rozptyl</strong>.  V některých učebnicích statistiky je doporučeno začít s ověřením hypotézy o shodě rozptylů pomocí Fischerova testu a dle výsledku poté zvolit variantu t-testu. Tento postup však není korektní.</p></div>
<!-- /wp:advanced-gutenberg-blocks/intro -->

<!-- wp:advanced-gutenberg-blocks/summary -->
<div class="wp-block-advanced-gutenberg-blocks-summary"><p class="wp-block-advanced-gutenberg-blocks-summary__title">Obsah článku</p><div class="wp-block-advanced-gutenberg-blocks-summary__fold"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-up"><polyline points="18 15 12 9 6 15"></polyline></svg></div><ol role="directory" class="wp-block-advanced-gutenberg-blocks-summary__list"><li><a href="#levostranný-welchův-t-test">Levostranný Welchův t-test</a><ol><li><a href="#výpočet-pomocí-doplňku-analýza-dat">Výpočet pomocí doplňku Analýza dat</a><ol></ol></li><li><a href="#výpočet-pomocí-funkce-ttest">Výpočet pomocí funkce T.TEST</a><ol><li><a href="#obecná-funkce-pro-levostranný-test">Obecná funkce pro levostranný test</a><ol></ol></li></ol></li></ol></li><li><a href="#pravostranný-welchův-test">Pravostranný Welchův test</a><ol><li><a href="#výpočet-pomocí-doplňku-analýza-dat">Výpočet pomocí doplňku Analýza dat</a><ol></ol></li><li><a href="#výpočet-pomocí-funkce-ttest">Výpočet pomocí funkce T.TEST</a><ol></ol></li></ol></li><li><a href="#oboustranný-welchův-test">Oboustranný Welchův test</a><ol><li><a href="#výpočet-pomocí-doplňku-analýza-dat">Výpočet pomocí doplňku Analýza dat</a><ol></ol></li><li><a href="#výpočet-pomocí-funkce-ttest">Výpočet pomocí funkce T.TEST</a><ol></ol></li></ol></li></ol></div>
<!-- /wp:advanced-gutenberg-blocks/summary -->

<!-- wp:heading -->
<h2 id="levostranný-welchův-t-test">Levostranný Welchův t-test</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Abychom si ještě jednou ukázali odlišnost Welchova testu, vyjdeme ze zadání z předchozích dvou článku:&nbsp;<em>Máme data o průměrném počtu vyrobených výrobků pracovníky&nbsp;<strong>ve dvou různých závodech</strong>, přičemž v jednom ze závodů jsou testovány nové výrobní procesy. Vedení společnosti potřebuje ověřit, zda nové výrobní postupy zvýšily produktivitu práce. Ověřte na [latex] \alpha = 5 % [/latex]&nbsp;hypotézu, že v závodě s novými výrobními postupy vyrobí pracovníci v průměru více výrobků, než v závodě s původními postupy, přičemž předpokládáme, že&nbsp;<strong>rozptyly</strong>&nbsp;průměrného počtu výrobků&nbsp;<strong>se mohou lišit</strong>. Vedení v minulosti statisticky ověřilo, že před změnou procesů byli pracovníci v obou závodech v průměru stejně výkonní.</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Data jsou v tabulce níže</p>
<!-- /wp:paragraph -->

<!-- wp:table -->
<figure class="wp-block-table"><table class=""><tbody><tr><td>Závod 1</td><td>199.98214</td><td>200.02066</td><td>200.02763</td><td>199.95948</td><td>199.99668</td><td>200.01018</td><td>199.99315</td><td>199.97664</td><td>200.01485</td><td>199.96795</td><td>199.92523</td><td>200.02216</td><td>200.03065</td><td>200.01761</td><td>200.01264</td><td>200.08308</td><td>199.99550</td><td>200.00041</td><td>199.99517</td><td>200.02942</td></tr><tr><td>Závod 2</td><td>200.04822</td><td>200.08817</td><td>200.04806</td><td>200.01402</td><td>200.03498</td><td>199.92516</td><td>200.09787</td><td>200.10234</td><td>199.95363</td><td>200.01334</td><td>199.97706</td><td>200.01043</td><td>199.96209</td><td>199.91984</td><td>200.08773</td><td>200.04719</td><td>199.98357</td><td></td><td></td><td></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>Opět zavedeme značení:&nbsp;[latex] X_1 [/latex]&nbsp;obsahuje pozorování ze závodu se starými postupy a soubor [latex] X_2 [/latex]&nbsp;pozorování ze závodu s upravenými postupy. Příslušné střední hodnoty pak označíme [latex] \mu_{X_1} [/latex]&nbsp;a [latex] \mu_{X_2} [/latex]. Nyní můžeme formulovat nulovou a alternativní hypotézu:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>[latex] H_0: \mu_{X_1} = \mu_{X_2} [/latex] (Střední hodnota obou souborů je stejná.)</li><li> [latex] H_1: \mu_{X_1} &lt; \mu_{X_2}  [/latex] (Střední hodnota prvního souboru je nižší.)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Statistiku testu vypočteme dle vzorce</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center">[latex] T = \frac{\bar{X_1} - \bar{X_2}}{\sqrt{\frac{s_1^2}{n_1} +  \frac{s_2^2}{n_2}}} \, ,  [/latex]</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>kde [latex] \bar{X_1} [/latex] a [latex] \bar{X_2} [/latex] značí průměry,  [latex] s_1^2 [/latex] a [latex] s_2^2 [/latex] výběrové rozptyly a [latex] n_1 [/latex] a [latex] n_2 [/latex] počty pozorování. Statistika má opět Studentovo (t) rozdělení. Poměrně složitý je tentokrát určení počtů stupňů volnosti, proto se ručnímu výpočtu vyhneme a provedeme výpočet pouze pomocí Analýzy dat a funkce T.TEST.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5080,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Levostranný-Welchův-test-Excel-1-1024x398.png" alt="" class="wp-image-5080"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 id="výpočet-pomocí-doplňku-analýza-dat">Výpočet pomocí doplňku Analýza dat</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>V Analýze dat tentokrát volíme možnost <strong>Dvouvýběrový t-test s nerovností rozptylů</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5069,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Výběr-testu.png" alt="" class="wp-image-5069"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Do polí 1. soubor a 2. soubor vybereme oblasti s daty. Vybereme-li oblasti včetně záhlaví, zaškrtneme pole Popisky. Dále označíme Výstupní oblast a stiskneme tlačítko OK.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5071,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Levostranný-Welchův-test-AD-výsledky.png" alt="" class="wp-image-5071"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Na obrázku níže vidíme výsledky.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5081,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Levostranný-Welchův-test-AD-výsledky-2-1.png" alt="" class="wp-image-5081"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p> Protože provádíme levostranný test, zajímají nás označené řádky. Hodnota statistiky je tedy [latex] T = -0{,}9650 [/latex]. Kritický obor se nachází vlevo, proto vezmeme hranici z řádku t krit (1) a přidáme k ní tlačítko minus. Kritický obor tedy leží v intervalu [latex] W = \left( - \infty,   -1{,}7109 \right\rangle [/latex]. P-hodnota testu je [latex] 0{,}1721 [/latex]. P-hodnota skutečně odpovídá naší variantě testu. Protože p-hodnota je vyšší než hladina významnosti, nezamítáme [latex] H_0 [/latex].</p>
<!-- /wp:paragraph -->

<!-- wp:advanced-gutenberg-blocks/notice -->
<div class="wp-block-advanced-gutenberg-blocks-notice is-variation-info" data-type="info"><p class="wp-block-advanced-gutenberg-blocks-notice__title">Poznámka</p><p class="wp-block-advanced-gutenberg-blocks-notice__content"> Statistika testu je totiž záporná a tím pádem musí být p-hodnota menší než  [latex] 0{,}05[/latex].  </p></div>
<!-- /wp:advanced-gutenberg-blocks/notice -->

<!-- wp:heading {"level":3} -->
<h3 id="výpočet-pomocí-funkce-ttest">Výpočet pomocí funkce T.TEST</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Funkce T.TEST (ve starších verzích TTEST) vrací p-hodnotu testu. Prvními dvěma parametry jsou soubory s daty. Třetím parametrem je varianta testu (oboustranný nebo jednostranný), zadáváme tedy 1. Posledním parametrem volíme, zda se jedná o párový t-test (1), Studentův t-test (2) nebo Welchův test (3).</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>=T.TEST(A2:A21,B2:B18,1,3)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Pro naše data vrací funkce hodnotu [latex] 0{,}1721 [/latex], na základě toho bychom tedy nezamítli  [latex] H_0 [/latex].</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 id="obecná-funkce-pro-levostranný-test">Obecná funkce pro levostranný test</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Funkce T.TEST funguje na podobném principu jako výpočet p-hodnoty u Analýzy dat, tj. vrací menší z možných dvou p-hodnot. Teoreticky by se mohlo stát, že by hodnota statistiky byla vyšší než 0 a tím pádem by p-hodnota testu byla vyšší 0,5. Funkce T.TEST však vrací vždy p-hodnotu menší než 0,5, tj. vracela by p-hodnotu pro pravostranný test. Rozhodnutí můžeme opět provést na základě hodnoty statistiky a pomocí funkce KDYŽ:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>=KDYŽ(E8&lt;0,T.TEST(A2:A21,B2:B18,1,3),1-T.TEST(A2:A21,B2:B18,1,3))</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Samotný vzorec pro výpočet statistiky je </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>=(E3-F3)/ODMOCNINA(E4/E2+F4/F2)</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 id="pravostranný-welchův-test">Pravostranný Welchův test</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Uvažujme nyní, že máme obdobné zadání, máme však data o průměrné době potřebné na výrobu jednoho výrobku. Pokud by technologické postupy v novém závodě byly efektivnější, průměrná doba výroby by měla být nižší. Data jsou v tabulce níže.</p>
<!-- /wp:paragraph -->

<!-- wp:table -->
<figure class="wp-block-table"><table class=""><tbody><tr><td>Závod 1</td><td>44.69267</td><td>45.69315</td><td>44.42006</td><td>44.49233</td><td>44.76451</td><td>45.71278</td><td>45.26229</td><td>44.96354</td><td>45.32207</td><td>43.99095</td><td>45.64706</td><td>45.13311</td><td>44.88322</td><td>45.76855</td><td>43.95434</td><td>45.43278</td><td>45.29947</td><td>44.9996</td><td>45.76979</td><td>45.38547</td><td>45.88574</td><td>44.68477</td><td>44.88063</td><td>45.06176</td><td>45.37277</td><td></td><td></td></tr><tr><td>Závod 2</td><td>44.22226</td><td>44.78572</td><td>44.39838</td><td>45.08415</td><td>44.80706</td><td>44.03529</td><td>44.19068</td><td>45.15528</td><td>43.99419</td><td>44.79819</td><td>43.9513</td><td>44.92697</td><td>44.97488</td><td>45.43995</td><td>44.49937</td><td>44.81813</td><td>45.614</td><td>44.51578</td><td>43.90898</td><td>44.15076</td><td>43.78361</td><td>44.33133</td><td>44.362</td><td>44.22765</td><td>44.01149</td><td>45.01004</td><td>44.2919</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>Modifikujeme alternativní hypotézu a získáme dvojici hypotéz:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>[latex] H_0: \mu_{X_1} = \mu_{X_2} [/latex]</li><li> [latex] H_1: \mu_{X_1} &gt; \mu_{X_2} [/latex]</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Hladina významnosti je stále [latex] \alpha = 5 % [/latex].</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5087,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Pravostranný-Welchův-test-Excel-1024x488.png" alt="" class="wp-image-5087"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 id="výpočet-pomocí-doplňku-analýza-dat">Výpočet pomocí doplňku Analýza dat</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Postup výpočtu je naprosto stejný jako u levostranného testu. Pro aktuální data máme výstup na obrázku níže.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5086,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Pravostranný-Welchův-test-AD-výsledky-2.png" alt="" class="wp-image-5086"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Hodnota statistiky je nyní [latex] T = 3{,}9928 [/latex]. Kritický obor se nachází vpravo, proto hranici najdeme v řádku t krit (1) a tentokrát ji nijak neupravujeme. Kritický obor tedy leží v intervalu [latex] W = \left\rangle 1{,}6766 , \infty \right) [/latex]. Vidíme, že statistika lež v kritickém oboru. p-hodnota testu je [latex] 0{,}0001 [/latex], zamítáme tedy [latex] H_0 [/latex]. Na [latex] \alpha = 5 % [/latex] jsme prokázali, že výroba ve druhém závodě je rychlejší.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 id="výpočet-pomocí-funkce-ttest">Výpočet pomocí funkce T.TEST</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Zápis funkce je opět stejný, tj.:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>=T.TEST(A2:A26,B2:B28,1,3)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Funkce vrací p-hodnotu testu, což je [latex] 0{,}0001[/latex]. Nulovou hypotézu bychom opět zamítli.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Pokud bychom opět chtěli obecný vzorec, který si poradí i s p-hodnotami vyššími než 0,5, upravíme jej o podmínku na základě hodnoty statistiky:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>=KDYŽ(E8>0,T.TEST(A2:A26,B2:B28,1,3),1-T.TEST(A2:A26,B2:B28,1,3))</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 id="oboustranný-welchův-test">Oboustranný Welchův test</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>V případě oboustranného testu řešíme pouze to, zda je mezi středními hodnotami rozdíl. Vraťme se k našemu příkladu s počty vyrobených výrobků ve dvou různých závodech. Nyní tedy rozhodneme "pouze" o tom, zda se průměrné počty mezi závody liší.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Naše hypotézy jsou nyní:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>[latex] H_0: \mu_{X_1} = \mu_{X_2} [/latex] (Střední hodnota obou souborů je stejná.)</li><li> [latex] H_1: \mu_{X_1} \neq \mu_{X_2}  [/latex] (Střední hodnota prvního souboru je nižší.)</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Data z obou závodů jsou v tabulce níže.</p>
<!-- /wp:paragraph -->

<!-- wp:table -->
<figure class="wp-block-table"><table class=""><tbody><tr><td>Závod 1</td><td>190.53082</td><td>190.70691</td><td>190.68514</td><td>189.32068</td><td>189.93107</td><td>189.65363</td><td>189.62920</td><td>190.15749</td><td>189.88063</td><td>190.15778</td><td>189.86708</td><td>190.81115</td><td>190.35090</td><td>189.60921</td><td>190.38187</td><td>190.85053</td><td>189.79748</td><td>189.90501</td><td>########</td><td>########</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Závod 2</td><td>190.51846</td><td>191.86783</td><td>191.71020</td><td>189.71007</td><td>189.79866</td><td>190.82983</td><td>191.09171</td><td>190.59191</td><td>190.10827</td><td>190.59553</td><td>190.91844</td><td>190.10630</td><td>190.16401</td><td>190.00247</td><td>190.19419</td><td>190.20659</td><td>190.03263</td><td>190.37341</td><td>########</td><td>########</td><td>########</td><td>########</td><td>########</td><td>########</td><td>########</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>Test opět provedeme na hladině významnosti [latex] \alpha = 5 % [/latex].</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5092,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Oboustranný-Welchův-test-Excel-1024x469.png" alt="" class="wp-image-5092"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3 id="výpočet-pomocí-doplňku-analýza-dat">Výpočet pomocí doplňku Analýza dat</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Test spustíme pomocí stejného postupu jako v ostatních variantách. Hodnota statistiky testu je [latex] T = -2{,}0854 [/latex]. p-hodnotu a hranici kritického oboru nyní najdeme v posledních dvou řádcích. p-hodnota testu je [latex] 0{,}0430 [/latex]. Kritický obor je v případě oboustranného testu rozdělen na dvě části. Analýza dat nám vrací dolní hranici pravé části, horní hranici levé získáme, když před danou hranici napíšeme 0. Kritický obor je tedy [latex] W = \left( -\infty, - 2{,}0167 \right\rangle \cup \left\langle  2{,}0167, \infty \right) [/latex].</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":5093,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://statistikajednoduse.cz/wp-content/uploads/2019/12/Oboustranný-Welchův-test-AD-výsledky.png" alt="" class="wp-image-5093"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Statistika tedy leží v kritickém oboru a p-hodnota je nižší než hladina významnosti, na [latex] \alpha = 5 % [/latex] tedy zamítáme [latex] H_0 [/latex]. Tentokrát jsme však pouze prokázali, že mezi výkonností závodů existuje rozdíl, nelze však tvrdit, že v druhém závodě je výkonnost vyšší.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 id="výpočet-pomocí-funkce-ttest">Výpočet pomocí funkce T.TEST</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>V případě oboustranného testu zadáváme na třetí pozici číslo 2, díky čemuž nám funkce T.TEST vrátí p-hodnotu oboustranného testu. V našem případě to je tedy hodnota [latex] 0{,}0430 [/latex].</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>=T.TEST(A2:A21,B2:B26,2,3)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>V případě oboustranného testu je vrácená hodnota vždy správná a funkci již nemusíme nijak upravovat.</p>
<!-- /wp:paragraph -->