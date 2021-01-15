# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def ImportData(assessdata):

    df_assessed = pd.read_csv(assessdata)
    df_assessed['printkey'] = ''
    for i, row in df_assessed.iterrows():
        search_key = ''
        temp_key = ''  # temp_key holds the data until we perform padding
        x = 0 # used to perfom the first 2 sections of the TaxKey
        TaxKey = row['Print Key'] # TaxKey is the Tax Map code on the tax roll

        # print(TaxKey)

        count = 0
        for key in TaxKey:
            lengthTaxkey = len(TaxKey)
            count += 1

            if x !=2:
                if key.isdigit():
                    temp_key += key
                else:
                    real_key = temp_key.zfill(3)
                    search_key += real_key
                    temp_key = ''
                    # print(real_key)
                    x += 1


            else: # this pads the 3rd item with 4
                if key.isdigit():
                    temp_key += key
                else:
                    real_key = temp_key.zfill(4)
                    search_key += real_key
                    temp_key = ''
                    # print(real_key)
                    x += 1
            if count == lengthTaxkey:
                real_key = temp_key.zfill(3)
                search_key += real_key + '0000'
                # print(real_key)
        if len(search_key) != 20:
            search_key += '000'

        print(search_key)
        df_assessed['printkey'][i]= search_key

    print(df_assessed[['Print Key', 'printkey']].head())
    print(df_assessed[['Print Key', 'printkey']].tail())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ImportData("c:\\temp\FULTON_AssessmentRole.csv")

