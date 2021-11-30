import theorems as th  #importiamo tutte le funzioni che fanno uso di matplotlib per i teoremi e le loro dimostrzazioni (cove necessarie). Consultare il file theorems se interessati a quelle

def main():
    #quella che segue è il core del programma, un nido di dizionari che ci permette di ricercare il teorema a cui siamo interessati. A ogni teorema/dimostrazione è assegnato un numero perché
    #pare che non si possano ottenere variabili contenenti le figure date da matplotlib (se qualcuno sa come farlo può segnalarcelo), quindi le funzoni contenenti i teoremi avrebbero come effetto
    #collaterale quello di mostrare la figura già durante la lettura del dizionario. Invece così la scelta del numero associato al teorema richiama più avanti solo la funzione necessaria
    piramide = {
       'teoremi che se non sai vieni bocciato!' : { 'teorema inverso (e diretto) di bolzano (dimostrazione: SI) ' : {'teorema' : 1,
                                                                                                                     'dimostrazione' : 2},
                                                    'teorema ponte (dimostrazione: SI ?)' : {'teorema' : 3,
                                                                                             'dimostrazione' : 4 }},

        'teoremi sulle derivate' : {'teorema di weirstrass dimostrazione (SI)' : {'teorema' : 5,
                                                                                  'dimostrazione' : 6},
                                    'teorema di fermat dimostrazione (SI)' : {'teorema' : 7,
                                                                              'dimostrazione' : 8},
                                    'teorema di lagrange dimostrazione (SI)' : {'teorema' : 9,
                                                                                'dimostrazione' : 10},
                                    'teorema di rolle dimostrazione (SI)' : {'teorema' :  11 ,
                                                                             'dimostrazione' :12},
                                    'teorema di cauchy dimostrazione (SI)' : {'teorema' : 13,
                                                                              'dimostrazione' : 14},
                                    'teorema di de l\'hopital': {'teorema' : 15}},

       'teoremi sui limiti': {'teorema del confronto e corollari vari dimostrazione (SI)' : {'teorema' :  16,
                                                                                             'dimostrazione' : 17},
                              'teorema di unicità del limite' : {'teorema' : 18,
                                                                 'dimostrazione' : 19},
                              #'teorema dei valori intermedi' : {'teorema' : '!Inserire teorema!',                                         #!LAVORI IN CORSO!
                              #                                  'dimostrazione' : '!Inserire dimostrazione!'},                            #!LAVORI IN CORSO!
                              'teorema degli zeri' : {'teorema' : 20,
                                                      'dimostrazione' : 21},
                              'teorema della permanenza del segno' : {'teorema' : 22,
                                                                      'dimostrazione' : 23}},

       #'teoremi sul calcolo integrale' : {'teorema della media integrale' : {'teorema' : '!Inserire teorema!',                            #!LAVORI IN CORSO!
        #                                                                     'dimostrazione' : '!Inserire dimostrazione!'},               #!LAVORI IN CORSO!
        #                                  'teorema fondamentale del calcolo integrale' : {'teorema' : '!Inserire teorema!',               #!LAVORI IN CORSO!
        #                                                                                  'dimostrazione' : '!Inserire dimostrazione!'}}, #!LAVORI IN CORSO!

       'definizioni relative ai limiti (so na cifra, vedi quaderno E slide)': {'definizione di limite di successione convergente, divergente': {'teorema' : '!Inserire teorema!', #!LAVORI IN CORSO!
                                                                                                                                                'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'definzione di limite di funzione convergente, divergente' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                                                            'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'definizione di punto di accumulazione' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                                       'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'definizione di compatto' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                          'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'definizione di intorno' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                         'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'definzione di continuità' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                           'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'condizioni sufficienti per la derivabilità' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                                             'dimostrazione' : '!Inserire dimostrazione!'},#!LAVORI IN CORSO!
                                                                               'condizioni sufficienti per l\'integrabilità' : {'teorema' : '!Inserire teorema!',#!LAVORI IN CORSO!
                                                                                                                                'dimostrazione' : '!Inserire dimostrazione!'}},#!LAVORI IN CORSO!
#!LAVORI IN CORSO!
       'teoremi sensa senso': {'teorema di cantor (quello vecchio incomprensibile)' : {'teorema' : '!Inserire teorema!',
                                                                                    'dimostrazione' : '!Inserire dimostrazione!'}}#!LAVORI IN CORSO!
   }

    print("Benvenuto alla piramide dei teoremi di quei folli di ingneria informatica")
    chosen = False
    while not chosen:            #chiediamo finché non sia stata data uina risposta decifabile
        print("Scegli il tipo di teorema/definizione tra questi (scrivendo il nome o il numero corrispondente):")
        for i, d in enumerate(piramide): #creiamo la lista di teroemi a disposizione
            print(f"{i + 1}) {d}")       #per ogni chiave del dizionario, i +1 è il numero in ordine della chiave in stampata e d è la chiave stessa
        th_type = input()
        if th_type in piramide:          #se in input abbiamo l'intero numero della chiave
            chosen = True
            pass
        elif th_type.isnumeric():        #se in input abbiamo il numero ordinato alla chiave
            key_list = [k for k in piramide]
            th_type = key_list[int(th_type) - 1]
            chosen = True
        else:
            print("L'input dato non corrisonde ad alcun tipo di teroema, riprova:")  #se l'input non è chiaro al programma

    chosen = False
    while not chosen: #nido di cicli simile al precedente
        print(f"Scegli tra questi/e {th_type} (scrivendo il nome o il numero corrispondente):")
        for i, d in enumerate(piramide[th_type]):
            print(f"{i + 1}) {d}")
        theoreme = input()
        if theoreme in piramide[th_type]:
            chosen = True
            pass
        elif theoreme.isnumeric():
            key_list = [k for k in piramide[th_type]]
            theoreme = key_list[int(theoreme) - 1]
            chosen = True
        else:
            print("L'input dato non corrisonde ad alcun teroema, riprova:")

    chosen = False
    while not chosen: #abbastanza simile ai precedenti
        print("Vuoi vedere il teorema o la dimostrazione? (th o dim):")
        th_or_dim = input()
        if th_or_dim == 'th':
            th_or_dim = 'teorema'
            chosen = True
        elif th_or_dim == 'dim':
            th_or_dim = 'dimostrazione'
            chosen = True
        else:
            print("L'input dato non corrisonde ad alcuna opzione, riprova:")

    scelta = piramide[th_type][theoreme][th_or_dim]  #mettiamo insieme le risposte per andare a cercare il teorema che serve all'utente


    th.display(scelta)    #l'unica funzione che chiamiamo effettivamente dal theorems, in realtà al suo essa richiama la funzione specifica che ci serve per mostrare (per questo "display") la figura creata per il teorema scelto



if __name__ == '__main__':
    main()
