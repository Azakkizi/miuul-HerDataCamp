########################################################################################################################
###   Görev 1 :  List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük ###
###   harfe çeviriniz ve başına NUM ekleyiniz. Numeric olmayan değişkenlerin de isimleri büyümeli.   ###################
########################################################################################################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
# print(df.dtypes)

["NUM_" + column.upper() if df[column].dtype in ["int64", "float64"] else column.upper() for column in df.columns]


########################################################################################################################
###   Görev 2 :  List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin ###
###   isimlerinin sonuna "FLAG" yazınız. Tüm değişkenlerin isimleri büyük harf olmalı.   ###############################
########################################################################################################################

[column.upper() + "_FLAG" if "no" not in column else column.upper() for column in df.columns]


########################################################################################################################
###   Görev 3 :  List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin ##
###   isimlerini seçiniz ve yeni bir dataframe oluşturunuz. Önce verilen listeye göre list comprehension kullanarak  ###
###   new_cols adında yeni liste oluşturunuz. Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ###
###   ve adını new_df olarak isimlendiriniz.   #########################################################################
########################################################################################################################

og_list = ["abbrev", "no_previous"]

new_cols = [column for column in df.columns if column not in og_list]

new_df = df[new_cols]
