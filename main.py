
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from GetData import get_detail
import pandas as pd
import logging

logging.basicConfig(filename='c:\\temp\\assessment.log', filemode='w', format='%(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def import_data(assess_data):

    df_assessed = pd.read_csv(assess_data)
    df_assessed['key_code'] = ''
    df_assessed['zoning_code'] = ''
    for i, row in df_assessed.iterrows():
        search_key = ''
        temp_key = ''  # temp_key holds the data until we perform padding
        x = 0  # used to perfom the first 2 sections of the TaxKey
        tax_key = row['Print Key']  # TaxKey is the Tax Map code on the tax roll

        # print(TaxKey)
        count = 0
        for key in tax_key:
            length_tax_key = len(tax_key)
            count += 1

            if x != 2:
                if key.isdigit():
                    temp_key += key
                else:
                    real_key = temp_key.zfill(3)
                    search_key += real_key
                    temp_key = ''
                    # print(real_key)
                    x += 1
            else:  # this pads the 3rd item with 4
                if key.isdigit():
                    temp_key += key
                else:
                    real_key = temp_key.zfill(4)
                    search_key += real_key
                    temp_key = ''
                    # print(real_key)
                    x += 1
            if count == length_tax_key:
                real_key = temp_key.zfill(3)
                search_key += real_key + '0000'
                # print(real_key)
        if len(search_key) != 20:
            search_key += '000'
        print(tax_key)
        print(search_key)

        try:
            zone_code = get_detail(search_key)
            df_assessed['key_code'][i] = search_key
            df_assessed['zoning_code'][i] = zone_code
        except:
            logging.info('Map key ' + tax_key)

    df_assessed.to_csv("c:\\temp\\FultonAssesScrubbed.csv")


if __name__ == '__main__':
    import_data("c:\\temp\\FULTON_AssessmentRole.csv")
