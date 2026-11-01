class Procedure:
    def __init__(self, ProcedureID, ProcedureName, ProcedureRunTime):
        self.ProcedureID = ProcedureID
        self.ProcedureName = ProcedureName
        self.ProcedureRunTime = ProcedureRunTime

class DataBase:
    def __init__(self, DataBaseID, DataBaseName):
        self.DataBaseID = DataBaseID
        self.DataBaseName = DataBaseName

class ProceduresOfBase:
    def __init__(self, DataBaseID, ProcedureID):
        self.DataBaseID = DataBaseID
        self.ProcedureID = ProcedureID

def main():
    procedures = [
        Procedure(1, "ArchiveLogs",        150),
        Procedure(2, "BackupDatabase",     320),
        Procedure(3, "CleanTempTables",     45),
        Procedure(4, "UpdateStatistics",   210),
        Procedure(5, "GenerateReport",     500),
        Procedure(6, "SyncReplicas",       275),
    ]
    databases = [
        DataBase(10, "AccountingDB"),
        DataBase(20, "HR_DataBase"),
        DataBase(30, "AnalyticsDB"),
    ]
    procedures_of_base = [
        ProceduresOfBase(10, 1),
        ProceduresOfBase(10, 2),
        ProceduresOfBase(10, 3),
        ProceduresOfBase(20, 4),
        ProceduresOfBase(20, 5),
        ProceduresOfBase(30, 6),
    ]

    db_dict = {db.DataBaseID: db for db in databases}
    proc_dict = {proc.ProcedureID: proc for proc in procedures}

    key = 'A'
    query1 = [(proc.ProcedureName, db_dict[pair.DataBaseID].DataBaseName)
            for pair in procedures_of_base
            for proc in [proc_dict[pair.ProcedureID]]
            if proc.ProcedureName[0] == key]
    print(*query1, end ='\n\n')

    query2 = [(db.DataBaseName, min(proc_dict[pair.ProcedureID].ProcedureRunTime
                for pair in procedures_of_base if pair.DataBaseID == db.DataBaseID))
            for db in databases]
    print(*query2, end ='\n\n')

    query3 = sorted([(db.DataBaseName, [proc_dict[pair.ProcedureID].ProcedureName
                                        for pair in procedures_of_base
                                        if pair.DataBaseID == db.DataBaseID])
                    for db in databases],
                    key=lambda x: x[1])
    print(*query3)

if __name__ == '__main__':
    main()
