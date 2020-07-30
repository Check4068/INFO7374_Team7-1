import uvicorn
import pandas as pd
from fastapi import FastAPI, Query

app = FastAPI()

npf = pd.read_csv('ncf_predict.csv')
npa = pd.read_csv('npa_predict.csv')

# Mapping back the wordembedding code to words for NPA
propertyMapping = ['Authentic', 'Japanese', 'beautifully', 'tasty', 'organic',
                   'gluten-free', 'GMO-free', 'all-natural', 'artificial-ingredient-free',
                   'classic', 'trendy', 'healthy']


@app.get('/')
async def index():
    return {"text": "Hello API Masters"}


@app.get('/ncf/{userID}')
async def get_npf(userID):
    df = npf.loc[npf['userID'] == int(userID)]
    df_sorted = df.sort_values('rating', ascending=False)
    df_head = df_sorted.head(3)
    df_product = df_head['products'].drop_duplicates()
    return df_product


@app.get('/npa/{userID}')
async def get_npa(userID):
    df = npa.loc[npa['User'] == int(userID)]
    df_sorted = df.sort_values('ImpressionID', ascending=False)
    encoded = df_sorted['CandidateNews'].values[0][1:-1].split(',')
    decode = []
    for e in encoded:
        index = int(e.strip())
        decode.append(propertyMapping[index])
    return decode

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
