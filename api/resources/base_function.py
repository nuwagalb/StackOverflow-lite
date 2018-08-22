class BaseFunction:
    def __init__(self, table_details):
        self.record_details = []

    def save(self):
        id = self.generate_id(self)
        if self.record_details:
            return id
        else:
            return id

    @staticmethod
    def generate_id(self):
        latest_record = self.record_details[-1]
        if latest_record.get('id'):
            return latest_record['id'] + 1
        else:
            return "Error in creating record id"



