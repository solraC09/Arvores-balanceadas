class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.rotacoes = 0
        self.verificacoes = 0

    def _altura(self, no):
        return no.altura if no else 0

    def _atualizar(self, no):
        no.altura = 1 + max(self._altura(no.esq), self._altura(no.dir))

    def _fator(self, no):
        return self._altura(no.esq) - self._altura(no.dir)

    def _rot_dir(self, y):
        self.rotacoes += 1
        x = y.esq
        y.esq = x.dir
        x.dir = y
        self._atualizar(y)
        self._atualizar(x)
        return x

    def _rot_esq(self, x):
        self.rotacoes += 1
        y = x.dir
        x.dir = y.esq
        y.esq = x
        self._atualizar(x)
        self._atualizar(y)
        return y

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if no is None:
            return NoAVL(chave)
        if chave < no.chave:
            no.esq = self._inserir(no.esq, chave)
        else:
            no.dir = self._inserir(no.dir, chave)

        self._atualizar(no)
        self.verificacoes += 1
        fator = self._fator(no)

        if fator > 1:
            if chave >= no.esq.chave:
                no.esq = self._rot_esq(no.esq)
            return self._rot_dir(no)
        if fator < -1:
            if chave < no.dir.chave:
                no.dir = self._rot_dir(no.dir)
            return self._rot_esq(no)
        return no

    def altura(self):
        def h(no):
            return 0 if no is None else 1 + max(h(no.esq), h(no.dir))
        return h(self.raiz)


RED, BLACK = 0, 1


class No:
    def __init__(self, chave):
        self.chave = chave
        self.cor = RED
        self.esq = self.dir = None
        self.pai = None


class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(None)
        self.NIL.cor = BLACK
        self.raiz = self.NIL
        self.rotacoes = 0
        self.recoloracoes = 0
        self.verificacoes = 0

    def _rot_esq(self, x):
        self.rotacoes += 1
        y = x.dir
        x.dir = y.esq
        if y.esq != self.NIL:
            y.esq.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y
        y.esq = x
        x.pai = y

    def _rot_dir(self, x):
        self.rotacoes += 1
        y = x.esq
        x.esq = y.dir
        if y.dir != self.NIL:
            y.dir.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.dir:
            x.pai.dir = y
        else:
            x.pai.esq = y
        y.dir = x
        x.pai = y

    def inserir(self, chave):
        novo = No(chave)
        novo.esq = novo.dir = self.NIL
        pai, atual = None, self.raiz
        while atual != self.NIL:
            pai = atual
            atual = atual.esq if chave < atual.chave else atual.dir
        novo.pai = pai
        if pai is None:
            self.raiz = novo
        elif chave < pai.chave:
            pai.esq = novo
        else:
            pai.dir = novo
        self._corrigir_insercao(novo)

    def _corrigir_insercao(self, z):
        while z.pai and z.pai.cor == RED:
            self.verificacoes += 1
            avo = z.pai.pai
            if z.pai == avo.esq:
                tio = avo.dir
                if tio.cor == RED:
                    z.pai.cor = tio.cor = BLACK
                    avo.cor = RED
                    self.recoloracoes += 1
                    z = avo
                else:
                    if z == z.pai.dir:
                        z = z.pai
                        self._rot_esq(z)
                    z.pai.cor = BLACK
                    avo.cor = RED
                    self._rot_dir(avo)
            else:
                tio = avo.esq
                if tio.cor == RED:
                    z.pai.cor = tio.cor = BLACK
                    avo.cor = RED
                    self.recoloracoes += 1
                    z = avo
                else:
                    if z == z.pai.esq:
                        z = z.pai
                        self._rot_dir(z)
                    z.pai.cor = BLACK
                    avo.cor = RED
                    self._rot_esq(avo)
        self.raiz.cor = BLACK

    def altura(self):
        def h(no):
            return 0 if no == self.NIL else 1 + max(h(no.esq), h(no.dir))
        return h(self.raiz)


def comparar(sequencia):
    avl = ArvoreAVL()
    rn = ArvoreRubroNegra()
    for chave in sequencia:
        avl.inserir(chave)
        rn.inserir(chave)
    return [
        ("AVL", avl.altura(), avl.rotacoes, "-"),
        ("Rubro-Negra", rn.altura(), rn.rotacoes, rn.recoloracoes),
    ]


def comparar_detalhado(sequencia):
    avl = ArvoreAVL()
    rn = ArvoreRubroNegra()
    for chave in sequencia:
        avl.inserir(chave)
        rn.inserir(chave)
    return [
        ("AVL", avl.altura(), avl.rotacoes, "-", avl.verificacoes),
        ("Rubro-Negra", rn.altura(), rn.rotacoes, rn.recoloracoes, rn.verificacoes),
    ]
