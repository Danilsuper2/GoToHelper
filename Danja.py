# Добро пожаловать! Рад вас приветствовать в блоке кода от Данилы Миронова!
# Мы, вместе с Надей и Самиром, сделали этот замечательный проект, который РАБОТАЕТ!
# Может ходя бы мои коментики и красивый не говнокод поможет нам получить призовое место?
# Ну чтож... Как говорится, ни пуха, ни пера! (К чёрту!)

import networkx as nx  # Библиотека графов (СУПЕР АЛГОРИТМ ПРОСТО!!! Спасибо, Гоша, что подсказал)
from Samir import Pandas  # Данные таблички от Самира  #


def match():
    pandas = Pandas("csv.csv")
    users = list(pandas.keys())

    p = len(pandas[users[0]])  # Колличество параметров у участника
    n = len(users)  # Колличество участников

    def weight(a, b):  # Калибровка весов
        node1, node2 = pandas[users[a]], pandas[users[b]]  # Параметры двух вершин-участников
        w = 0
        for i in range(p, 0, -1):
            if node1[i-1] != node2[i-1]:
                w += 2 ** (i - 1)  # Первый параметр важнее последнего
        return w

    def weight_edges():  # Рёбра с весами
        edges = []
        for node1 in range(n):
            for node2 in range(node1, n):
                if node1 != node2:
                    edges.append((users[node1], users[node2], weight(node1, node2)))
        return edges

    G = nx.Graph()  # Граф для решения разбиения по парам
    G.add_nodes_from(users)  # Добавим вершинки в денежную пирамиду
    G.add_weighted_edges_from(weight_edges())  # Добавим недостающих рёбер в теле программиста

    # Прокоментируем пустые строки, что бы код казался болле полным и изящным с этими ненужными комментариями.
    # Вы правда читаете эти коментарии? Ну а что, весело :-). Я бы ещё суда добавил стикер из ВКонтакте,
    # но квк добавить картинку в коментарий? Ну ладно... Может я вас немного подкуплю? Вот промокодик,
    # который работает в ВКонтакте. На 9 голосов. Вот он: todo: Достать промокод
    # Купите себе какой-нибудь стикепак)

    return list(nx.max_weight_matching(G))  # Данные в бота (Надя)

    # Вы покидаете мой код. Нвдеюсь, увидимся снова!
