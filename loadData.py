# sudo python3 -m pip install pip --upgrade
# sudo python3 -m pip install py2neo
from py2neo import *
import pandas as pd

class TopicosI:

	GRAPH = Graph(password="ifg")

	def loadDatabase(self):
		df = pd.read_csv('data.txt', sep=',')
		print(df)
		for index, linha in df.iterrows():
			tx = self.GRAPH.begin()
			p = Node("Pessoa", nome=linha['pessoa'])
			h = Node("Hobbie", nome=linha['hobbie'])
			t = Node("Profissao", nome=linha['profissao'])
			tx.merge(p)
			tx.merge(h)
			tx.merge(t)
			p_h = Relationship(p, "GOSTA_DE", h)
			p_t = Relationship(p, "QUER_SER", t)
			tx.create(p_h)
			tx.create(p_t)
			tx.commit()


topicos  = TopicosI();

topicos.loadDatabase()