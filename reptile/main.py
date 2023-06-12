from template import Wanda_reptile, init_database_tables

if __name__ == "__main__":
    init_database_tables = init_database_tables.initialize_database()
    DataSetReptile = Wanda_reptile.WandaReptile()
    from template import DataChart
    DataSetViewCrate = DataChart.DataChart()
    from template import GUI
    gui = GUI.email_yanzheng()
