from sql_dal.dql_dal import update_table


class Processor:

    @staticmethod
    def process(data):
        update_table(data)
        return