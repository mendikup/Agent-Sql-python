import DBconection
from models.agent import Agent

class AgentDbManeger:

    def __init__(self):
        self.db = DBconection.DbConectore()
        self.cursor = self.db.get_conection()

    def get_all_agent(self):
        self.cursor.execute("SELECT * FROM agents")
        rows = self.cursor.fetchall()

        agents = []
        for row in rows:
            agent = Agent(
                codeName=row["codeName"],
                realName=row["realName"],
                location=row["location"],
                status=row["st"],
                missionsCompleated=row["missionCompleted"],
                id=row["id"]
            )
            agents.append(agent)
        return agents

db = AgentDbManeger()
agents = db.get_all_agent()

for agent in agents:
    print(agent)
