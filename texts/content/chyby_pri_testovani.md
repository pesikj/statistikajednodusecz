Možné případy chyb a správných výsledků se často znázorňují v tabulce. Ve sloupcích vidíme skutečnost (kterou neznáme) a v řádcích výsledek našeho testování.


<table class="table">
  <thead>
    <tr>
      <th scope="col"></th>
      <th scope="col">Nulová hypotéza platí</th>
      <th scope="col">Nulová hypotéza neplatí</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Nulovou hypotézu nezamítáme</th>
      <td>Správný výsledek</td>
      <td>Chyba 2. druhu</td>
    </tr>
    <tr>
      <th scope="row">Nulovou hypotézu zamítáme</th>
      <td>Chyba 1. druhu</td>
      <td>Správný výsledek</td>
    </tr>
  </tbody>
</table>

Celkem tedy mohou nastat dva případy, přičemž dva znamenají, že výsledek našeho testování je správný, a zbývající, že výsledek testování je chybný.

Pokud vás chyby zajímají více, podívejte se na ukázku toho, [jak vznikají](jak_vznikaji_chyby.md).
