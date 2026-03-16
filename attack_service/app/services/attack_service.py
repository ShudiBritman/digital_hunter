from dal.sql_dal import attack_update



class Processor:

    @staticmethod
    def process(event):
        attack_update(event)
        return