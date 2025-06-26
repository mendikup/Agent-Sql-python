from DALL.agentDbMeneger import AgentDbManeger


class Menu:



    def start(self):

        agntDBmngr = AgentDbManeger()

        print("-------welcome to EAGLE AGENT system---------")
        print()

        chose=""

        while chose!="5":
            print("       what would you like to do?")
            print("           1.to add new agent ")
            print("           2.deleat agent  ")
            print("           3.get agent by id")
            print("           4 get all agent")

            chose= input()

            if chose=="4":
                agents= agntDBmngr.get_all_agent()

                for agent in agents:
                    print(agent)
                    print()





menu=Menu()
menu.start()