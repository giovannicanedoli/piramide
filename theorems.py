import matplotlib.pyplot as plt    #tutte le seguenti funzioni di teoremi e dimostrazioni fanno uso di matplotlib, e molte anche di numpy. Essendo molto simili tra di loro, dopo aver spiegato il template che trovate per primo,
import numpy as np                 #verranno commentati solo i passaggi specifici di determinate funzioni
def teorema_ ():
    plt.title(r'Teorema ', fontfamily = 'serif', fontweight = 'roman')              #permette di scrivere il titolo della slide. Come per .text() esistono molti argomenti opzionali. In questo codice sono utilizzati quasi esclusivamente quelli riguardanti la customizzazione del font
    plt.text(0.010, 0.1, r'''Th:   ''', fontfamily = 'serif', fontweight = 'roman') #<dove inserire il testo. Parametri necessari sono la posizione sugli assi, prima x e poi y (float), poi il testo. Mi raccomando di utilizzare la r prima della stringa perché python possa riconoscere i comandi che permettono di scrivere i caratteri matematici
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)                                         #cambiare questo argomento a False nella funzione fa si che non appaiano gli assi numerati (di default per matplotlib) in quei casi scriviamo solo testo
    fig.axes.get_yaxis().set_visible(False)
    plt.show()

def teorema_inverso_di_bolzano():
    plt.title(r'Teorema inverso di Bolzano', fontfamily = 'serif', fontweight = 'roman')
    plt.text(-0.15, 2500, '''Th: Sia f(x) una funzione monotona nell'intervallo chiuso [a, b].
    Allora f(x) è continua in [a, b] se e solo se l'immagine di f(x)
    è tutto l'intervallo di estremi f(a), f(b)''', fontfamily = 'serif', fontstyle= 'italic', fontweight = 'roman')
    fig = plt.gca()
    x = np.arange(0, 11, 1)                                        #la funzione plot ha bisogno di due liste, una di coordinate in x e una in y, per accoppiarle e poi "unire i punti". Dunque usiamo la funzione arange di numpy per crearci uha lista di numeri
    y = 3*(x**3) + 2*x                                             #stabiliamo i valori di y in funzione di x
    a , f_a = [4,4], [0,200]
    b, f_b = [8,8], [0,1570   ]                                    #dati che ci servono per condurre una linea da un punto all'altro (utilizziamo quindi solo coppie di coordinate x y)
    plt.plot(a, f_a, color= 'black', ls = '--')                    #è facile immaginare cosa permetta di ottenere l'argomento opzoinale color. ls serve per stabilire il tipo di linea (in questo caso è tratteggiata)
    plt.plot(b, f_b, color= 'black', ls= '--')
    _a = [0,4]
    _b = [0,8]
    f_a1 = [200,200]
    f_b1 = [1570,1570]
    plt.plot(_a, f_a1, color= 'black', ls = '--')
    plt.plot(_b, f_b1, color= 'black', ls = '--')
    plt.plot(x, y, color= 'black')
    plt.annotate(r'$(a; f(a))$', (4, 200), xytext = (4.25,150))      #funzione che permette di annotare un punto preciso del disegno. Le prime cordinate sono quelle del punot da annotare, quelle nell'argomento opzionale sono quelle in cui apparirà il testo (in default corrispondono)
    plt.annotate(r'$(b; f(b))$', (8, 1570), xytext = (8.25,1550))
    plt.xlabel("x")
    plt.ylabel("y")
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_inverso_di_bolzano_dim():
    plt.title(r'Teorema inverso di Bolzano', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.450, '''Dim: Se f(x) è continua in [a, b] allora, indipendentemente
    dalla monotonia, assume tutti i valori compresi tra f(a) e f(b).
    Viceversa, se f(x) è crescente in [a, b] ma non è continua ''' + r'$x_0$' + '''
    una discontinuità di prima specie si ha
    $\lim_{x \to x_0^-} f(x) = \ell_1 < \ell_2 = \lim_{x \to x_0^+} f(x)$
    ed f(x) non assume alcun valore nell\'intervallo $(\ell_1, \ell_2)$.
    Si procede in modo analogo se x = a, oppure se x = b: ad esempio,
    se x = a e se f(x) è crescente e non è continua per x = a,
    allora f(x) non asssume akcun valore all\' interno dell\'intervallo
    $(f(a), \ell)$, essendo $f(a) < \ell = \lim_{x \to a^+} f(x)$ ''' , fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_ponte():
    plt.title(r'Teorema Ponte', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.8, r'''Th: Le seguenti affermazioni sono equivalenti:
     $(1) \forall x_n \to x_0, \/ x_n \in A - \{x_0\} \/ \forall n \in N \/ \Rightarrow \/ f(x_n) \to \ell;$
     $(2) \forall \epsilon > 0, \/ \exists \delta < 0 : \/ x \in A, \/ 0 \ne |x - x_0| < \delta \/ \Rightarrow \/ |f(x) - \ell | < \epsilon$''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_ponte_dim():
    plt.title(r'Teorema Ponte', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.02, r'''Dim:  Proviamo preliminarmente che (2) implica (1): per ogni $ \epsilon \/ > \/ 0,$
    sia $\delta \/ > 0 $ il numero reale per cui vale l'ipotesi (2); consideriamo poi
    una generica successione $x_n$, di punti di A, convergente ad $x_0$, con $x_n \/ \ne \/ X_0$ per ogni $ n \in \mathit{N}$.
    Per la definizione di limite di successione, esiste un indice $ \nu $ per cui $ |x_n - x_0| \/ < \/ \delta $
    per ogni $ n > \delta $; inoltre, essendo $x_n \/ \ne \/ X_0$, in definitiva si ha:
    $ x_n \/ \in \/ A, \/\/\/ 0 \ne |x_n - x_0| \/ < \/ \delta $,
    Per l'ipotesi (2) segue allora     $|f(x_0) - \ell| < \epsilon$,
    che, in base alla definizione di limite di succesione, significa che $ f(x_n) \/ \to \/ \ell$ per $ n \/ \to \/ + \infty$.
    Proviamo ora, per assurdo, che (1) implica (2): contraddire (2) equivale ad affermare che:

    $\exists \epsilon_0 : \/ \forall \delta > 0, \/ \exists x \in A: \/ 0 \ne |x - x_0|< \delta, \/ |f(x) - \ell| \geq \epsilon_0$ .

    Poniamo $ \delta = 1/n$ con $ n \in \mathit{N}$, e indichiamo con $ x = x_n $ il valore di x in dipendenza da $ \delta = 1/n$:

    $ \exists \epsilon_0 : \/ \forall n \in \mathit{N}, \/ \exists x_n \in A: \/ 0 \ne |x_n - x_0|< \frac{1}{n}, \/ |f(x_n) - \ell| \geq \epsilon_0$.

    Risulta in particolare

    $ x_n \ne x_0, \/\/ x_0 - \frac{1}{n} < x_n < x_0 + \frac{1}{n} $,

    perciò $ x_n \in A -\{ x_0 \} \/ \forall n \in \mathit{N}$ e $ x_n \to x_0$ (per il teorema del confronto); però f(x)
    non converge ad $ \ell $ perché la disuguaglianza $|f(x_n) - \ell | \geq \epsilon_0 $, $ \forall n \in \mathit{N}$,
    contrasta con la definzione di limite di successione''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_weirstrass():
    plt.title(r'Teorema di Weirstrass', fontfamily = 'serif', fontweight = 'roman')
    plt.text(-0.5, -0.57, r'''Th: Sia f(x)  una funzione continua in un 'intervallo chiuso e limitato.
    Allora f(x) assume minimo e massimo in [a, b],
    cioè esistono $x_1, \/ x_2 $ in [a, b] tali che

    $ f(x_1) \leq f(x) \leq f(x_2)$,     $ \forall x \in [a, b]$ ''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    x = np.arange(0, 11, 0.0001)
    y = np.sin(x)
    a , f_a = [4,4], [-1.2,1.2]
    b, f_b = [9,9], [-1.2,1.2]
    plt.plot(a, f_a, color= 'black', ls = '--')
    plt.plot(b, f_b, color= 'black', ls= '--')
    plt.plot(x, y, color= 'black')
    plt.annotate(r'$a$', (4.05, 0))
    plt.annotate(r'$b$', (8.80, 0))
    z, w = [0,11], [-1,-1]
    plt.plot(z, w, color= 'black', ls= '--')
    plt.annotate(r'min', (4.71, -1), xytext= (4.71, -1.05))
    s, t = [0,11], [1,1]
    plt.plot(s, t, color= 'black', ls= '--')
    plt.annotate(r'MAX', (7.85, 1), xytext= (7.85, 1.03))
    plt.xlabel("x")
    plt.ylabel("y")
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_weirstrass_dim():
    plt.title(r'Teorema di Weirstrass', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: posto $ M = sup {f(x): x \in [a,b]}$, verifichiamo che esiste una successione $x_n$ di punti di [a, b] tale che

    $ \lim_{n \to +\infty} f(x_n) = M $

    Infatti, se M = $ + \infty$, per le proprietà dell'estremo superiore, per ogni $ n \in \mathit{N}$ esiste $ x_n \in [a, b]$ tale che $f(x_n) > n$ e perciò $ f(x_n) \to M = + \infty$.
    Se invece risulta $ M < +\infty$, per ogni $ n \in \mathit{N}$ esiste $x_n$ in [a,b] tale che

    $ M - \frac{1}{n} < f(x_n) \leq M $

    e perciò $f(x_n) \to M$.
    Per il teorema di Bolzano-Weirstrass esiste un'estratta $x_{n_k}$ da $x_n$ ed un punto $x_0 \in [a, b]$, tale che  $x_{n_k} \to x_0$
    Poiché f(x) è continua, ne segue $ f(x_{n_k}) \to f(x_0)$
    e allora

    $ M = \/ \lim_{n \to +\infty} f(x_n) = \/ \lim_{k \to +\infty} f(x_{n_k}) = \/ f(x_0)$.

    Abbiamo dimostrato che

    $f(x_0) = M = sup{f(x): x \in [a,b]}$;

    ciò implica allo stesso tempo che $ M < + \infty $ e che ò'estreemo superiore è, in effetti, un massimo.
    Analogamente si ragiona per determinare un punto di minimo, partendo dall'estremo inferiore di f(x) in [a,b].''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_fermat():
    plt.title(r'Teorema di Fermat', fontfamily = 'serif', fontweight = 'roman')
    plt.text(6, -0.9, r'''Th: Sia $f$ una funzione definita in un intervallo [a,b] e sia $x_0$
    un punto di massimo o minimo relativo interno ad [a,b].
    Se f è derivabile in $x_0$ risulta $ f'(x_0) = 0$.''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    x = np.arange(3, 11, 0.0001)
    y = np.sin(x)
    a , f_a = [4,4], [-1.2,1.2]
    b, f_b = [9,9], [-1.2,1.2]
    plt.plot(a, f_a, color= 'black', ls = '--')
    plt.plot(b, f_b, color= 'black', ls= '--')
    plt.plot(x, y, color= 'black')
    plt.annotate(r'$a$', (4.05, 0))
    plt.annotate(r'$b$', (8.80, 0))
    s, t = [3,11], [1,1]
    plt.plot(s, t)
    plt.annotate(r'MAX', (7.85, 1), xytext= (7.85, 1.03))
    plt.annotate(r'$\frac{df(\frac{5} {2} \pi)}{dx}$', (7,1.03))
    x = np.arange(5,9,0.5)
    y = x - 2*np.pi
    plt.plot(x, y)
    plt.annotate(r'$\frac{df(2 \pi)}{dx}$', (6.4, 0))
    plt.xlabel("x")
    plt.ylabel("y")
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_fermat_dim():
    plt.title(r'Teorema di Fermat', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: consideriamo il caso in cui $x_0$ sia un punto di massimo relativo;
    significa che esiste $\delta > 0$ per cui

    $f(x_0) \geq f(x_0 + h)$,        $ \forall h: \/ |h| < \delta $

    Studiamo separatamente i casi h > 0 e h < 0; dall'espressione precedente otteniamo:

    $\frac{f(x_0 + h) - f(x_0)}{h} \leq 0 \/\/ se \/ 0<h<\delta$
    $\frac{f(x_0 + h) - f(x_0)}{h} \geq 0 \/\/ se \/ -\delta<h<0 $

    e, al limite per $h \to 0^{\pm}$

    $f'(x_0) = \lim_{h \to 0^+} [f(x_0 + h) - f(x_0)]/h \leq 0 $;

    $f'(x_0) = \lim_{h \to 0^-} [f(x_0 + h) - f(x_0)]/h \geq 0 $

    Ne segue che $f'(x_0) = 0$''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_lagrange():
    plt.title(r'Teorema di Lagrange', fontfamily = 'serif', fontweight = 'roman')
    plt.text(9.1, 0.7, r'''Th: Sia f(x) una funzione continua in [a,b] e derivabile in ]a,b[.
    Esiste un punto $x_0 \in ]a,b[ $ per cui

    $ f'(x_0) = \frac{f(b) - f(a)}{b - a}$.  ''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    x = np.arange(5, 11, 0.0001)
    y = np.sin(x)
    a , f_a = [6,6], [-1.2,1.2]
    b, f_b = [9,9], [-1.2,1.2]
    plt.plot(a, f_a, color= 'black', ls = '--')
    plt.plot(b, f_b, color= 'black', ls= '--')
    plt.plot(x, y, color= 'black')
    plt.annotate(r'$a$', (6.05, -1))
    plt.annotate(r'$b$', (8.80, -1))
    plt.plot([6, 9], [np.sin(6), np.sin(9)])
    plt.plot([6, 9], [np.sin(6), np.sin(6)], color= 'black', ls= '--')
    plt.annotate(r'f(b) - f(a)', (8.65, 0))
    plt.annotate(r'a - b', (7.5, np.sin(6) + 0.10))
    plt.plot([6, 9], [np.sin(6) + 0.8788 , np.sin(9) + 0.8788])
    plt.annotate(r'$\frac{df(x_0)}{dx}$', (6.9, 0.9))
    plt.xlabel("x")
    plt.ylabel("y")
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_lagrange_dim():
    plt.title(r'Teorema di Lagrange', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim:  ci si riconduce al teorema per mezzo della funzione

    $ g(x) = f(x) - [ f(a) + \frac{f(b) - f(a)}{b - a} \cdot (x - a)] $.

    Si noti che g(x) è ottenuta sottraendo da f(x) l'espressione della retta congiungente gli estremi del grafico.
    Ponendo successivamente x = a, x = b, si verifica che g(a) = g(b) = 0 (Nota del trascrittore: in g(a) si annulla l'ultima parentesi, in g(b) si semplifica con il denominatore). Inoltre g è derivabile in ]a,b[ e risulta

    $ g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$           $ \forall x \in ]a,b[$,

    Per il teorema di Rolle, esiste quindi $x_0 \in ]a,b[$ per cui $g'(x_0) = 0$
    Ponendo questo risultato nella relazione precedente, verifichiamo l'asserto''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_rolle():
    plt.title(r'Teorema di Rolle', fontfamily = 'serif', fontweight = 'roman')
    plt.text(6.1, -0.5, r'''Th: Sia f(x) una funzione continua in [a,b] e derivabile in ]a,b[, se f(a) = f(b),
     esiste un punto $x_0 \in ]a,b[$ per cui $f'(x_0) = 0 $ ''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    x = np.arange(5, 11, 0.0001)
    y = np.sin(x)
    a , f_a = [6,6], [-1.2,1.2]
    b, f_b = [9.70,9.70], [-1.2,1.2]
    plt.plot(a, f_a, color= 'black', ls = '--')
    plt.plot(b, f_b, color= 'black', ls= '--')
    plt.plot(x, y, color= 'black')
    plt.annotate(r'$a$', (6.05, 0))
    plt.annotate(r'$b$', (9.65, 0))
    plt.plot([6, 9.70], [np.sin(6), np.sin(6)])
    s, t = [6,11], [1,1]
    plt.plot(s, t)
    plt.annotate(r'$\frac{df(x_0)}{dx}$', (6.9, 0.9))
    plt.xlabel("x")
    plt.ylabel("y")
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_rolle_dim():
    plt.title(r'Teorema ', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: indichiamo con $x_1$ e  $x_2$ due punti, rispettivamente di massimo
        e minimo assoluto per f nell'intertvallo [a,b]; cioè

            $f(x_1) \leq f(x) \leq f(x_2)$         $ \forall x \in [a,b]$

        Tali punti di massimo e di minimo assoluto per f esistono, in base
        al teorema di Weirstrass.
        Se almeno uno dei due punti $x_1, \/\/ x_2$ è interno all'intervallo [a,b],
        in corrispondenza la derivata si annulla (per il teorema di Fermat).
        Rimane da esaminare il caso in cui entrambi i punti non sono interni;
        diciamo che $x_1 =a$, $x_2 = b$.
        Avremo dunque che $ f(a) \leq f(x) \leq f(b), \/\/\/ \forall x \in [a,b]$.
        Dato che per ipotesi f(a) = f(b), risulta f(x) = f(a)
        per ogni $x \in [a,b]$; quindi f è costante e la sua derivata è ovunque zero.
        Il teorenma è dimostrato anche in questo caso ''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_cauchy():
    plt.title(r'Teorema di Cauchy', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.7, r'''Th: Siano f(x), g(x) due funzioni continue in [a,b], derivabili in ]a,b[.
    Se g'(x) $ \ne $ 0 per ogni $ x \in ]a,b[$ per cui

    $ \frac{f'(x_0)}{g'(x_0)} = \frac{f(b) - f(a)}{g(b) - g(a)}$.  ''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))
    
def teorema_di_cauchy_dim():
    plt.title(r'Teorema di Cauchy', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: procediamo alla dimostrazione utilizzando la funzione

    $ h(x) = \/ f(x) \/ - \/ [f(a) \/ + \/ \frac{f(b) - f(a)}{g(b)- g(a)} \cdot (g(x) - g(a))]$,

    che è ben definita in [a,b] perché g(b) - g(a) $\ne $ 0 (infatti,
    se fosse g(a) = g(b), per il teorema di Rolle esisterebbe un punto ù$ x_0 \in ]a,b[$ per cui $ g'(x_0) = 0$, contrariamente all'ipotesi $ g'(x_0) \ne 0 \/ \/ \/ \forall x \in ]a,b[$).
    La funzione h(x) è continua in [a,b] e verifica le condizioni
     h(a) = h(b) = 0; inoltre è derivabile in ]a,b[ e la derivata vale

       $ h'(x) = f(x) - \frac{f(b) - f(a)}{g(b) - g(a)} \cdot g'(x)$.

    Per il teorema di Rolle esiste $ x_0 \in ]a,b[ $ per cui $ h'(x_0) = 0$ che,
    essendo g' $ \ne $ 0, equivale alla tesi
     ''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_di_delHopital():
    plt.title(r"Teorema di de l' $H\hat o pital $", fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Th: Siano f, g funzioni derivabili in un intorno di $x_0$
    con la eventuale eccezzione di $x_0$ stesso) tali che

           $ \lim_{x \to x_0} f(x) = 0$         $ \lim_{x \to x_0} g(x) = 0$.

    Se un intorno di $x_0$ risulta g(x), g'(x) $ \ne $ 0 per ogni $ x \ne x_0 $, allora si ha

           $ \lim_{x \to x_0} \/ \frac{f(x)}{g(x)}  \/ = \/ \lim_{x \to x_0} \/  \frac{f'(x)}{g'(x)}  $,

    purché esista il secondo limite.  ''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    #plt.show()
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_del_confronto():
    plt.title(r'Teorema del confornto', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Th: Siano $ a_n, \/ b_n, \/ c_n $ tre successioni tali che

        $ a_n \leq b_n \leq b_n$,     $ \forall n \in N$.

    se $ \lim_{n \to +\infty} \/ a_n \/ = \/ \lim_{n \to +\infty} \/ b_n \/ = a$, allora anche la successione
     $c_n$ è convergente e $ \lim_{n \to + \infty} c_n = a$. ''', fontfamily = 'serif', fontweight = 'roman', fontstyle = 'italic')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_del_confronto_dim():
    plt.title(r'Teorema del confornto', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: per ipotesi, per ogni $ \epsilon > 0 $

              $ \exists \nu_1 : |a_n -a| < \epsilon,\/ \forall n > \nu_1 ;$      $ \exists \nu_2 : |b_n - a | < \epsilon, \/ \forall n > \nu_2$.

    Ricordiamo che le disuguaglianze con il valore assoluto
    si possono anche riscrivere

              $ a - \epsilon < a_n < a + \epsilon $;   $ a - \epsilon < b_n < a + \epsilon $

    Quindi, se n > $\nu$ = max {$ \nu_1 , \nu_2 $}, risulta

          $ a - \epsilon \/<\/ a_n \/\leq\/ c_n \/\leq\/ b_n \/<\/ a + \epsilon$.

    Perciò $ |c_n - a| < \epsilon $ per ogni $n > \nu$, come volevasi dimostrare ''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_unicita_limite():
    plt.title(r'Teorema di unicità del limite', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.95, r'''Th: Una successione convergente non può avere due limiti distiniti  ''', fontfamily = 'serif', fontweight = 'roman', fontstyle= 'italic')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_unicita_limite_dim():
    plt.title(r'Teorema di unicità del limite', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: supponiamo per assurdo che esistano due limiti distinti,
     cioè supponiamo che $ a_n \to a, a_n \to b$ con $ a \ne b $.
    Poniamo $ \epsilon = |a - b|/2(>0)$. Si ha

           $ \exists \nu_1 : |a_n - a|< \epsilon, \/ \forall n > \nu_1 $;     $\exists \nu_2 : |a_n - a|< \epsilon, \/ \forall n > \nu_2 $.

    Ponendo $ \nu = max\{\nu_1, \nu_2\}$, le relazioni sopra scritte valgono
     contemporaneamente e si ha, per la disuguaglianza triangolare

    $ |a - b| = |(a - a_n) + (a_n - b)| \leq |a - a_n| + |a_n - b| < \epsilon + \epsilon = |a - b|$.

    Abbiamo così trovato che $ |a - b| < |a - b|$, che è assurdo. ''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_degli_zeri():
    plt.title(r'Teorema ', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Th: Sia f(x) una funzione continua in un intervallo [a,b],
    Se f(a) < 0, f(b) > 0, allora esiste $x_0 \in ]a,b[ $ tale che f($x_0$) = 0.  ''', fontfamily = 'serif', fontweight = 'roman', fontstyle = 'italic')
    fig = plt.gca()
    x = np.arange(5, 11, 0.0001)
    y = np.sin(x)
    a , f_a = [6,6], [-1.2,1.2]
    b, f_b = [9,9], [-1.2,1.2]
    plt.plot(a, f_a, color= 'black', ls = '--')
    plt.plot(b, f_b, color= 'black', ls= '--')
    plt.plot(x, y, color= 'black')
    plt.annotate(r'$a$', (6.05, -1))
    plt.annotate(r'$b$', (8.80, -1))
    plt.annotate(r'f(a)', (6.1, np.sin(6)))
    plt.annotate(r'f(b)', (9.1, np.sin(9)))
    plt.plot([5,11], [0,0], color= 'black')
    plt.annotate(r'$(x_0, 0)$', (6.3, -0.06))
    plt.xlabel("x")
    plt.ylabel("y")
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_degli_zeri_dim():
    plt.title(r'Teorema degli zeri', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim:   ''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))
def teorema_della_permanenza_del_segno():
    plt.title(r'Teorema della permanenza del segno', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.8, r'''Th: Sia f(x) una funzione definita in un intorno di $x_0$ e sia continua
    in $x_0$. Se $f(x_0)>0$, esiste un numero $\delta>0$ con la proprietà
    che f(x)>0 per ogni $ x \in (x_0 - \delta, x_0 + \delta) $.''', fontfamily = 'serif', fontweight = 'roman', fontstyle = 'italic')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def teorema_della_permanenza_del_segno_dim():
    plt.title(r'Teorema della permanenza del segno', fontfamily = 'serif', fontweight = 'roman')
    plt.text(0.010, 0.1, r'''Dim: dato che $ f(x_0) > 0$, possiamo scegliere $ \epsilon = f(x_0)/2 $; esiste quindi
    un numero $\delta > 0$ per cui

         $ |f(x) - f(x_0)| < \frac{f(x_0)}{2} $,    $ \forall x \in (x_0 - \delta, x_0 + \delta) $
         $ -\frac{f(x_0)}{2} < f(x) - f(x_0) < \frac{f(x_0)}{2} $;

    dunque:

        $ f(x) > f(x_0) - \frac{f(x_0)}{2} = \frac{f(x_0)}{2} >0$

    è così verificato l'asserto ''', fontfamily = 'serif', fontweight = 'roman')
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig = plt.gcf()
    fig.set_size_inches((16, 9))

def display(t):    #funzione che permette di richiamare una delle funzioni precedenti usando il numero in cui sono posizioate. Counsultare il main code per capire perché serve
    if t == 1:
        teorema_inverso_di_bolzano()
        plt.show()
    elif t == 2:
        teorema_inverso_di_bolzano_dim()
        plt.show()
    elif t == 3:
        teorema_ponte()
        plt.show()
    elif t == 4:
        teorema_ponte_dim()
        plt.show()
    elif t == 5:
        teorema_di_weirstrass()
        plt.show()
    elif t == 6:
        teorema_di_weirstrass_dim()
        plt.show()
    elif t == 7:
        teorema_di_fermat()
        plt.show()
    elif t == 8:
        teorema_di_fermat_dim()
        plt.show()
    elif t == 9:
        teorema_di_lagrange()
        plt.show()
    elif t == 10:
        teorema_di_lagrange_dim()
        plt.show()
    elif t == 11:
        teorema_di_rolle()
        plt.show()
    elif t == 12:
        teorema_di_fermat_dim()
        plt.show()
    elif t == 13:
        teorema_di_cauchy()
        plt.show()
    elif t == 14:
        teorema_di_cauchy_dim()
        plt.show()
    elif t == 15:
        teorema_di_delHopital()
        plt.show()
    elif t == 16:
        teorema_del_confronto()
        plt.show()
    elif t == 17:
        teorema_del_confronto_dim()
        plt.show()
    elif t == 18:
        teorema_unicita_limite()
        plt.show()
    elif t == 19:
        teorema_unicita_limite_dim()
        plt.show()
    elif t == 20:
        teorema_degli_zeri()
        plt.show()
    elif t == 21:
        teorema_degli_zeri_dim()
        plt.show()
    elif t == 22:
        teorema_della_permanenza_del_segno()
        plt.show()
    elif t == 23:
        teorema_della_permanenza_del_segno_dim()
        plt.show()
