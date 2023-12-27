from flask import Flask, render_template, request
import pandas as pd

df = pd.read_excel('data/Prediction.xlsx')
data = pd.read_excel('data/second.xlsx')


app = Flask(__name__)

# Render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle form submission
@app.route('/process_data', methods=['POST'])
def process_data():
    district = request.form.get('district')
    prediction = df[df['DISTRICTS'] == district]['Solar_Power_in_KW']
    new_data = data[data['DISTRICTS'] == district]
    value = round(prediction.iloc[0], 2)
    
    return render_template('index.html', prediction = value,
                           district = district,
                           latitude = new_data.iloc[:,1].iloc[0],
                           longitude = new_data.iloc[:,2].iloc[0],
                           temperature = new_data.iloc[:,3].iloc[0],
                           humidity = new_data.iloc[:,4].iloc[0],
                           pressure = new_data.iloc[:,5].iloc[0],
                           prec = new_data.iloc[:,6].iloc[0],
                           snowfall = new_data.iloc[:,7].iloc[0],
                           total_cloud_cover = new_data.iloc[:,7].iloc[0],
                           high_cloud_cover = new_data.iloc[:,8].iloc[0],
                           med_cloud_cover = new_data.iloc[:,9].iloc[0],
                           low_cloud_cover = new_data.iloc[:,10].iloc[0],
                           shortwave_radiation = new_data.iloc[:,11].iloc[0],
                           angle = new_data.iloc[:,12].iloc[0],
                           zenith = new_data.iloc[:, 13].iloc[0],
                           azimuth = new_data.iloc[:,14].iloc[0])



if __name__ == "__main__":
    app.run(debug=True)



