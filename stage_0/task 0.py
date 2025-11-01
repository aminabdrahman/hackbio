import pandas as pd

data = {
    'name':['Vishnushiri','Joy','Victor','Aakash','Mary','Opemidimeji','Amin','Oluwaseun','Ishita','Opeoluwa','Olorunfemi'],
    'slack_username':['vishnu shiri','Abiodun Joy','ONAH','Aakash Deva Thirukonda','Alo Yetunde Mary','Opemidimeji Osatoyinbo','Amin',
                       'Oluwaseun Awosise','Ishita Chopra','Eadencre8ives','Fem'],
    'country':['India','Nigeria','Nigeria','Sweden','Nigeria','Nigeria','Malaysia','Nigeria','India','Nigeria','Nigeria'],
    'hobby':["Reading","Exploring","Footballing","cooking","Reading","Exploring","Reading","Watching Sitcoms","Reading","Watching Movies","Watching Movies"],
    'affiliations':["Bioinformatician","Statistician","Bioinformatician","-","Bioinformatician","Microbiologist","Molecular biologist","Computational Biology",
                    "Bioinformatican","Microbiology","Cell Biology"],
    'DNA_seq':['SOD1','-','-','TP53','DNMT3A','D86923','TERT','BRCA1','BCL2','BRCA1','SONICHEDGEHOG']
}

df = pd.DataFrame(data).set_index('name')
df.index = df.index.str.upper()
name = str(input('Write you name here:')).upper()
info = df.loc[name]
info