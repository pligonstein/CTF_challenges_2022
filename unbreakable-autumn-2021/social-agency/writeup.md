# Social Agency - OSINT

Dupa ce am copiat adresa email tecgirwilliam@gmail.com,  am incercat prima data sa ii dau email dar nu a mers.
Apoi am incercat sa intru pe Google Hangouts, am adaugat email-ul si am intrat la inspect elements unde am observat:

![screenshot-social-agency](https://github.com/pligonstein/Veterans_in_security_ctf/blob/master/unbreakable-autumn-2021/social-agency/screeshot.png)

Am intrat pe Google Maps si am cautat acest oid gasit cu inspect, unde am vazut ca la recenzii un user pe nume Tecgir (care era acelasi cu emailul dat) a facut recenzie la Cascada Lotrisor.
Apoi am vazut ca Cascada Lotrisor are Google plus code-ul `827J+WX Brezoi`.
Ca sa aflam flagu am dat hash la acest code si am gasit flag-ul: `CTF{e0c34f6ffe1dcc87c67a4fa218b1050da7bb9b9d01871ea7afcb49e55b81257d}`.
